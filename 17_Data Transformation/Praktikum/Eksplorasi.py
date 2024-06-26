from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
import pandas as pd
import requests

# Fungsi untuk mendapatkan data dari API
def extract_data():
    response = requests.get("https://fakestoreapi.com/products")
    data = response.json()
    df = pd.DataFrame(data)
    df.to_csv("/tmp/product_data.csv", index=False)

# Fungsi untuk melakukan transformasi data
def transform_data():
    df = pd.read_csv("/tmp/product_data.csv")

# Fungsi untuk mengekspor hasil analisis ke file Excel
def export_to_excel():
    df = pd.read_csv("/tmp/product_data.csv")
    # Lakukan ekspor data ke file Excel
    df.to_excel("/tmp/product_analysis.xlsx", index=False)

# Fungsi untuk membuat visualisasi data
def visualize_data():
    df = pd.read_csv("/tmp/product_data.csv")

# Definisikan default arguments untuk DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 4, 18),
    'retries': 1
}

# Inisialisasi DAG
dag = DAG(
    'data_analysis_workflow',
    default_args=default_args,
    description='Workflow untuk melakukan analisis data',
    schedule_interval=None,
)

# Task 1 - Ekstraksi Data
extract_data_task = PythonOperator(
    task_id='extract_data',
    python_callable=extract_data,
    dag=dag,
)

# Task 2 - Transformasi Data dengan Pandas
transform_data_task = PythonOperator(
    task_id='transform_data',
    python_callable=transform_data,
    dag=dag,
)

# Task 3 - Ekspor Hasil Analisis
export_to_excel_task = PythonOperator(
    task_id='export_to_excel',
    python_callable=export_to_excel,
    dag=dag,
)

# Task 4 - Visualisasi Data
visualize_data_task = PythonOperator(
    task_id='visualize_data',
    python_callable=visualize_data,
    dag=dag,
)

# Mendefinisikan urutan task
extract_data_task >> transform_data_task >> export_to_excel_task >> visualize_data_task
