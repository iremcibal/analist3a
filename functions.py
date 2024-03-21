#definition => Tanımlama
def ortalamaHesapla():
    vize = 87
    final = 45
    ortalama = (vize * 0.4) + (final * 0.6)
    print(ortalama)


def ortalamaHesapla2():
    vize = 87
    final = 75
    ortalama = (vize * 0.4) + (final * 0.6)
    return ortalama #fonk çağırıldığı yere değer götürür

ortalamaHesapla()
print(ortalamaHesapla2())


def ortalamaHesapla3(vize:float,final:float) -> float:
    return (vize * 0.4) + (final * 0.6)

print(ortalamaHesapla3(78,98))


exam1 = int(input("Vize notunuzu giriniz: "))
exam2 = int(input("Final notunuzu giriniz: "))
def ortalamaHesapla4(vize:float,final:float) -> float:
    return (vize * 0.4) + (final * 0.6)

print(ortalamaHesapla4(exam1,exam2))
   