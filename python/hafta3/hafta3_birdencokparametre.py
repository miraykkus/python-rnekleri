def topla_ne_varsa(*a):
    toplam = 0
    for deger in a:
        toplam += deger
    return toplam

print(topla_ne_varsa(3, 5, 7, 8))