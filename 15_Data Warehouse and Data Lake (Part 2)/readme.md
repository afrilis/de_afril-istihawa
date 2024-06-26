# Resume Data Warehouse and Data Lake part 2

Replikasi dan Sharding adalah dua teknik penting dalam mengelola data dalam skala besar Replikasi menduplikasi data ke beberapa node untuk meningkatkan ketersediaan dan ketahanan. Sharding membagi data menjadi beberapa partisi yang disimpan di node berbeda untuk meningkatkan kinerja dan skalabilitas.

Citus adalah sebuah extension open-source untuk PostgreSQL yang memungkinkan replikasi dan sharding data secara horizontal. Citus memungkinkan Anda untuk menskalakan database Anda secara horizontal dengan menambahkan lebih banyak node ke cluster Anda.

Skema based sharding adalah metode sharding di mana data dipartisi berdasarkan skema database. Skema based sharding memungkinkan Anda untuk mengontrol bagaimana data Anda didistribusikan di cluster Anda.

BigQuery adalah data warehouse serverless yang memungkinkan Anda untuk menganalisis data dalam skala besar. BigQuery dapat digunakan untuk menganalisis data yang disimpan di Google Cloud Storage.

Google Cloud Storage adalah layanan penyimpanan objek yang memungkinkan Anda untuk menyimpan data dalam skala besar. Google Cloud Storage dapat digunakan untuk menyimpan data yang direplikasi dan di-shard dengan Citus.