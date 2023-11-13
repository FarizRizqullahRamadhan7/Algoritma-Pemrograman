def atas_anggaran(anggaran, *pengeluaran):
    total_pengeluaran = sum(pengeluaran)
    if total_pengeluaran > anggaran:
        return True
    else:
        return False


print(atas_anggaran(100, 20, 30, 10, 40)) 
print(atas_anggaran(100, 50, 30, 20, 10)) 