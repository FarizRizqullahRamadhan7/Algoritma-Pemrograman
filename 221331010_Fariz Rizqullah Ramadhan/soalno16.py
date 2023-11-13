def list_ke_string(daftar_kata):
    separator= ""
    for i in daftar_kata:
        separator += i + " "
        return separator
print(list_ke_string(["Python", "adalah", "menyenangkan"]))
print(list_ke_string(["satu", "dua", "tiga"])) 
