# Airflow-podcast-pipeline
This project, tentatively titled "PodCatch," leverages the power of Python, SQLite3, and Apache Airflow to efficiently download podcasts.
---
# 1: Install airflow and configure
- Recommend creating a virtualenv -->  python -m venv myenv
- Install airflow
  - steps how to install Airflow     
  """
    AIRFLOW_VERSION=2.10.4    -->   https://airflow.apache.org/docs/apache-airflow/stable/start/local.html
    PYTHON_VERSION = 3.12     -->    python --version
    CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"
    pip install "apache-airflow==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"
    """
    
