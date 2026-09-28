class Father:
    def bike(self):
        print("Father's old bike")
class Son(Father):
    def bike(self): 
        print("Son's new KTM bike")
s = Son()
s.bike() 
class Father2:
    def bike(self):
        print("Father's old bike")
class Son2(Father2):
    def bike(self):
        super().bike() 
        print("Son's new KTM bike")
s2 = Son2()
s2.bike()
class Animal:
    def sound(self):
        print("Animal makes some sound")
class Dog(Animal):
    def sound(self): 
        print("Dog barks - Woof Woof!")
class Cat(Animal):
    def sound(self):
        print("Cat meows - Meow!")
d = Dog()
d.sound()
c = Cat()
c.sound() 