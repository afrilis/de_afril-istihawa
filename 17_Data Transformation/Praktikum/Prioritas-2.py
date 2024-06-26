import pandas as pd

# Memuat data dari file CSV
house_data = pd.read_csv('house_listings.csv')

# Membersihkan kolom 'area' dari karakter non-numerik dan mengonversi ke tipe data float
house_data['area'] = house_data['area'].str.replace(' m²', '').astype(float)

# Membersihkan kolom 'price' dari karakter non-numerik dan mengonversi ke tipe data float
house_data['price'] = house_data['price'].str.replace(' ', '').astype(float)

# Identifikasi dan imputasi nilai yang hilang pada kolom 'area' dan 'floor'
house_data['area'].fillna(house_data['area'].median(), inplace=True)

# Mengatasi outlier pada kolom 'price' menggunakan metode IQR
Q1 = house_data['price'].quantile(0.25)
Q3 = house_data['price'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
house_data = house_data[(house_data['price'] >= lower_bound) & (house_data['price'] <= upper_bound)]

# Pilih hanya kolom-kolom yang diminta
selected_columns = ['url', 'area', 'floor', 'address', 'price']
house_data_selected = house_data[selected_columns]

# Menyimpan data yang telah diproses ke dalam file Excel
house_data_selected.to_excel('result_prioritas_2.xlsx', index=False)

# Menampilkan beberapa baris data untuk verifikasi
print(house_data_selected.head())
