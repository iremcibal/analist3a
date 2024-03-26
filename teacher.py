class Teacher:
    def __init__(self,name,lesson) -> None:
        self.name = name
        self.lesson = lesson
        print("Yapıcı blok çalıştı")

    #method,davranışlarımızı
    def teach(self):
        print(f"{self.name} is teaching")

    def rest(self):
        print(f"{self.name} is resting...")