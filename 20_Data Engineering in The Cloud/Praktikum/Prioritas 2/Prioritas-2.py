import json
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
import firebase_admin
from firebase_admin import credentials, storage
import requests

# Inisialisasi Firebase Admin SDK
cred = credentials.Certificate("accountKey.json")
firebase_admin.initialize_app(cred, {'storageBucket': 'de-with-cloud-3b5c3'})

# Fungsi untuk ekstraksi data dari URL JSON
def extract_data(json_url):
    response = requests.get(json_url)
    data = json.loads(response.text)
    return data

# Fungsi untuk transformasi data
def transform_data(data):
    # Mengkonversi data ke dalam DataFrame
    df = pd.DataFrame(data)
    
    # Mengambil transaksi saham untuk GOOGL, AMZN, MSFT, dan AAPL
    selected_stocks = ['GOOGL', 'AMZN', 'MSFT', 'AAPL']
    filtered_data = df[df['stock_symbol'].isin(selected_stocks)]
    
    # Mengambil data transaksi saham dengan harga di atas 500
    filtered_data = filtered_data[filtered_data['trade_price'] > 500]
    
    return filtered_data

# Fungsi untuk memuat data ke Google Storage Firebase dalam format Parquet
def load_data_to_gcs(data, bucket_name, file_name):
    bucket = storage.bucket(bucket_name)
    blob = bucket.blob(file_name)
    pq.write_table(pa.Table.from_pandas(data), f'tmp_{file_name}')
    blob.upload_from_filename(f'tmp_{file_name}')

    print("Data berhasil dimuat ke Google Cloud Storage.")

# Main function
def main():
    # URL file JSON
    json_url = 'https://gist.githubusercontent.com/nadirbslmh/93b62fdcfa694d4ec07bed9b3c94e401/raw/c07971341361e23fd4f3a880437c4d8e4ebcfafc/stock_trades.json'
    # Nama bucket Google Storage Firebase
    bucket_name = 'de-with-cloud-3b5c3'
    # Nama file untuk disimpan di Google Storage Firebase
    file_name = 'stock_trades.parquet'

    # Ekstraksi data dari URL JSON
    data = extract_data(json_url)
    # Transformasi data
    cleaned_data = transform_data(data)
    # Memuat data yang telah dibersihkan ke Google Storage Firebase
    load_data_to_gcs(cleaned_data, bucket_name, file_name)

if __name__ == "__main__":
    main()
