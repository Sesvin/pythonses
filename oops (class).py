class Student:
    def __init__(self, name):
        self.name = name
    def say_hello(self):
        print(f"Hi, I'm {self.name}")
s = Student("sesvin")
s.say_hello() 