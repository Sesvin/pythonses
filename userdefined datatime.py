from datetime import datetime, date, timedelta
import datetime as dt
def get_now():
    return datetime.now()
print(get_now())
def find_age(birth_year):
    current_year = date.today().year
    return current_year - birth_year

print(find_age(2005)) 
def calculate_age(dob):
    # dob format: "2005-05-10"
    birth_date = datetime.strptime(dob, "%Y-%m-%d").date()
    today = date.today()
    age = today.year - birth_date.year
    return age
print(calculate_age("2005-08-15"))
def greet_by_time():
    hour = datetime.now().hour
    if hour < 12:
        return "Good Morning!"
    elif hour < 18:
        return "Good Afternoon!"
    else:
        return "Good Evening!"
print(greet_by_time())
def days_until(target_date):
    # target_date format: "2026-12-31"
    target = datetime.strptime(target_date, "%Y-%m-%d").date()
    today = date.today()
    remaining = target - today
    return remaining.days
print(f"Days left: {days_until('2026-12-31')}")
def add_days_to_today(days):
    today = date.today()
    future = today + timedelta(days=days)
    return future
print(add_days_to_today(10)) 