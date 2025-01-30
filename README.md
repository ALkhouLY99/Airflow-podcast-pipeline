![image](https://github.com/user-attachments/assets/fae51b8d-8656-40eb-8eb0-b7a824b3aca2)

# ![podcatch_airflow drawio](https://github.com/user-attachments/assets/4fbf693b-c9ab-4f4d-97d3-b7ea343f9903)
🎧 PodCatch: Airflow Podcast Pipeline 🚀  
_Automate podcast downloads using Python, Airflow & SQLite3._
**This project, tentatively titled "PodCatch," leverages the power of Python, SQLite3, and Apache Airflow to efficiently download podcasts.**
---
## 📌 1: Install Airflow and Configure
### Prerequisites:
- Recommend creating a virtualenv
  -  python -m venv myenv
        - source myenv/bin/activate  # (Linux/Mac)
        - myenv\Scripts\activate     # (Windows)
- Install airflow
  - Follow the official Airflow setup guide:
## 🔗 Airflow Installation Guide
### 1️⃣ Set Environment Variables
  ``` 
    export AIRFLOW_VERSION=2.10.4
    export PYTHON_VERSION=3.12
    export CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"
  ```
### 2️⃣ Install Airflow
``` pip install "apache-airflow==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}" ```
## Run Airflow Server
- Initialize Airflow:
  - run ```airflow standalone```
## Install dependencies:
  - run ```pip install -r requirements.txt```
    
