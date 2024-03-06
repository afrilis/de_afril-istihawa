list_number = [1, 2, 3, 4, 5]
print(list_number)

list_string = ["Malang", "Surabaya", "Kediri"]
print(list_string)

list_mixed = [1, "Malang", True]
print(list_mixed)

# akses item pada list dapat menggunakan indeks positif atau negatif 
list_angka = [0, 1, 2, 3, 4]
print(list_angka[-1]) #output 4
print(list_angka[0]) #output 0

# Penerapan Method
list_number = [1, 2, 3, 4, 5]
print(len(list_number))         # untuk mengetahui banyak item

list_string = ["Malang", "Surabaya", "Kediri"]
list_string.append("Solo")      # menambahkan item
print(list_string)

list_mixed = [1, "Malang", True]
list_mixed.insert(1, False)     # menambahankan item secara spesifik, penambahan False pada indeks 1
print(list_mixed)

list_mixed.remove("Malang")     # menghapus nilai yang pertama kali ditemukan, ketika nilai malang ada 2, maka nilai ke dua tidak terhapus
print(list_mixed)

list_mixed.pop(0)       # menghapus nilai pada indeks yang di tentukan. Pada contoh berikut, dihapus nilai dari indeks 0
print(list_mixed)

# Penerapan Del Statement
list_nomor = [1, 2, 3, 4, 5, 6]

del list_nomor[2]       # akan menghapus nilai pada indeks 2 yakni 3
print(list_nomor)

#contoh lain del statement
list_nomor = [1, 2, 3, 4, 5, 6]

del list_nomor[2:]       # akan menghapus nilai pada indeks 2 sampai indeks terakhir
print(list_nomor)

#atau dapat juga menghapus seluruh item pada list/ menghapus list
list_nomor = [1, 2, 3, 4, 5, 6]
del list_nomor
print(list_nomor) # output undefined