class GrandFather:
    def house(self):
        print("GrandFather's house")
class Father(GrandFather):
    def car(self):
        print("Father's car")
class Son(Father):
    def bike(self):
        print("Son's bike")
s = Son()
s.house() 
s.car()   
s.bike()  
class A:
    def __init__(self):
        print("A constructor")
class B(A):
    def __init__(self):
        super().__init__()
        print("B constructor")
class C(B):
    def __init__(self):
        super().__init__()
        print("C constructor")
obj = C()