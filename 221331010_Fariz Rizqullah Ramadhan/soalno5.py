def cari_karakter(kalimat, karakter):
    jumlah_karakter = 0
    for huruf in kalimat:
        if huruf == karakter:
            jumlah_karakter += 1
    return jumlah_karakter
print(cari_karakter("hello world","o"))
print(cari_karakter("hello world","l"))