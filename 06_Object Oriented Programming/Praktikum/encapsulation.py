# Contoh class
class ClassRobot:
    pass 

# Instance
class Cat:
    def __init__(self, fur_color = "No Name", num_of_leg = 4):
        self._fur_color = fur_color
        self.num_of_leg = num_of_leg

manis = Cat("Hitam", 4)
pussy = Cat("Putih", 3)

# Contoh dari type artibrute
class Mobil:
    def __init__(self, tipe, name, roda, platnum):
        self.roda = roda
        self._tipe = tipe
        self.__name = name  # atribute private ditandai dengan dua garis bawah
        self.__platnum = platnum # merupakan atribute private (hak akses classnya sendiri, tidak bisa diakses oleh luar kelas maupun turunannya)

class Bebek:
    def speak(self, bunyi_suara):
        return bunyi_suara          #Nilai kembalian

# Membuat objek dari kelas Bebek 
donald = Bebek()

# Memanggil Method Speak
suara_donald = donald.speak("Kwek kwek")
print(suara_donald)        