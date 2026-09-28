class Father:
    def property(self):
        print("Father's house")

class Son1(Father):
    def car(self):
        print("Son1 has car")

class Son2(Father):
    def bike(self):
        print("Son2 has bike")

class Daughter(Father):
    def jewellery(self):
        print("Daughter has jewellery")

s1 = Son1()
s1.property() 
s1.car()      

s2 = Son2()
s2.property() 
s2.bike()     

d = Daughter()
d.property()  
d.jewellery() 

class Animal:
    def eat(self):
        print("Eating")

class Dog(Animal):
    def bark(self):
        print("Barking")

class Cat(Animal):
    def meow(self):
        print("Meowing")

class Cow(Animal):
    def moo(self):
        print("Mooing")

dog = Dog()
dog.eat()
dog.bark()

cat = Cat()
cat.eat()
cat.meow()