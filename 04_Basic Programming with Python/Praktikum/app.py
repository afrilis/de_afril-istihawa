# name = "alterra"

# print(name)
# print(name[0])
# print(name[0:3])

#formating
# number= 15.678

# print(f"{number:.2f}")
# print(f"{16:d}") #notasi d kecil menandakan 16 bilangan int
# print(f"{78:c} {66:c}") #representasi dari bentuk karakter

# name = "afril"
# favorite_drink ="milk"

# #using +
# print("hello, my name is " + name +" and my favorite drink is " + favorite_drink)

# #using f""
# print (f"hello, my name is {name} and my favorite drink is {favorite_drink}")

#pengulangan string
# symbol = "[]"
# symbol *= 10
# print(symbol)

# strip method --> menghapus white space
sentence = "\n\n      hello from python       \t\t"
result = sentence.strip()
print(result)
print(sentence.rstrip())
print(sentence.lstrip())