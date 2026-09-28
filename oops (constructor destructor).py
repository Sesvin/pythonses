# 1. Default Constructor - argument illa
class Demo1:
    def __init__(self):
        print("Default constructor")
d1 =Demo1()
class Demo2:
    def __init__(self, name, age):
        self.name = name
        self.age = age
d2 = Demo2("ses", 21)
print(d2.name) 
class Demo3:
    def __init__(self, name="Guest"):
        self.name = name
d3 = Demo3()      
d4 = Demo3("ses") 
print(d3.name) 
print(d4.name) 