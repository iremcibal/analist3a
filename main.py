print("Merhaba Tobeto Analist Ekibi")


#degiskenler => herhangi bir veri içeren ifadedir
#string => metinsel ifadeler
text = "Merhaba, hoşgeldin "
fullName = "irem" #veritabanından bilgi alınıyor

print(text + fullName) #Anasayfa
print(text + fullName) #Profilim
print(text + fullName) #about
print(text + fullName) #contact

#int , integer => tam sayı 
studentCount = 45
print(studentCount + 5)

#double,decimal,float => ondalıklı sayılar 
averagePoint = 25.5 
print(averagePoint+ 5)

#bool,boolean => true - false 
isVerified = True
print(isVerified) 

print(type(text))
print(type(studentCount))
print(type(averagePoint))
print(type(isVerified))


#matematiksel operatörler
# + - / * %
number = 10
print(number + 10)

print(number - 5)

print(number * 2)

print(number / 2)

print(number % 3) 

#mantıksal operatörler => karşılaştırma operatörler
print(number == 10) #True
print(number == 11) #False

print(number != 10)  #false
print(number != 11)  #true

print(number >10) #false
print(number >=10 ) #true

print(number <10) #false
print(number <=10) #true

# string interpolation => metin birleştirme 

print(text + fullName) #Anasayfa
#f-string
totalText = f"Hoşgeldiniz {fullName}"
print(totalText)








