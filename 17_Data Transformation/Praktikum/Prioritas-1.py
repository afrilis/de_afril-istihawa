import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Memuat data ke dalam DataFrame
house_data = pd.read_csv('house_listings.csv')

# Membersihkan kolom 'price' dari karakter non-numerik dan mengubahnya menjadi float
house_data['price'] = house_data['price'].str.replace(' ', '').astype(float)

# Membersihkan kolom 'price_1m2' dari karakter non-numerik dan mengubahnya menjadi float
house_data['price_1m2'] = house_data['price_1m2'].str.replace(' AZN/m²', '').str.replace(' ', '').astype(float)

# Normalisasi harga rumah dan harga per meter persegi menggunakan Min-Max scaling
scaler = MinMaxScaler()
house_data[['price', 'price_1m2']] = scaler.fit_transform(house_data[['price', 'price_1m2']])

# Encoding data kategorikal
house_data = pd.get_dummies(house_data, columns=['category', 'title_deed', 'repair', 'mortgage'])

# Aggregasi data
aggregated_data = house_data.groupby(['room_number', 'category_Köhnə tikili', 'category_Yeni tikili']).agg({'price': ['mean', 'median', lambda x: x.mode()[0]]})
aggregated_data.columns = ['avg_price', 'median_price', 'mode_price']

# Menyimpan hasil aggregasi ke file Excel
aggregated_data.to_excel('result_prioritas_1.xlsx')

# Menampilkan hasil aggregasi
print(aggregated_data)
