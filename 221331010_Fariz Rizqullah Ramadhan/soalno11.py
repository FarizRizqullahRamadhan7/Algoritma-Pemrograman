def kurangi_rekursif(angka):
    if angka == 1:
        return 1
    else:
        return angka+kurangi_rekursif(angka-1)
print(kurangi_rekursif(10)) # harus mencetak 55
print(kurangi_rekursif(5)) # harus mencetak 15