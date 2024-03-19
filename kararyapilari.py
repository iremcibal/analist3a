ortalamaNot = int(input("Lütfen ortalamanizi giriniz: "))
#print(type(ortalamaNot))

if ortalamaNot >80:
    print("Bravo")
elif ortalamaNot >50:
    print("Başarılı")
    if ortalamaNot >40:
        print("Normal")
else:
    print("Dersten Kaldınız")

print("if-else bloğu içerisinde miyim?")


