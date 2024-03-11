# ------------------------ SOAL PRIORITAS 1 ------------------------------
# NO 1
def group_numbers(numbers, target):
    # TODO : implement your solution here
    true = []
    false = []

    for i in range(len(numbers)):
        if numbers[i] % target==0:
            true.append(numbers[i])
        else:
            false.append(numbers[i]) 
    return true+false

print(group_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))    #[[3, 6, 9], [1, 2, 4, 5, 7, 8]]
print(group_numbers([23, 15, 19, 20, 75, 30, 45], 5))   #[[15, 20, 75, 30, 45], [23, 19]]


# NO 2
def get_breads(flour_stock, breads):
    # TODO: implement your solution here
    available_breads = []
    for bread in breads:
        if bread["flour"] <= flour_stock:
            available_breads.append(bread["name"])
    return available_breads

def main():
    
    flour_stock_1 = 100 
    bread1 = [
        {"name": "donut", "flour": 25},
        {"name": "mini puff", "flour": 15},
        {"name": "baguette", "flour": 75},
        {"name": "cupcake", "flour": 15}
    ]

    bread2 = [
        {"name": "pancake", "flour": 15},
        {"name": "waffle", "flour": 25},
        {"name": "bagel", "flour": 15},
        {"name": "cupcake", "flour": 15},
        {"name": "choco chips", "flour": 10},
        {"name": "mini puff", "flour": 5},
        {"name": "bread", "flour": 30},
    ]

    available_bread1 = get_breads(flour_stock_1, bread1)
    print("Jenis roti yang dapat dibuat:")
    print(available_bread1)

    # case 2
    flour_stock_2 = 75 
    bread2 = [
        {"name": "pancake", "flour": 15},
        {"name": "waffle", "flour": 25},
        {"name": "bagel", "flour": 15},
        {"name": "cupcake", "flour": 15},
        {"name": "choco chips", "flour": 10},
        {"name": "mini puff", "flour": 5},
        {"name": "bread", "flour": 30}
    ]
    available_bread2 = get_breads(flour_stock_2, bread2)
    print("\nJenis roti yang dapat dibuat:")
    print(available_bread2)

if __name__ == "__main__":
    main()

print("\n-------------------------------------")

# ------------------------ SOAL PRIORITAS 2 ------------------------------
# NO 1
def collect_chars(word, rooms):
    if rooms <= 0:
        return "Ruangan tidak mencukupi"
    repeat = rooms // len(word)
    remainder = rooms % len(word)
    sequence = word * repeat + word[:remainder]
    return sequence

def main():
    # Test Case 1
    print("Test Case 1:")
    word_1 = "alta"
    rooms_1 = 10
    sequence_1 = collect_chars(word_1, rooms_1)
    print("Output:", sequence_1)

    # Test Case 2
    print("\nTest Case 2:")
    word_2 = "sepulsa"
    rooms_2 = 20
    sequence_2 = collect_chars(word_2, rooms_2)
    print("Output:", sequence_2)

if __name__ == "__main__":
    main()

print("\n-------------------------------------")

# NO 2
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def generate_prime_sum(height, width, start):
    matrix = []
    prime_sum = 0

    for i in range(height):
        row = []
        for j in range(width):
            while True:
                if is_prime(start):
                    prime_sum += start
                    row.append(start)
                    break
                start += 1
        matrix.append(row)

    return matrix, prime_sum

def main():
    print("Test Case 1:")
    height_1 = 1
    width_1 = 3
    start_1 = 13
    matrix_1, prime_sum_1 = generate_prime_sum(height_1, width_1, start_1)
    print("Segiempat berisi bilangan prima:")
    for row in matrix_1:
        print(row)
    print("Jumlah seluruh bilangan prima:", prime_sum_1)

    # Test Case 2
    print("\nTest Case 2:")
    height_2 = 5
    width_2 = 2
    start_2 = 1
    matrix_2, prime_sum_2 = generate_prime_sum(height_2, width_2, start_2)
    print("Segiempat berisi bilangan prima:")
    for row in matrix_2:
        print(row)
    print("Jumlah seluruh bilangan prima:", prime_sum_2)

if __name__ == "__main__":
    main()

# ------------------------ SOAL EKSPLORASI ------------------------------
import uuid

class Pengeluaran:
    def __init__(self):
        self.data_pengeluaran = {}

    def tambah_pengeluaran(self, nama_item, jumlah):
        id_pengeluaran = str(uuid.uuid4())
        self.data_pengeluaran[id_pengeluaran] = {"nama_item": nama_item, "jumlah": jumlah}
        print("Data pengeluaran berhasil ditambahkan.")

    def lihat_pengeluaran(self):
        if not self.data_pengeluaran:
            print("Belum ada data pengeluaran.")
        else:
            print("Data Pengeluaran:")
            total_pengeluaran = 0
            for id_pengeluaran, data in self.data_pengeluaran.items():
                print(f"ID: {id_pengeluaran}, Nama Item: {data['nama_item']}, Jumlah: {data['jumlah']}")
                total_pengeluaran += data['jumlah']
            print(f"Total Pengeluaran: {total_pengeluaran}")

    def ubah_pengeluaran(self, id_pengeluaran, nama_item, jumlah):
        if id_pengeluaran in self.data_pengeluaran:
            self.data_pengeluaran[id_pengeluaran] = {"nama_item": nama_item, "jumlah": jumlah}
            print("Data pengeluaran berhasil diubah.")
        else:
            print("ID pengeluaran tidak ditemukan.")

    def hapus_pengeluaran(self, id_pengeluaran):
        if id_pengeluaran in self.data_pengeluaran:
            del self.data_pengeluaran[id_pengeluaran]
            print("Data pengeluaran berhasil dihapus.")
        else:
            print("ID pengeluaran tidak ditemukan.")

def main():
    pengeluaran_manager = Pengeluaran()

    while True:
        print("\nMenu:")
        print("1. Tambah Pengeluaran")
        print("2. Lihat Pengeluaran")
        print("3. Ubah Pengeluaran")
        print("4. Hapus Pengeluaran")
        print("5. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == '1':
            nama_item = input("Masukkan nama item pengeluaran: ")
            jumlah = float(input("Masukkan jumlah pengeluaran: "))
            pengeluaran_manager.tambah_pengeluaran(nama_item, jumlah)
        elif pilihan == '2':
            pengeluaran_manager.lihat_pengeluaran()
        elif pilihan == '3':
            id_pengeluaran = input("Masukkan ID pengeluaran yang ingin diubah: ")
            nama_item = input("Masukkan nama item baru: ")
            jumlah = float(input("Masukkan jumlah baru: "))
            pengeluaran_manager.ubah_pengeluaran(id_pengeluaran, nama_item, jumlah)
        elif pilihan == '4':
            id_pengeluaran = input("Masukkan ID pengeluaran yang ingin dihapus: ")
            pengeluaran_manager.hapus_pengeluaran(id_pengeluaran)
        elif pilihan == '5':
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()


