class Father:
    def father_property(self):
        print("Father's house")
class Mother:
    def mother_property(self):
        print("Mother's jewellery")
class Son(Father, Mother):
    def my_property(self):
        print("Son's car")
s = Son()
s.father_property() 
s.mother_property() 
s.my_property()     

class A:
    def __init__(self):
        self.a = "Class A"
class B:
    def __init__(self):
        self.b = "Class B"
class C(A, B):
    def __init__(self):
        A.__init__(self)
        B.__init__(self)
        self.c = "Class C"
obj = C()
print(obj.a)
print(obj.b) 
print(obj.c) 