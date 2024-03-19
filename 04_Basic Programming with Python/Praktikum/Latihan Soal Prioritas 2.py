# PRIORITAS 2 NO 1

def hitung_tarif_pengiriman(berat, jarak):
    # Menentukan tarif berdasarkan berat
    if berat >= 1 and berat <= 20:
        tarif_berat = 10000
    elif berat >= 21 and berat <= 30:
        tarif_berat = 15000
    elif berat >= 31 and berat <= 60:
        tarif_berat = 20000
    else:
        tarif_berat = 45000
    
    # Menentukan tarif berdasarkan jarak
    if jarak >= 1 and jarak <= 5:
        tarif_jarak = 2000
    elif jarak >= 6 and jarak <= 15:
        tarif_jarak = 5000
    elif jarak >= 16 and jarak <= 30:
        tarif_jarak = 10000
    else:
        tarif_jarak = 15000
    
    # Menghitung tarif keseluruhan
    tarif_keseluruhan = tarif_berat + tarif_jarak
    
    return tarif_keseluruhan

# Contoh penggunaan program
berat = int(input("Masukkan berat paket: "))
jarak = int(input("Masukkan jarak yang ditempuh: "))

tarif = hitung_tarif_pengiriman(berat, jarak)
print("Tarif pengiriman:", tarif)



#------------------- NO 2 ---------------------

def hitung_skor_budget(budget):
    if budget >= 0 and budget <= 50:
        return 4
    elif budget >= 51 and budget <= 80:
        return 3
    elif budget >= 81 and budget <= 100:
        return 2
    else:
        return 1

def hitung_skor_waktu(waktu):
    if waktu >= 0 and waktu <= 20:
        return 10
    elif waktu >= 21 and waktu <= 30:
        return 5
    elif waktu >= 31 and waktu <= 50:
        return 2
    else:
        return 1

def hitung_skor_kesulitan(kesulitan):
    if kesulitan >= 0 and kesulitan <= 3:
        return 10
    elif kesulitan >= 4 and kesulitan <= 6:
        return 5
    elif kesulitan >= 8 and kesulitan <= 10:
        return 1
    else:
        return 0

def tentukan_prioritas(budget, waktu, kesulitan):
    skor_budget = hitung_skor_budget(budget)
    skor_waktu = hitung_skor_waktu(waktu)
    skor_kesulitan = hitung_skor_kesulitan(kesulitan)

    skor_total = skor_budget + skor_waktu + skor_kesulitan

    if skor_total >= 17 and skor_total <= 24:
        return "High"
    elif skor_total >= 10 and skor_total <= 16:
        return "Medium"
    elif skor_total >= 3 and skor_total <= 9:
        return "Low"
    else:
        return "Impossible"

# Contoh penggunaan program
budget = int(input("Masukkan budget proyek: "))
waktu = int(input("Masukkan waktu pengerjaan proyek: "))
kesulitan = int(input("Masukkan tingkat kesulitan proyek: "))

prioritas = tentukan_prioritas(budget, waktu, kesulitan)
print("Prioritas proyek:", prioritas)
