#import koyup klasördeki diğer dosyayı yazıp çağırabilirsin
class sinif:
    metin = ""
    def __init__(self, a):
        self.metin = a
    def __del__(self):
        print("beni siliyorlar")

    def __str__(self):
        return "yazdirilan"+self.metin

nesne = sinif("civa")
print(nesne.metin)
print(nesne)#nesneyi yazdırırsan str fonk. çalışır

