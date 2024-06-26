from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import pandas as pd
import requests
import os

def get_data_from_api():
    # Mendapatkan data dari API
    url = "https://gist.githubusercontent.com/nadirbslmh/b50406d5579e875e6435896c9ff6c80c/raw/cac8007653b6145e9ad0ec69b1e4fd6c1be718e7/transactions.json"
    response = requests.get(url)
    data = response.json()
    return data

def perform_data_cleaning(data):
    # Mengubah data ke dalam DataFrame
    df = pd.DataFrame(data)
    
    # Mengubah format nomor telepon
    df['phone_number'] = '+62' + df['phone_number'].astype(str)
    
    # Mengubah nilai transaksi
    df['transaction_amount'] = 'Rp ' + df['transaction_amount'].astype(str)
    
    # Memfilter data transaksi dengan status success
    df = df[df['transaction_status'] == 'success']
    
    # Menyimpan hasil data cleaning dalam DataFrame
    cleaned_data = df
    
    # Menyimpan DataFrame ke dalam file CSV
    output_path = os.path.join('~\22_Pemahaman tentang Data Quality dan Data Governance', 'cleaned_data.csv')
    cleaned_data.to_csv(output_path, index=False)
    
    return cleaned_data

# Menentukan default arguments untuk DAG
default_args = {
    'owner': 'afril',
    'depends_on_past': False,
    'start_date': datetime(2024, 4, 20),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
}

# Mendefinisikan DAG
dag = DAG(
    'data_cleaning_workflow1',
    default_args=default_args,
    description='Workflow untuk melakukan data cleaning',
    schedule_interval=None,
)

# Operator untuk mendapatkan data dari API
get_data_task = PythonOperator(
    task_id='get_data_from_api',
    python_callable=get_data_from_api,
    dag=dag,
)

# Operator untuk melakukan data cleaning
perform_data_cleaning_task = PythonOperator(
    task_id='perform_data_cleaning',
    python_callable=perform_data_cleaning,
    provide_context=True,
    dag=dag,
)

# Menentukan urutan dari task dalam DAG
get_data_task >> perform_data_cleaning_task
