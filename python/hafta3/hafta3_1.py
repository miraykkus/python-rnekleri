liste =[]
for i in range(0, 5):
    liste.append(eval(input()))

def sirala(a):
    return a*a-20

liste.sort(key=sirala)
print(liste)
