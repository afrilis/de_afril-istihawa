import pandas as pd
import firebase_admin
from firebase_admin import credentials, storage

# Inisialisasi Firebase Admin SDK
cred = credentials.Certificate("accountKey.json")
firebase_admin.initialize_app(cred, {'storageBucket': 'de-with-cloud-3b5c3'})

# Fungsi untuk ekstraksi data dari file CSV
def extract_data(csv_file):
    data = pd.read_csv(csv_file)
    return data

# Fungsi untuk transformasi data
def transform_data(data):
    # Mengambil data pada kolom payment_method yang menggunakan credit card
    credit_card_data = data[data['payment_method'] == 'credit_card']
    
    # Mengambil data pada kolom status yang dikategorikan success
    success_data = credit_card_data[credit_card_data['status'] == 'success']
    
    return success_data[['transaction_id', 'transaction_date', 'customer_name', 'transaction_amount', 'item_category', 'item_name', 'payment_method', 'status']]

# Fungsi untuk memuat data ke Google Storage Firebase dalam format CSV
def load_data_to_gcs(data, bucket_name, file_name):
    bucket = storage.bucket(bucket_name)
    blob = bucket.blob(file_name)
    data.to_csv(file_name, index=False)
    blob.upload_from_filename(file_name)

# Main function
def main():
    # Nama file CSV
    csv_file = 'data_prioritas1-2.csv'
    # Nama bucket Google Storage Firebase
    bucket_name = 'de-with-cloud-3b5c3'
    # Nama file untuk disimpan di Google Storage Firebase
    file_name = 'result-prioritas1-2.csv'

    # Ekstraksi data dari file CSV
    data = extract_data(csv_file)
    # Transformasi data
    cleaned_data = transform_data(data)
    # Memuat data yang telah dibersihkan ke Google Storage Firebase
    load_data_to_gcs(cleaned_data, bucket_name, file_name)

if __name__ == "__main__":
    main()
