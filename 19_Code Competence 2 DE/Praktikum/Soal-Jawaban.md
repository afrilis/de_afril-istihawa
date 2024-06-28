# Soal Jawaban Code Competance 2

# Persiapan Lingkungan Pengembangan

Membuat virtual environment venv_code2. Modifikasi environment untuk memasukkan dependencies baru yang diperlukan, seperti library pandas, airflow, dan library lain yang diperlukan.

![image](..//Screenshots/01.png)

Download dataset dan kemudian simpan kedalam folder data_source.

![image](..//Screenshots/02.png)

# Data Ingestion dan Persiapan Data Lake / Data Werehouse

- Penyiapan Skrip Python

Buat file Python dengan nama data_ingestion.py.

![image](..//Screenshots/03.png)

Dalam file ini, buat kelas dengan nama DataLakeBuilder.

![image](..//Screenshots/04.png)

- Kelas DataLakeBuilder

Kelas ini harus memiliki metode untuk membaca data dari file CSV, menangani missing values dan outliers, dan menyimpan data ke format yang sesuai untuk Data Lake.

read_csv_data(self, file_path): Metode untuk membaca data dari file CSV.

handle_missing_values(self, df): Metode untuk menangani missing values dalam DataFrame.

handle_outliers(self, df, column): Metode untuk menangani outliers dalam kolom tertentu dari DataFrame.

save_to_parquet(self, df, file_name): Metode untuk menyimpan DataFrame ke file Parquet.

![image](..//Screenshots/05.png)

- Metode read_csv_data

Gunakan pandas untuk membaca file CSV.

Contoh: pd.read_csv(file_path) di mana file_path adalah path ke file CSV.

![image](..//Screenshots/06.png)

- Metode handle_missing_values

Terapkan strategi untuk menangani missing values, seperti pengisian nilai (imputation) atau penghapusan baris/kolom.

Contoh: Menggunakan df.fillna() atau df.dropna() dari pandas.

![image](..//Screenshots/07.png)

- Metode handle_outliers

Gunakan teknik statistik untuk mendeteksi dan menangani outliers.

Contoh: IQR (Interquartile Range) untuk mengidentifikasi outliers dan kemudian menggantinya atau menghapusnya.

![image](..//Screenshots/08.png)

- Metode save_to_parquet

Simpan DataFrame yang telah diolah ke format Parquet, yang efisien untuk Data Lake.

Contoh: df.to_parquet(file_name).

![image](..//Screenshots/09.png)

- Eksekusi Script

Buat instance dari DataLakeBuilder dan panggil metode-metodenya untuk setiap file CSV (events.csv, customers.csv, tickets.csv, transactions.csv, dan customer_feedback.csv).

Pastikan semua file terbaca dan diolah dengan benar, lalu simpan dalam format Parquet.

![image](..//Screenshots/10.png)

- Validasi Data

Setelah semua data disimpan dalam format Parquet, buat metode untuk memvalidasi atau menampilkan ringkasan data.

Contoh: Metode validate_data(self, file_path) yang membaca file Parquet dan menampilkan ringkasan statistik atau beberapa baris awal data.

![image](..//Screenshots/11.png)

# Transformasi Data dan Pemuatan ke Data Warehouse

- Penyiapan Skrip Python untuk Transformasi Data

Buat file Python baru dengan nama data_transformation.py.

![image](..//Screenshots/12.png)

Dalam file ini, buat kelas dengan nama DataWarehouseLoader.

![image](..//Screenshots/13.png)

- Kelas DataWarehouseLoader

Kelas ini harus memiliki metode untuk membaca data dari Data Lake, melakukan transformasi data, dan menyimpan data yang telah ditransformasi ke Data Warehouse.

load_data(self, file_path): Metode untuk membaca data dari Data Lake (format Parquet).

transform_data(self, df): Metode umum untuk melakukan transformasi data.

save_to_warehouse(self, df, table_name): Metode untuk menyimpan data ke Data Warehouse.

![image](..//Screenshots/14.png)

- Metode load_data

Gunakan pandas untuk membaca file Parquet dari Data Lake.

Load data dari file Parquet untuk tabel events, customers, tickets, transactions, dan customer_feedback.

Contoh: pd.read_parquet(file_path).

![image](..//Screenshots/15.png)

- Metode Transform Data

Menggabungkan Data untuk Analisis

Gabungkan tabel transactions dengan tickets berdasarkan ticket_id, dan kemudian dengan events berdasarkan event_id.

Menghitung Jumlah Tiket yang Terjual per Acara

Gunakan groupby pada kolom event_id atau name dari tabel events.

Hitung jumlah tiket yang terjual dengan mengagregasi kolom quantity menggunakan fungsi sum.

Menghitung Total Pendapatan dari Setiap Acara

Dari DataFrame yang digabungkan sebelumnya, gunakan groupby pada kolom event_id atau name.

Hitung total pendapatan dengan mengagregasi total_amount menggunakan fungsi sum.

Analisis Feedback Pelanggan

Gabungkan tabel customer_feedback dengan transactions berdasarkan transaction_id untuk mengaitkan feedback dengan transaksi.

Analisis rating rata-rata per acara.

![image](..//Screenshots/16.png)

- Metode Save to Werehouse

Penamaan File Hasil Transformasi

Tickets_sold_per_event.parquet

Revenue_per_event.parquet

Feedback_analysis.parquet

Setup Google Cloud Storage/Supabase

Pastikan Anda memiliki akses ke Google Cloud Storage/Supabase.

Buat bucket yang akan digunakan sebagai Data Warehouse, jika belum ada.

Struktur Folder Berdasarkan DateTime

Untuk mengorganisir data, gunakan struktur folder berdasarkan tanggal. Format yang umum adalah YYYY/MM/DD atau YYYY-MM-DD.

Contoh: Untuk data yang diproses pada tanggal 20 November 2023, folder bisa bernama 2023/11/20 atau 2023-11-20.

![image](..//Screenshots/17.png)

![image](..//Screenshots/18.png)

# Orkestrasi Workflow dengan Apache Airflow

Buatlah DAG (Directed Acyclic Graph) di Apache Airflow untuk mengotomatisasi proses pengambilan data, transformasi, dan pemuatan ke Data Warehouse.

DAG harus mencakup task untuk data ingestion, data transformation, dan loading data ke warehouse.

Jelaskan bagaimana Anda akan menjadwalkan DAG ini dan mengatur dependencies antar tasks.

![image](..//Screenshots/19.png)

![image](..//Screenshots/20.png)

![image](..//Screenshots/21.png)