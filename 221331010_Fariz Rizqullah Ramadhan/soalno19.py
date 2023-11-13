def jumlahkan_prima(n):
    if n<2:
        return 0
    else:
        # Menginisialisasi variabel jumlah_prima untuk diisi penjumlahan bilangan prima
        jumlah_prima = 0
        # perulangan pengecekan pada bilangan dari 2 ke n+1
        for angka in range(2, n + 1):
            # Untuk mengecek bilangan angka merupakan bilangan prima atau bukan
            if angka > 1:
                for i in range(2, angka):
                    if (angka % i) == 0:
                        break
            else:
                    # If prime, add it to the sum
                    jumlah_prima += angka

        return jumlah_prima
print(jumlahkan_prima(10)) # harus mencetak jumlah dari semua bilangan prima hingga 10
print(jumlahkan_prima(20)) # harus mencetak jumlah dari semua bilangan prima hingga 20