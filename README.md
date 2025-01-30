# 🎧 PodCatch: Airflow Podcast Pipeline 🚀  
_Automate podcast downloads using Python, Airflow & SQLite3._
<p align="center">
 <img src="https://github.com/user-attachments/assets/8c36ca4f-f979-4842-8f3e-eb9a8f87cb5b" width="500">

  <img src="https://github.com/user-attachments/assets/fae51b8d-8656-40eb-8eb0-b7a824b3aca2" width="500">
</p>

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
    
