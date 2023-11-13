def konversi_suhu(dari, ke, suhu):
    if dari == "C" and ke == "F":
        return suhu * 9/5 + 32
    elif dari == "F" and ke == "C":
        return (suhu - 32) * 5/9
    else:
        return "Kode yang dimasukkan tidak valid"
    
print(konversi_suhu("C", "F", 0)) # harus mencetak 32
print(konversi_suhu("F", "C", 32)) # harus mencetak 0