food = "bubut ayam" # bubur ayam

splitted = food.split()
print(splitted)

text = "this is text. sample text. separated by dot"
print(text.split(". "))

# join --> menggabungkan berbagai karakter yg ada disuatu list menjadi satu str utuh
characters = ["a", "f", "r", "i", "l"]

result = "".join(characters)
print(result)
result = ",".join(characters)
print(result)

# partition --> memecah string menjadi 3 bagian
address = "jl. aja dulu no. 5"
print(address.partition(". "))

url = "http://www.example.com/products/l/details.html"

endpoint, sep, doc = url.rpartition("/")
print(endpoint)
print(sep)
print(doc)

paragraph = """halo semuanya 
ini adalah sebuah tulisan 
dengan baris baru 
ggwp"""

print(paragraph)
print(paragraph.splitlines(True))

# check if string is a number / digit
number = "123"
number2 ="A20"

print(number.isdigit())
print(number2.isdigit())

#check if string is contains alphanumeric only
#alphanumeric --> hanya terdiri dari angka dan huruf tanpa spasi, titik atau tandabaca lainnya
code = "C0012345"
code2 ="f 9803"

print(code.isalnum())
print(code2.isalnum())

#in Windows
# file_path = "D:\\folder\\sample.csv"
# print(file_path())

file_path = r"D:\folder\sample.cvs"     # lebih efektif menggunakan cara ini daripada \\
print(file_path)

