# SOAL PRIORITAS 1
"""
1. Buatlah sebuah program untuk menghitung luas persegi panjang.
Kemudian dari hasil perhitungan luas tersebut tampilkan tulisan “even rectangle” 
jika luas merupakan bilangan genap dan tampilkan tulisan “odd rectangle” 
jika luas merupakan bilangan ganjil. Rumus perhitungan luas persegi panjang adalah sebagai berikut:
"""
p = 2
l = 5

p *= l

if p % 2 == 0:
    print("even rectangle")
else:
    print("odd rectangle")

"""
2. Buatlah sebuah program untuk menghitung volume bola. 
Volume bola dapat dihitung dengan rumus berikut:
"""
r = 21
phi = 3.14

print(4/3*phi*r**3)

"""
3. Buatlah sebuah program yang mencetak angka dari 1 sampai 100 dengan kriteria sebagai berikut:
Jika bilangan merupakan kelipatan 3 maka tampilkan hasil kuadrat dari bilangan tersebut.
Jika bilangan merupakan kelipatan 5 maka tampilkan hasil perpangkatan 3 dari bilangan tersebut.
Jika bilangan merupakan kelipatan 3 dan 5 maka tampilkan tulisan “buzz”
Jika tiga kriteria diatas tidak terpenuhi maka tampilkan bilangan aslinya.
"""
# for x in range(100):
#     if x % 3 == 0:
#         print(x**2)
#     elif x % 5 == 0:
#         print(x**3)
#     elif x % 3 == 0 and x % 5 == 0:
#         print("buzz")
#     else:
#         print(x)

class Solution(object):
    def numbers(self, n):
        result = []
        for x in range(1, n + 1):
            if x % 3 and x % 5 == 0: 
                result.append("buzz")
            elif x % 3 == 0:
                result.append(x**2)
            elif x % 5 == 0:
                result.append(x**3)
            else:
                result.append(x)  
        return result
ob1 = Solution()
print(ob1.numbers(100))

