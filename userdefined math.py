import math

print(math.sqrt(25))
print(math.pow(2, 3))
print(math.ceil(4.2))     
print(math.floor(4.9))    
print(math.factorial(5))  
print(math.fabs(-10))

print(math.pi) 
print(math.e)
def find_circle_area(radius):
    return math.pi * radius * radius
print(find_circle_area(7))
def is_prime_math(n):
    # sqrt varaikkum check pannale pothum
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
print(is_prime_math(17)) 
def solve_quadratic(a, b, c):
    d = b*b - 4*a*c
    if d < 0:
        return "No real roots"
    r1 = (-b + math.sqrt(d)) / (2*a)
    r2 = (-b - math.sqrt(d)) / (2*a)
    return r1, r2
print(solve_quadratic(1, -3, 2))
def math_stats(lst):
    return {
        "max": max(lst),
        "min": min(lst),
        "sqrt_max": math.sqrt(max(lst)),
        "factorial_min": math.factorial(min(lst)) if min(lst) >=0 else "Can't"
    }
print(math_stats([3, 5, 2]))