a = 2
b = 3
c = 6
if a > b:
    print("a b den büyük")

if c < 0:
    print("c sıfırdan küççük")


#elif

if a > b:
    print("a bden büyük")
elif a==2:
    print("a=2")
else:
    print("a bden küçük")


#short if

print("a ile b farklı") if a != b else print("a ile b aynı")
