def hitung_genap_ganjil(daftar_angka):
    jumlah_genap = 0
    jumlah_ganjil = 0

    for angka in daftar_angka:
        if angka % 2 == 0:
            jumlah_genap += 1
        else:
            jumlah_ganjil += 1

    return (jumlah_genap, jumlah_ganjil)

print(hitung_genap_ganjil([1, 2, 3, 4, 5])) 
print(hitung_genap_ganjil([10, 20, 30])) 
