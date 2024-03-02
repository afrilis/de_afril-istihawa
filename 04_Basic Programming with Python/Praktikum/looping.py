a = 1 
b = 6

# While
# while kondisi:
#     aksi
#     iterasi/perulangan

# while a <= b:
#     print(a)
#     a += 1

# # For
# for x in range(b):
#     print(x)

#nested loop
for x in range(b):
    while a <= b:
        print(a)
        a += 1
    print(x)
