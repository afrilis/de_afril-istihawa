CREATE TABLE kendaraan (
  id_kendaraan INT PRIMARY KEY,
  jenis_kendaraan VARCHAR (255),
  merek VARCHAR(255),
  nomor_polisi INT,
  tahun_pembuatan DATE,
  status_ketersediaan BOOLEAN
);

CREATE TABLE pelanggan (
  id_pelanggan INT PRIMARY KEY,
  nama VARCHAR (255),
  alamat VARCHAR (255),
  nomor_hp INT,
  no_ktp INT,
  email VARCHAR (255)
);

SELECT create_reference_table('pelanggan');

CREATE TABLE feedback_pelanggan (
  id_feedback INT PRIMARY KEY,
  id_pelanggan INT,
  isi_feedback VARCHAR (255),
  waktu TIMESTAMP
);

CREATE TABLE penghasilan_bulanan (
  id_penghasilan INT PRIMARY KEY,
  bulan DATE,
  total_keuntungan VARCHAR (255),
  biaya_operasional VARCHAR (255)
);

CREATE TABLE transaksi_penyewaan (
  id_transaksi INT PRIMARY KEY,
  id_kendaraan INT,
  id_pelanggan INT,
  waktu_sewa DATE,
  waktu_kembali DATE,
  durasi_sewa TIMESTAMP,
  biaya_sewa decimal (10, 2),
  jenis_pembayaran VARCHAR (255)
);

SELECT create_distributed_table('transaksi_penyewaan', 'waktu_sewa');
