class Student:
    def __init__(self,name,age) -> None:
        self.name = name
        self.age = age
        print("Yapıcı blok çalıştı")

    #method,davranışlarımızı
    def doHomework(self):
        print(f"{self.name} is doing homework")

    def study(self):
        print(f"{self.name} is Studying...")
