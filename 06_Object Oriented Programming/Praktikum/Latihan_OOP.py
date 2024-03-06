# 1. Desain Kelas Pelanggan:
class Pelanggan:
    def __init__(self, nama, usia, id_pelanggan):
        self.__nama = nama
        self.__usia = usia
        self.__id_pelanggan = id_pelanggan

# Implementasi metode get dan set
    def get_nama(self):
        return self.__nama
    
    def get_usia(self):
        return self.__usia
    
    def get_id_pelanggan(self):
        return self.__id_pelanggan
    
tampilkanInfo = Pelanggan("Dina", 21, 91280) 
print(tampilkanInfo.get_nama()) 
print(tampilkanInfo.get_usia())
print(tampilkanInfo.get_id_pelanggan()) 


# 2. Desain Kelas Pelatih :
class Pelatih:
    def __init__(self, nama, spesialisasi, tahun_pengalaman):
        self.__nama = nama
        self.__spesialisasi = spesialisasi
        self.__tahun_pengalaman = tahun_pengalaman
    
    def get_nama(self):
        return self.__nama 
    def get_spesialisasi(self):
        return self.__spesialisasi 
    def get_tahun_pengalaman(self):
        return self.__tahun_pengalaman
        
tampilkanInfo = Pelatih("Yuna", "Public Speaking", 4)
print(tampilkanInfo.get_nama())
print(tampilkanInfo.get_spesialisasi())
print(tampilkanInfo.get_tahun_pengalaman())


# 3. Desain Kelas KelasLatihan
# Class Induk 
class Pelatih:
    def __init__(self, nama, spesialisasi, tahun_pengalaman):
        self.nama = nama
        self.spesialisasi = spesialisasi
        self.tahun_pengalaman = tahun_pengalaman
    
    def tampilkanInfo(self):
        return self.nama + " " + self.spesialisasi + " " + self.tahun_pengalaman
        
# Class yang diwarisi
class KelasLatihan(Pelatih):
    def __init__(self, nama, spesialisasi, tahun_pengalaman, jenis_latihan, jadwal):
        super().__init__(nama, spesialisasi, tahun_pengalaman)
        self.jenis_latihan = jenis_latihan
        self.jadwal = jadwal
    
    def tampilkanInfo(self):
        return super().tampilkanInfo() + " " + str(self.jenis_latihan) + " " + str(self.jadwal)

pelatih = Pelatih("Budi", "Publik Speaking", "5")
kelas_latihan = KelasLatihan("Budi", "Publik Speaking", "5", "Pemula", "Senin dan Rabu")

tampilkanInfo_pelatih = pelatih.tampilkanInfo()
print(tampilkanInfo_pelatih)

tampilkanInfo_kelas_latihan = kelas_latihan.tampilkanInfo()
print(tampilkanInfo_kelas_latihan)


# 4. Demonstrasi

