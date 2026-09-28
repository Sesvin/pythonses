def create_list():
    lst = []
    n = int(input("How many numbers? "))
    for i in range(n):
        num = int(input(f"Enter {i+1}: "))
        lst.append(num)
    return lst

def show_stats(lst):
    print(f"List: {lst}")
    print(f"Length: {len(lst)}")
    print(f"Max: {max(lst)}")
    print(f"Min: {min(lst)}")
    print(f"Count of first element {lst[0]}: {lst.count(lst[0])}")
my_list = create_list()
show_stats(my_list)