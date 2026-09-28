def clean_name(name):
    return str(name).strip().capitalize()
print(clean_name("  ravi  ")) 
def count_vowels(text):
    text = str(text).lower()
    count = 0
    for ch in text:
        if ch in "aeiou":
            count += 1
    return count
print(count_vowels("Hello World")) 
def reverse_string(s):
    return str(s)[::-1]
print(reverse_string("Python")) 