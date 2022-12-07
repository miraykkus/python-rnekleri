"""palindrom sayıları toplayıp diğerlerini çıkarıp geri döndren program."""
def palindromtopla(*a):
    toplam = fark = 0
    for deger in a:
        if str(a) == str(a)[::-1]:
            toplam+=a
        else:
            fark+=a
    return toplam-fark

print(palindromtopla(10, 101,55,40,9009))

