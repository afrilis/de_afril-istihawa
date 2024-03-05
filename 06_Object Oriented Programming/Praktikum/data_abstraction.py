class AkunBank:
    def __init__(self, nama, saldo_awal):
        self.__nama = nama
        self.__saldo = saldo_awal

    # Metode Getter
    def get_nama(self):
        return self.__nama 
    
    def get_saldo(self):
        return self.__saldo
    
    def setor(self, jumlah):
        self.__saldo += jumlah  # artinya saldo akan bertambah seiring ketika digunakan metode setor
        return self.__saldo

    # Metode Setter
    def tarik(self, jumlah):
        if jumlah > self.__saldo:
            print("Saldo anda tidak cukup")
            return
        self.__saldo -= jumlah
        return self.__saldo
    
akun = AkunBank("Alterra", 2000)
print(akun.get_nama())
print(akun.get_saldo())
akun.setor(1000)
print(akun.get_saldo())
akun.tarik(4000)
akun.tarik(500)
print(akun.get_saldo())