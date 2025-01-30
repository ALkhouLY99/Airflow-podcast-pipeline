from airflow.decorators import dag,task
from airflow.utils.dates import days_ago
from datetime import timedelta
import pendulum
import requests
import xmltodict
from airflow.providers.sqlite.operators.sqlite import SqliteOperator
from airflow.providers.sqlite.hooks.sqlite import SqliteHook
import os



headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

PODCAST_URL = "https://www.marketplace.org/feed/podcast/marketplace/"

EPISODE_FOLDER ="/workspaces/113965280/Podcast_Airflow-pro/episodes"


@dag( dag_id = 'podcast_pro',schedule_interval='@daily',start_date= days_ago(1),catchup=False,
     default_args={'retry_delay': timedelta(minutes=5)  # Retry after 5 minutes
    })
def podcast_pro():

    # task-1
    create_db = SqliteOperator(
        task_id= 'create_tables_sqllite',
        sqlite_conn_id='podcasts',
        sql = r"""CREATE TABLE IF NOT EXISTS episodes (
                    link TEXT PRIMARY KEY,
                    title TEXT,
                    filename TEXT,
                    published TEXT,
                    description TEXT,
                    transcript TEXT);
                """ )

    # task-2
    @task
    def get_episodes():
        """ get episodes from url """

        try:
            data = requests.get(PODCAST_URL,headers=headers)
            data.raise_for_status()       # Raise an error for bad responses (4xx and 5xx)
            feed = xmltodict.parse(data.text)
            episodes= feed["rss"]["channel"]["item"]
            print(f"found {len(episodes)}episodes.")

            return episodes

        except Exception as err:
            print(f"An error occurred: {err}")
            return []



    podcast_episodes= get_episodes()
    create_db.set_downstream(podcast_episodes)

    # task-3
    @task
    def load_episodes(episodes):
        """Load new episodes into the SQLite database."""
        if not episodes:
            print("⚠️ No episodes to load.")
            return

        hook = SqliteHook(sqlite_conn_id='podcasts')
        stored_episodes=set(hook.get_pandas_df("select link from episodes;")["link"])  ## set() is better than (.values <--> numpyarray)
        new_episodes =[]

        for epi in episodes:
            if epi["link"] not in stored_episodes:
                filename = f"{epi["link"].split('/')[-1]}.mp3"
                new_episodes.append([epi["link"],
                                    epi.get("title","No Title"),
                                    epi.get("pubDate","Unknown Date"),
                                    epi.get("description", "No Description"),
                                    filename
                                     ])
        hook.insert_rows(table='episodes',rows=new_episodes,target_fields=["link","title","published",
                                                                           "description","filename",
                                                                           None  # Placeholder for transcript
                                                                            ])


    load_episodes(podcast_episodes)

    # task-4
    @task
    def download_episodes(episodes):

         """Download audio files only if episodes exist."""
         if not episodes:
             print("⚠️ No episodes available for download.")
             return

         for epi in episodes:

            filename = f"{epi["link"].split('/')[-1]}.mp3"
            audio_path = os.path.join(EPISODE_FOLDER,filename)
            # Check if the file already exists
            if not os.path.exists(audio_path):
                print(f"Downloading {filename}")
                audio_url = epi["enclosure"]["@url"]
            # Perform the HTTP request to download the file
                audio = requests.get(audio_url)
                audio.raise_for_status()   # Ensure the download was successful
                with open(audio_path,"wb+") as f:
                    f.write(audio.content)

            else:
                print(f"{filename} already exists. Skipping download.")

    download_episodes(podcast_episodes)


result = podcast_pro()
