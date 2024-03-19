
# LATIHAN RELATION DATABASE

## Merancang Skema Database

1. Buatlah rancangan skema database dengan kriteria sebagai berikut:
- a. Sistem dapat menyimpan data mengenai detail item product, yaitu : product, product_type,             product_description, operator, payment_methods.
- b. Sistem juga harus menyimpan data mengenai pelanggan yang akan membeli product tsb diantaranya : nama, alamat, tanggal lahir, status_user, gender, created_at, updated_at.
- c. Sistem dapat mencatat transaksi pembelian dari pelanggan.
- d. Sistem dapat mencatat detail transaksi pembelian dari pelanggan.
Gunakan draw.io atau lucidchart untuk membuat ERD.

![](../Screenshots/Skema_Database.jpg)



## Data Definition Language (DDL)

1. Create database alta_online_shop.

2. Dari schema Olshop yang telah kamu kerjakan di, Implementasikanlah menjadi table pada MySQL.
Create table user.

![](../Screenshots/tb_user.png)

Create table product, product type, operators, product description, payment_method.

![](../Screenshots/tb_product.png)

Create table transaction, transaction detail.

![](../Screenshots/tb_transaction.png)

![](../Screenshots/tb_transaction_detail.png)


3. Create tabel kurir dengan field id, name, created_at, updated_at.

![](../Screenshots/add_tb_kurir.png)

4. Tambahkan ongkos_dasar column di tabel kurir.

![](../Screenshots/add_ongkos_dasar.png)

5. Rename tabel kurir menjadi shipping.

![](../Screenshots/rename_tabel_kurir_menjadi_shipping.png)

6. Hapus / Drop tabel shipping karena ternyata tidak dibutuhkan.

![](../Screenshots/drop_tabel_shipping.png)

7. Silahkan menambahkan entity baru dengan relation 1-to-1, 1-to-many, many-to-many. Seperti:
1-to-1: payment method description.

![](../Screenshots/payment_method_desc.png)

1-to-many: user dengan alamat.

![](../Screenshots/user_alamat.png)

many-to-many: user dengan payment method menjadi user_payment_method_detail.

![](../Screenshots/payment_method_detail.png)