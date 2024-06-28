from datetime import datetime, timedelta
import requests
import json
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
from airflow import DAG
from airflow.operators.python import PythonOperator
from google.cloud import storage


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2022, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}

dag = DAG('ETL_pipeline',
          default_args=default_args,
          description='A simple ETL pipeline',
          schedule_interval=timedelta(days=1),
        )

def extract_data():
    response = requests.get('https://fakestoreapi.com/products')
    data = response.json()
    return data

def transform_data(data):
    df = pd.DataFrame(data)
    df = df[df['price'] > 100]
    transformed_data = df[['title', 'price', 'description', 'category']]
    return transformed_data

def load_data_to_gcs(data, bucket_name, file_name):
    table = pa.Table.from_pandas(data)
    with pa.BufferOutputStream() as buf:
        pq.write_table(table, buf)
        buf.flush()
        bytes_ = buf.getvalue()
        client = storage.Client()
        bucket = client.get_bucket(bucket_name)
        blob = bucket.blob(file_name)
        blob.upload_from_string(bytes_)


extract_data = PythonOperator(
    task_id='extract_data',
    python_callable=extract_data,
    dag=dag,
)

transform_data = PythonOperator(
    task_id='transform_data',
    python_callable=transform_data,
    provide_context=True,
    dag=dag,
)

load_data_to_gcs = PythonOperator(
    task_id='load_data_to_gcs',
    python_callable=load_data_to_gcs,
    op_args=['{{ task_instance.xcom_pull(task_ids="transform_data") }}', 'de-with-cloud-3b5c3', 'eksplorasi.parquet'],
    dag=dag,
)

extract_data >> transform_data >> load_data_to_gcs
