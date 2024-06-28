from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.python import PythonOperator
import requests
import pandas as pd

default_args = {
  "owner": "yazid",
  "retries": 5,
  "retry_delay": timedelta(minutes=5),
}

def get_data_from_api():
  api_url = "https://fakestoreapi.com/products"
  response = requests.get(api_url)
  data = response.json()
  return data

def write_to_csv(data, **kwargs):
  df = pd.DataFrame(data)
  df.to_csv("products.csv", index=False)

def write_to_txt(data, **kwargs):
  # Access data from the upstream task using XCom
  data_from_api = kwargs['task_instance'].xcom_pull(task_ids='get_data_from_api')
  with open("products.txt", "w") as f:
    for item in data_from_api:
      f.write(str(item) + "\n")

def print_success_message(**kwargs):
  print("done!")

# Define the DAG object
with DAG(
  dag_id="get_data_dag",
  default_args=default_args,
  start_date=datetime(2024, 4, 12),
  schedule_interval='@daily', 
) as dag:

  get_data_from_api_task = PythonOperator(
      task_id="get_data_from_api",
      python_callable=get_data_from_api,
      provide_context=True,
  )

  write_to_csv_task = PythonOperator(
      task_id="write_to_csv",
      python_callable=write_to_csv,
      provide_context=True,
  )

  write_to_txt_task = PythonOperator(
      task_id="write_to_txt",
      python_callable=write_to_txt,
      provide_context=True,
  )

  print_success_message_task = PythonOperator(
      task_id="print_success_message",
      python_callable=print_success_message,
      provide_context=True,
  )

  # Define task dependencies
  get_data_from_api_task >> write_to_csv_task
  get_data_from_api_task >> write_to_txt_task
  write_to_csv_task >> print_success_message_task
  write_to_txt_task >> print_success_message_task