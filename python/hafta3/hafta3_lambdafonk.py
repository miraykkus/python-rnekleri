lambda_fonsiyonu = lambda a: a+10

print(lambda_fonsiyonu(5)) #doğrudan bir fonksiyon bir değişkene atanmış oluyo. return ile falan uğraştırmıyo


topla = lambda b, c: b+c
print(topla(3, 6))


def fonk(n):
    return lambda x: x * n

kat_al = fonk(2)
print(kat_al(5))

kat_al = fonk(5)
print(kat_al(5))
#sınavda sorar
