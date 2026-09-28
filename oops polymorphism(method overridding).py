class Calculator:
    def add(self, a, b, c=0):
        return a + b + c
calc = Calculator()
print(calc.add(2, 3))
print(calc.add(2, 3, 4)) 
class Demo:
    def add(self, *args):
        total = 0
        for num in args:
            total += num
        return total
d = Demo()
print(d.add(2, 3))       
print(d.add(2, 3, 4))    
print(d.add(1,2,3,4,5))  
class Greet:
    def show(self, name=None):
        if name:
            print(f"Hello {name}")
        else:
            print("Hello Guest")
g = Greet()
g.show()
g.show("sesvin") 