def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i        # Mengembalikan indeks elemen yang di temukan
    return -1       # Mengembalikan -1 jika target tidak ditemukan
    
# Contoh penggunaan fungsi linear search
data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

target = 4
result = linear_search(data, target)

if result != -1:
    print(f"{target} ditemukan di indeks {result}.")
else:
    print(f"{target} tidak ditemukan dalam daftar.")