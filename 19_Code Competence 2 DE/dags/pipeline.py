import os
import sys
import numpy as np
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from .data_lake_builder import DataLakeBuilder
from .data_warehouse_loader import DataWarehouseLoader

# Cetak sys.path untuk memeriksa jalur direktori yang tersedia
print(sys.path)

default_args = {
    'owner': 'afril',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'data_pipeline',
    default_args=default_args,
    description='A DAG to automate data pipeline',
    schedule_interval=timedelta(days=1),
    start_date=datetime(2024, 4, 30),
    catchup=False
)

def data_ingestion():
    data_lake_builder = DataLakeBuilder()

    csv_files = ['events.csv', 'customers.csv', 'tickets.csv', 'transactions.csv', 'customer_feedback.csv']
    data_source_dir = r'C:\Users\user\OneDrive\Documents\GitHub\data-engineer_afril-istihawa\19_Code Competence 2 DE\data_source'
    parquet_dir = 'parquet_files'

    if not os.path.exists(parquet_dir):
        os.makedirs(parquet_dir)

    for file in csv_files:
        file_path = os.path.join(data_source_dir, file)
        df = data_lake_builder.read_csv_data(file_path)
        df = data_lake_builder.handle_missing_values(df)
        numeric_columns = df.select_dtypes(include=[np.number]).columns
        for column in numeric_columns:
            df = data_lake_builder.handle_outliers(df, column)
        parquet_file = os.path.join(parquet_dir, file.split('.')[0] + '.parquet')
        data_lake_builder.save_to_parquet(df, parquet_file)

def data_transformation():
    loader = DataWarehouseLoader()

    events_df = loader.load_data('parquet_files/events.parquet')
    customers_df = loader.load_data('parquet_files/customers.parquet')
    tickets_df = loader.load_data('parquet_files/tickets.parquet')
    transactions_df = loader.load_data('parquet_files/transactions.parquet')
    customer_feedback_df = loader.load_data('parquet_files/customer_feedback.parquet')

    tickets_sold, revenue, avg_rating = loader.transform_data(transactions_df, tickets_df, events_df, customer_feedback_df)

    loader.save_to_warehouse(tickets_sold, 'tickets_sold_per_event')
    loader.save_to_warehouse(revenue, 'revenue_per_event')
    loader.save_to_warehouse(avg_rating, 'avg_rating_per_event')

ingest_task = PythonOperator(
    task_id='data_ingestion',
    python_callable=data_ingestion,
    dag=dag
)

transform_task = PythonOperator(
    task_id='data_transformation',
    python_callable=data_transformation,
    dag=dag
)

ingest_task >> transform_task
