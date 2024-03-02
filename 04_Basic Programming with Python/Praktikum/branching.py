a = True
b = False

angka1 = 8
angka2 = 3

if angka1 < angka2:
    print(a)

if b:
    print("kondisi terpenuhi")
else:
    print("kondisi tidak terpenuhi/default")

# if angka2 > angka1:
#     print(1)
# elif angka1 == angka2:
#     print(2)
# else:
#     print(-1)

# if kondisi:
#     aksi
# else:
#     aksi

# if kondisi1:
#     aksi1
# elif kondisi2:
#     aksi
# else:
#     aksi
    
if angka2 > angka1:
    if a == True:
        print("nested condition") #kondisi dalam kondisi
elif angka1 == angka2:
    print(2)
else:
    print(-1)