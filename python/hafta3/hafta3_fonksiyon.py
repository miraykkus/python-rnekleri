def yazdir():
    print("yazdim")
yazdir()


def topla(a, b):
    return a+b

print(topla(3, 5))


#iki değer döndürme

def topla_carp(a, b):
    return a+b, a*b

print(topla_carp(3, 5))

toplam, carpım = topla_carp(3,5)
print(toplam, carpım)