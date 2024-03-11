def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Menentukan titik tengah daftar

        # Membagi daftar menjadi dua bagian
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Memanggil merge_sort untuk kedua bagian
        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        # Menggabungkan dua bagian menjadi satu daftar yang sudah diurutkan
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


# Contoh penggunaan merge sort
data = [38, 27, 43, 3, 9, 82, 10]

print("Data sebelum diurutkan:", data)
merge_sort(data)
print("Data setelah diurutkan:", data)

