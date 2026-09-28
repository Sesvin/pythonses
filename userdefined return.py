def test():
    return 10
    print("This will not print")
def check(num):
    if num > 0:
        return "Positive"
    else:
        return "Negative"
print(check(5))  
def get_stats(lst):
    return max(lst), min(lst), len(lst)

numbers = [10, 20, 5, 8]
big, small, count = get_stats(numbers)
print(f"Max: {big}, Min: {small}, Count: {count}")

def greet():
    print("Hi")

result = greet()
print(result)