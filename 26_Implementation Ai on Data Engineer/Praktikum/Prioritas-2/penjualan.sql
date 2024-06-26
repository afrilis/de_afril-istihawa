CREATE TABLE Penjualan (
    id_transaksi INT PRIMARY KEY,
    tanggal_transaksi DATE,
    jumlah_penjualan INT,
    harga DECIMAL(10, 2),
    kategori_produk VARCHAR(50)
);

SELECT DATE_FORMAT(tanggal_transaksi, '%Y-%m') AS bulan, kategori_produk, SUM(jumlah_penjualan) AS total_penjualan
FROM Penjualan
GROUP BY DATE_FORMAT(tanggal_transaksi, '%Y-%m'), kategori_produk;
