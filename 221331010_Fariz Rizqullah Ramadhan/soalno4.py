def faktorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * faktorial(n-1)
print(faktorial(5)) # harus mencetak 120
print(faktorial(4)) # harus mencetak 24