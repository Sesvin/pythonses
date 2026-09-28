class Animal:
    def eat(self):
        print("Eating")

class Dog(Animal):  
    def bark(self):
        print("Barking")

class Cat(Animal):
    def meow(self):
        print("Meowing")

class Puppy(Dog, Cat): 
    def weep(self):
        print("Weeping")

p = Puppy()
p.eat()  
p.bark() 
p.meow() 
p.weep() 