def counting_sort(arr):
    # Menemukan nilai maksimum dalam daftar untuk menetukan rentang (range)
    max_value = max(arr)

    # Membuat array kosong untuk menghitung frekuensi masing-masing elemen
    count = [0] * (max_value + 1)

    # Menghitung frekuensi masing-masing elemen dalam daftar
    for num in arr:
        count[num] += 1

    # Membangun daftar hasil yang sudah diurutkan
    sorted_list = []
    for i in range(max_value + 1):
        print(i)
        while count[i] > 0:
            sorted_list.append(i)
            print(i)
            count[i] -= 1

    return sorted_list

# Contoh penggunaan counting sort
data = [4, 2, 2, 8, 3, 3, 1]

print("Data sebelum diurutkan:", data)
sorted_data = counting_sort(data)
print("Data setelah diurutkan:", sorted_data)