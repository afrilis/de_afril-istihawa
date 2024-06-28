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

# Fungsi untuk transformasi data (membersihkan data)
def transform_data(data):
    # Hapus data duplikat
    data = data.drop_duplicates()
    # Hapus baris dengan data yang tidak lengkap
    data = data.dropna()
    return data

# Fungsi untuk memuat data ke Google Storage Firebase dalam format CSV
def load_data_to_gcs(data, bucket_name, file_name):
    bucket = storage.bucket(bucket_name)
    blob = bucket.blob(file_name)
    data.to_csv(file_name, index=False)
    blob.upload_from_filename(file_name)

# Main function
def main():
    # Nama file CSV
    csv_file = 'survey.csv'
    # Nama bucket Google Storage Firebase
    bucket_name = 'de-with-cloud-3b5c3'
    # Nama file untuk disimpan di Google Storage Firebase
    file_name = 'survey_cleaned.csv'

    # Ekstraksi data dari file CSV
    data = extract_data(csv_file)
    # Transformasi data
    cleaned_data = transform_data(data)
    # Memuat data yang telah dibersihkan ke Google Storage Firebase
    load_data_to_gcs(cleaned_data, bucket_name, file_name)

if __name__ == "__main__":
    main()
