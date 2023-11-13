def hapus_duplikat(daftar):
    tanpa_duplikat = list (set(daftar))
    return tanpa_duplikat
print(hapus_duplikat([1, 2, 2, 3, 3, 3]))
print(hapus_duplikat(["apple", "banana", "apple"])) 
