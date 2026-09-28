class Father:
    def house(self):
        print("Father has a house")
class Son(Father): 
    def car(self):
        print("Son has a car")
s = Son()
s.house() 
s.car()  