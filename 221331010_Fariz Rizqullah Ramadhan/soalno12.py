def apakah_palindrome(kata):
    panjang_kata = len(kata)
    for i in range(panjang_kata//2):
        if (kata[i] != kata[panjang_kata-i-1]):
            palindrome = False
        else:
            palindrome = True
        return palindrome
print(apakah_palindrome("kayak"))
print(apakah_palindrome("python"))

