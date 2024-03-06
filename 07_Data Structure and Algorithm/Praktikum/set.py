# Ada dua cara pendeklarasian: Menggunakan kurung kurawal{} atau method set
my_set = {1, 2, 3, 4, 5}

set_2 = set(["Alterra", "Academy"])

# print(my_set)
# print(set_2)

# print(my_set[2]) # ketika diakses menggunakan indeks, set akan error

# adapun cara memanipulasi set dengan method method yang telah disediakan 
my_set.add(8)
# print(my_set)

my_set.pop()    # menghilangkan nilai pertama
print(my_set)

my_set.remove(2)    # dapat juga menggunakan remove
print(my_set)