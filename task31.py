class Employee:
    def __init__(self):
        self.name = input("Enter Name: ")
        self.age = int(input("Enter Age: "))
        self.salary = float(input("Enter Salary: "))
        self.emp_type = input("Enter Type of employee ('p' for permanent, 'c' for contract): ").lower()


class Permanent(Employee):
    def details(self):
        if self.emp_type == 'p':
            bonus_per = float(input("Enter bonus percentage: "))
            bonus_amount = self.salary * bonus_per / 100
            total_salary = self.salary + bonus_amount
            
            print("\n--- Permanent Employee Details ---")
            print(f"Name: {self.name}")
            print(f"Age: {self.age}")
            print(f"Salary: {self.salary}")
            print(f"Bonus: {bonus_amount}")
            print(f"Total Salary (Salary + Bonus): {total_salary}")
        else:
            print("This is not a Permanent Employee!")


class Contract(Employee):
    def details(self):
        if self.emp_type == 'c':
            duration = int(input("Enter contract duration (in months): "))
            
            print("\n--- Contract Employee Details ---")
            print(f"Name: {self.name}")
            print(f"Age: {self.age}")
            print(f"Salary: {self.salary}")
            print(f"Contract Duration: {duration} months")
        else:
            print("This is not a Contract Employee!")

print("Enter Details for Permanent Employee:")
p1 = Permanent()
p1.details()

print("\nEnter Details for Contract Employee:")
c1 = Contract()
c1.details()