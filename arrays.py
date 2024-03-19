sayilar = [100,200,300,400,"Merhaba"]

print(sayilar)
print(sayilar[0]) #programcı saymaya 0dan başlar 

sayilar.append(500) #listenin sonuna eleman ekler
sayilar.append(200)
print(sayilar)

sayilar.remove(200) #değere göre silme işlemi 
print(sayilar)

sayilar.pop() #default son index => indexe göre eleman siler
print(sayilar)

sayilar.extend([700,800])
print(sayilar)

sayilar.clear() #=> dizinin içindeki tüm elemanları sil diyorum
print(sayilar)
