class sinif:
    a=0
    b="dfgh"
    c=[1, 2, 3]

    def yazdir(self): #self kullanma zorunlu. selfin yanına parametre koyabilirsin.
        d=105
        print(d, self.a)

nesne=sinif()
print(type(nesne))
print(nesne.a)
nesne.a=100
print(nesne.a)
nesne.yazdir()