# PRIORITAS 1

1. Jelaskan perbedaan antara data terstruktur dan data tidak terstruktur. Berikan contoh untuk masing-masing dan bahas bagaimana mereka biasanya disimpan dan diproses.

**Data  terstruktur** adalah data yang memiliki model, format, dan skema, seperti: nama, alamat, kode pos. Data ini tersimpan pada database relational (RDBMS) dan mudah dicari menggunakan SQL (Structured Query Language) yang merupakan bahasa pemrograman query.

**Data tidak terstruktur** adalah data yang memiliki struktur internal tetapi tidak terstruktur melalui data model atau skema. Sehingga memerlukan proses lanjutan agar dapat dicari. Contoh data: teks dokumen, pdf, gambar, video, dan sosial media; seperti data dari twitter, facebook, instagram. 
Data ini biasa tersimpan pada file storage/datalake.


2. Apa itu basis data relasional dan bagaimana cara kerjanya? Berikan contoh penggunaannya dalam dunia nyata.

- Basis data relasional adalah jenis basis data yang menggunakan model relasional untuk menyimpan dan mengelola data. Model relasional mengorganisir data dalam bentuk tabel yang terhubung satu sama lain melalui kunci primer dan kunci asing, menciptakan hubungan antara entitas. Cara kerja basis data relasional umumnya melibatkan struktur data yang terorganisir dalam tabel, dengan setiap baris mewakili entitas tunggal dan kolom mewakili atribut atau field dari entitas tersebut. 

- Contoh penggunaan basis data relasional dalam dunia nyata adalah pada sistem manajemen basis data (DBMS) seperti MySQL, PostgreSQL, SQL Server, dan Oracle. Perusahaan menggunakan basis data relasional untuk menyimpan informasi pelanggan, transaksi penjualan, inventaris barang, dan banyak lagi. Misalnya, sebuah toko online dapat menggunakan basis data relasional untuk menyimpan informasi produk, data pelanggan, dan pesanan, dengan tabel yang saling terhubung melalui kunci primer dan kunci asing untuk menciptakan hubungan yang terstruktur antara data.


3. Jelaskan konsep normalisasi basis data dan mengapa hal ini penting dalam konteks basis data relasional.

Konsep normalisasi basis data adalah proses desain yang digunakan untuk mengorganisir struktur data dalam basis data relasional agar mencapai tingkat efisiensi, integritas, dan konsistensi yang optimal. Tujuan utama normalisasi adalah mengurangi redudansi data, menghindari anomali data, dan meningkatkan fleksibilitas dan kinerja basis data. Normalisasi sangat penting dalam konteks basis data relasional karena membantu memastikan bahwa basis data memiliki struktur yang baik, mudah dipahami, dan efisien dalam menyimpan dan mengakses informasi.


# PRIORITAS 2

Anda diberi tugas untuk merancang sistem basis data untuk sebuah perusahaan e-commerce. Perusahaan ini memiliki data yang sangat beragam, mulai dari data transaksi pelanggan hingga log interaksi pengguna di website. Diskusikan pendekatan yang akan Anda gunakan untuk mengelola data ini, termasuk pemilihan antara basis data relasional dan NoSQL, serta strategi untuk mengintegrasikan data terstruktur dan tidak terstruktur.

Dalam merancang sistem basis data untuk perusahaan e-commerce dengan data yang sangat beragam, ada beberapa faktor yang perlu dipertimbangkan termasuk jenis data, kecepatan akses, skalabilitas, konsistensi, dan kompleksitas struktur data. Berikut adalah pendekatan yang dapat dipertimbangkan:

1. Pemilihan Basis Data Relasional atau NoSQL:

- Basis Data Relasional: 
Cocok digunakan untuk data yang memiliki struktur yang jelas dan hubungan yang kompleks antara entitas. Misalnya, informasi pelanggan, produk, dan transaksi dapat disimpan dalam tabel-tabel yang terhubung melalui kunci primer dan asing. Basis data relasional juga cocok jika kebutuhan query kompleks dan transaksi ACID (Atomicity, Consistency, Isolation, Durability) diperlukan.

- Basis Data NoSQL: 
Lebih cocok digunakan untuk data yang tidak memiliki struktur yang tetap atau terstruktur secara longgar, seperti log interaksi pengguna, data sensor, atau data teks yang tidak terstruktur. Basis data NoSQL seperti MongoDB atau Cassandra dapat memberikan skalabilitas horizontal yang baik dan mendukung penambahan data dengan cepat. Mereka juga lebih fleksibel dalam menangani data semi-struktur atau tidak terstruktur.

2. Strategi Integrasi Data Terstruktur dan Tidak Terstruktur:

- Penggunaan Basis Data Hybrid: Dengan menggunakan kombinasi basis data relasional dan NoSQL dalam sistem basis data hybrid. Data terstruktur seperti informasi pelanggan dan transaksi dapat disimpan dalam basis data relasional, sementara data tidak terstruktur seperti log interaksi pengguna atau data teks dapat disimpan dalam basis data NoSQL.

- Penggunaan Data Lake: Jika data tidak terstruktur sangat beragam dan kompleks, Dapat mempertimbangkan penggunaan data lake untuk menyimpan semua jenis data dalam format mentah. Dari sana, data dapat diolah dan disimpan dalam basis data relasional atau NoSQL sesuai kebutuhan.

3. Strategi Pengelolaan dan Pengaksesan Data:

- ETL (Extract, Transform, Load): Gunakan proses ETL untuk mengambil, mentransformasi, dan memuat data dari berbagai sumber ke dalam basis data Anda. Misalnya, data transaksi dari sistem penjualan dapat diambil dan dimuat ke dalam tabel relasional, sementara log interaksi pengguna dapat dimuat ke dalam basis data NoSQL.

- API dan Integrasi Data: Gunakan API untuk mengintegrasikan data dari sistem yang berbeda ke dalam sistem basis data Anda. Misalnya, API dapat digunakan untuk mengintegrasikan data dari sistem manajemen inventaris atau sistem analitik ke dalam basis data.

Dengan pendekatan ini, pengelola data yang sangat beragam dengan lebih efisien dan memenuhi kebutuhan bisnis perusahaan e-commerce akan terlaksana secara efektif.


# Eksplorasi 

Sebuah perusahaan ingin mengimplementasikan data lake untuk mengelola data besar yang mereka miliki, yang mencakup data terstruktur, semi-terstruktur, dan tidak terstruktur. Jelaskan bagaimana Anda akan merancang dan mengimplementasikan data lake ini, termasuk alat dan teknologi yang akan digunakan, serta bagaimana data lake ini akan berintegrasi dengan sistem data lainnya di perusahaan.

Untuk merancang dan mengimplementasikan data lake yang dapat mengelola data besar yang mencakup data terstruktur, semi-terstruktur, dan tidak terstruktur, berikut adalah langkah-langkah yang dapat diambil beserta alat dan teknologi yang dapat digunakan:

1. Rancang Struktur Data Lake:

- Tentukan kebutuhan dan tujuan penggunaan data lake.
- Identifikasi sumber data yang akan dimuat ke dalam data lake, baik data terstruktur (misalnya, dari basis data relasional), semi-terstruktur (misalnya, dari log aplikasi), maupun tidak terstruktur (misalnya, dari teks atau file gambar).
- Rancang struktur penyimpanan yang sesuai, misalnya menggunakan format seperti Apache Parquet untuk data terstruktur, JSON atau Avro untuk data semi-terstruktur, dan object storage untuk data tidak terstruktur.


2. Pilih Platform Data Lake:

- Apache Hadoop atau Cloudera Data Platform: Platform ini dapat digunakan untuk menyimpan, mengelola, dan menganalisis data besar dengan Apache Hadoop Distributed File System (HDFS) sebagai penyimpanan utama.
- Amazon Web Services (AWS) S3: AWS S3 dapat digunakan sebagai penyimpanan objek yang skalabel untuk data tidak terstruktur dan semi-terstruktur.
- Google Cloud Storage (GCS): GCS juga merupakan penyimpanan objek yang dapat digunakan untuk data tidak terstruktur dan semi-terstruktur.


3. Pilih Alat dan Teknologi Pendukung:

- Apache Spark atau Apache Flink: Alat ini dapat digunakan untuk pemrosesan data streaming dan batch, serta analisis data besar dalam data lake.
- Apache Hive atau Apache Impala: Alat ini dapat digunakan untuk mengakses dan menganalisis data terstruktur dalam data lake dengan SQL-like queries.
- Apache Kafka: Jika Anda memiliki data streaming yang perlu dimuat ke dalam data lake secara real-time, Kafka dapat digunakan sebagai platform pengiriman pesan yang andal.


4. Implementasi Integrasi dengan Sistem Data Lainnya:

- Menggunakan ETL (Extract, Transform, Load): Gunakan alat seperti Apache NiFi, Apache Airflow, atau AWS Glue untuk mengambil, mentransformasi, dan memuat data dari sumber data lainnya ke dalam data lake.
- API dan Integrasi Data: Gunakan API untuk mengintegrasikan data dari sistem lain, seperti basis data relasional, aplikasi bisnis, atau sistem analitik ke dalam data lake.
- Penggunaan Data Catalog: Implementasikan data catalog seperti Apache Atlas, AWS Glue Data Catalog, atau Google Cloud Data Catalog untuk mengelola metadata dan dokumentasi data dalam data lake.