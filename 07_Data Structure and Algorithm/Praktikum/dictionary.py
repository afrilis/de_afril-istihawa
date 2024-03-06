simple_dict = {"angka"}
print(simple_dict)

simple_dict2 = {"angka": 1, "nama": "Alterra", "status": True}
print(simple_dict2)

second_dict = dict([("angka", 3), ("nama", "Academy")])
print(second_dict)

other_dict = dict({"key": "value"})
print(other_dict)

# Mengakases dictionary
simple_dict2 = {"angka": 1, "nama": "Alterra", "status": True}
print(simple_dict2["nama"])

# Melakukan operasi pada dictionary
simple_dict2["new"] = 123
print(simple_dict2)

# cara lain, mengganti value alterra dengan academy
simple_dict2["nama"] = "Academy"
print(simple_dict2)

# adapun cara menghapus key-value, key new dengan value 123 dihapus
del simple_dict2["new"]
print(simple_dict2)
