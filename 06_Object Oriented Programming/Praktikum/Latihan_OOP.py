# -------------------------------------- SOAL PRIORITAS 1 ---------------------------------------------
# 1. Desain Kelas Pelanggan:
class Pelanggan:
    def __init__(self, nama="afril", usia=19, id_pelanggan=0000):
        self.__nama = nama
        self.__usia = usia
        self.__id_pelanggan = id_pelanggan

# Implementasi metode get dan set
    def set_nama(self, x):
        self.__nama = x   
    def get_nama(self):
        return self.__nama
    
    def set_usia(self, y):
        self.__usia = y  
    def get_usia(self):
        return self.__usia
    
    def set_id_pelanggan(self, z):
        self.__id_pelanggan = z 
    def get_id_pelanggan(self):
        return self.__id_pelanggan
    
# print Data Pelanggan
tampilkanInfo = Pelanggan() 
tampilkanInfo.set_nama("Andy")
tampilkanInfo.set_usia(20)
tampilkanInfo.set_id_pelanggan(2002)

print("Berikut Info Pelanggan :")
print("Nama :",tampilkanInfo.get_nama()) 
print("Usia :",tampilkanInfo.get_usia())
print("Id   :",tampilkanInfo.get_id_pelanggan()) 
print(" ")
print("----------------------------------------")
print(" ")

# 2. Desain Kelas Pelatih :
class Pelatih:
    def __init__(self, nama="kakak", spesialisasi="no name", tahun_pengalaman=0000):
        self.__nama = nama
        self.__spesialisasi = spesialisasi
        self.__tahun_pengalaman = tahun_pengalaman
    
    def set_nama(self, x):
        self.__nama = x 
    def get_nama(self):
        return self.__nama 
    
    def set_spesialisasi(self, y):
        self.__spesialisasi = y 
    def get_spesialisasi(self):
        return self.__spesialisasi 
    
    def set_tahun_pengalaman(self, x):
        self.__tahun_pengalaman = x 
    def get_tahun_pengalaman(self):
        return self.__tahun_pengalaman

# print Data Pelatih
tampilkanInfo = Pelatih() 
tampilkanInfo.set_nama("Raka Bintang")
tampilkanInfo.set_spesialisasi("Pemula")
tampilkanInfo.set_tahun_pengalaman(4)

print("Berikut Info Pelatih :")
print("Nama             :",tampilkanInfo.get_nama())
print("Spesialisasi     :",tampilkanInfo.get_spesialisasi())
print("Tahun Pengalaman :",tampilkanInfo.get_tahun_pengalaman(), "tahun") 
print(" ")
print("----------------------------------------")
print(" ")      

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
        return super().tampilkanInfo() + " " + self.jenis_latihan + " " + self.jadwal

pelatih = Pelatih("Budi", "Publik Speaking", "5")
kelas_latihan = KelasLatihan("Budi", "Publik Speaking", "5", "Pemula", "Senin dan Rabu")

tampilkanInfo_pelatih = pelatih.tampilkanInfo()
tampilkanInfo_kelas_latihan = kelas_latihan.tampilkanInfo()

print(tampilkanInfo_pelatih)
print(tampilkanInfo_kelas_latihan)
print(" ")
print("----------------------------------------")
print(" ")

# 4. Demonstrasi
class Pelanggan:
    def __init__(self, nama, usia, id):
        self.nama = nama
        self.usia = usia
        self.id = id
    
    def tampilkanInfo(self):
        return self.nama + " " + self.usia + " " + self.id
class Pelatih:
    def __init__(self, nama, spesialis, tahun_pengalaman):
        self.nama = nama
        self.spesialis = spesialis
        self.tahun_pengalaman = tahun_pengalaman

    def tampilkanInfo(self):
        return self.nama + "\nSpesialis : " + self.spesialis + "\nTahun Pengalaman : " + self.tahun_pengalaman
    
class KelasLatihan(Pelatih):
    def __init__(self, nama, spesialisasi, tahun_pengalaman, jenis_latihan, jadwal):
        super().__init__(nama, spesialisasi, tahun_pengalaman)
        self.jenis_latihan = jenis_latihan
        self.jadwal = jadwal
    
    def tampilkanInfo(self):
        return super().tampilkanInfo() + "\nJenis Latihan : " + self.jenis_latihan + "\nJadwal : " + self.jadwal
    
pelanggan1 = Pelanggan("Yaya", "20", "0348")
pelanggan2 = Pelanggan("Zean", "19", "3728")
pelatih1 = Pelatih("Ka Seto", "Renang", "5")
pelatih2 = Pelatih("Ka Pai", "Sepak Bola", "7")
kelas_Renang = KelasLatihan("Ka Seto", "Renang", "5","Pemula", "Selasa dan Jumat")
kelas_SepBol = KelasLatihan("Budi", "Sepak Bola", "4", "Intermediate", "Senin dan Rabu")

print("Daftar Pelanggan :")
print(pelanggan1.tampilkanInfo())
print(pelanggan2.tampilkanInfo())
print(" ")
print("Daftar Pelatih :")
print(pelatih1.tampilkanInfo())
print(pelatih2.tampilkanInfo())
print(" ")
print("Informasi Kelas :")
print(kelas_Renang.tampilkanInfo())
print(" ")
print(kelas_SepBol.tampilkanInfo())
print(" ")
print("----------------------------------------")
print(" ")

# -------------------------------------- SOAL PRIORITAS 2 ---------------------------------------------

# Kelas Induk
class KelasLatihan:
    def __init__(self, nama, spesialisasi, tahun_pengalaman, jenis_latihan, jadwal):
        self.nama = nama
        self.spesialisasi = spesialisasi
        self.tahun_pengalaman = tahun_pengalaman
        self.jenis_latihan = jenis_latihan
        self.jadwal = jadwal
    
    def tampilkanInfo(self):
        return self.nama + " " + self.spesialisasi + " " + self.tahun_pengalaman + " " + self.jenis_latihan + " " + self.jadwal

# Kelas yang diwariskan
class Yoga(KelasLatihan):
    def __init__(self, nama, spesialisasi, tahun_pengalaman, jenis_latihan, jadwal, tingkatKesulitan):
        super().__init__(nama, spesialisasi, tahun_pengalaman, jenis_latihan, jadwal)
        self.tingkatKesulitan = tingkatKesulitan

    def aturPosisi(self, Yoga):
        self.posisi = Yoga
        return self.posisi
    
    def tampilkanInfo(self):
        return super().tampilkanInfo() + " " + self.tingkatKesulitan
    
class angkatBeban(KelasLatihan):
    def __init__(self, nama, spesialisasi, tahun_pengalaman, jenis_latihan, jadwal, beratMaksimum):
        super().__init__(nama, spesialisasi, tahun_pengalaman, jenis_latihan, jadwal)
        self.beratMaksimum = beratMaksimum

    def aturBeratBeban(self, Beban):
        self.beratMaksimum = Beban
        return self.beratMaksimum

    def tampilkanInfo(self):
        return super().tampilkanInfo() + " " + self.beratMaksimum + "kg"
    
kelasLatihan1 = KelasLatihan("Yolan", "Pemula", "4 th", "Kebugaran", "Senin dan kamis")
yoga1 = Yoga("Yolan", "Pemula", "4 th", "Senam", "Senin", "Mudah")   
angkatBeban1 = angkatBeban("Yolan", "Pemula", "4 th", "Tricep", "Senin dan kamis", "60")

tampilkanInfo_kelas_latihan = kelasLatihan1.tampilkanInfo()
tampilkanInfo_yoga = yoga1.tampilkanInfo()
tampilkanInfo_angkatBeban = angkatBeban1.tampilkanInfo()
atur_posisi_yoga = yoga1.aturPosisi("Lantai")
atur_berat_beban = angkatBeban1.aturBeratBeban(45)

print("Data Informasi Pusat Kebugaran: ")
print(tampilkanInfo_kelas_latihan)
print(tampilkanInfo_yoga)
print(tampilkanInfo_angkatBeban)
print(atur_posisi_yoga)
print(atur_berat_beban)
print(" ")
print("----------------------------------------")
print(" ")

# -------------------------------------- SOAL EKSPLORASI ---------------------------------------------
class KelasLatihan:
    def __init__(self, jenis_latihan, jadwal):
        self.jenis_latihan = jenis_latihan
        self.jadwal = jadwal
        self.terpesan = False

    def pesanKelas(self):
        if not self.terpesan:
            self.terpesan = True
            return f"Kelas {self.jenis_latihan} berhasil dipesan."
        elif not self.terpesan:
            self.terpesan = False
            return f"Kelas {self.jenis_latihan} belum dipesan."
        else:
            return f"Kelas {self.jenis_latihan} sudah dipesan sebelumnya."
    
    def batalkanKelas(self):
        if self.terpesan:
            self.terpesan = False
            return f"Kelas{self.jenis_latihan} berhasil dibatalkan."
    
    def tampilkanInfo(self):
        return self.jenis_latihan + " " + self.jadwal + " " + str(self.terpesan)

class Yoga(KelasLatihan):
    def __init__(self, jenis_latihan, jadwal, tingkatKesulitan):
        super().__init__(jenis_latihan, jadwal)
        self.tingkatKesulitan = tingkatKesulitan

    def aturPosisi(self, Yoga):
        self.posisi = Yoga
        return self.posisi
    
    def pesanKelas(self):
        return super().pesanKelas() 
    
    def batalkanKelas(self):
        return super().batalkanKelas()
    
    def tampilkanInfo(self):
        return super().tampilkanInfo() + " " + self.tingkatKesulitan
    
class angkatBeban(KelasLatihan):
    def __init__(self, jenis_latihan, jadwal, beratMaksimum):
        super().__init__(jenis_latihan, jadwal)
        self.beratMaksimum = beratMaksimum

    def aturBeratBeban(self, Beban):
        self.beratMaksimum = Beban
        return self.beratMaksimum
    
    def pesanKelas(self):
        return super().pesanKelas() 
    
    def batalkanKelas(self):
        return super().batalkanKelas()

    def tampilkanInfo(self):
        return super().tampilkanInfo() + " " + self.beratMaksimum + "kg"

kelasLatihan1 = KelasLatihan("Kebugaran", "Senin dan kamis")
yoga1 = Yoga("Senam", "Senin", "Mudah")   
angkatBeban1 = angkatBeban("Tricep", "Senin dan kamis", "60")

tampilkanInfo_kelas_latihan = kelasLatihan1.tampilkanInfo()
tampilkanInfo_yoga = yoga1.tampilkanInfo()
tampilkanInfo_angkatBeban = angkatBeban1.tampilkanInfo()
atur_posisi_yoga = yoga1.aturPosisi("Lantai")
atur_berat_beban = angkatBeban1.aturBeratBeban(45)
terpesan_yoga = yoga1.pesanKelas()
terpesan_angkat_beban = angkatBeban1.pesanKelas()

print("Informasi Pemesanan Kelas: ")
print(terpesan_yoga)
print(terpesan_angkat_beban)

print(" ")
print("----------------------------------------")
print(" ")
    
