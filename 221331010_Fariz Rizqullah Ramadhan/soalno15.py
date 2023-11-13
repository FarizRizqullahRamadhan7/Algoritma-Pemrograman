def cek_kelipatan(bilangan, kelipatan):
    if bilangan %kelipatan ==0:
        return True
    else:
        return False
print(cek_kelipatan(10, 2)) # harus mencetak True
print(cek_kelipatan(10, 3)) # harus mencetak False