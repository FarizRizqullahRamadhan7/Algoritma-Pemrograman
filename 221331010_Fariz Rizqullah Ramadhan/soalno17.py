def hapus_duplikat(daftar):
    daftar_hapus= set(daftar)
    daftar_baru= list(daftar_hapus)
    return daftar_baru
print(hapus_duplikat([1, 2, 2, 3, 3, 3])) # harus mencetak [1, 2, 3]
print(hapus_duplikat(["apple", "banana", "apple"])) # harus mencetak ["apple", "banana"]