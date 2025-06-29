from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import pandas as pd

def download():
    df = pd.read_csv('https://example.com/sample_data.csv')
    df.to_csv('/data/raw/sample.csv', index=False)

def transform():
    df = pd.read_csv('/data/raw/sample.csv')
    # example transform
    df = df.dropna()
    df.to_csv('/data/raw/transformed.csv', index=False)

def pipeline():
    download(); transform()

# Default arguments for the DAG
default_args = {
    'owner': 'nguyen_quoc_cuong',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG('data_pipeline', 
         start_date=datetime(2025,1,1), 
         default_args=default_args,
         schedule_interval='@daily', 
         catchup=False) as dag:
    run = PythonOperator(task_id='run_all', python_callable=pipeline)