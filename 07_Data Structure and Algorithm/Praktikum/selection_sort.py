def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i   # Indeks elemen terkecil saat ini
        
        # Mencari elemen terkecil dalam sisa daftar
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        # Menukar elemen terkecil dengan elemen ke-i
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Contoh penggunaan selection sort
data = [64, 25, 12, 22, 11]

print("Data sebelum diurutkan:", data)
selection_sort(data)
print("Data setelah diurutkan:", data)