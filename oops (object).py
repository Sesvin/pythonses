class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
s1 = Student("sesvin", 21)
s2 = Student("abisha", 20)
s3 = Student("Poojaa", 19)
print(s1.name, s1.age) 
print(s2.name, s2.age) 
students = []
students.append(s1)
students.append(s2)
students.append(s3)
for s in students:
    print(s.name)