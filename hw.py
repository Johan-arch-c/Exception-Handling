from datetime import date

def calculate_age(birthdate):
    today = date.today()
    age = today.year - birthdate.year
    if (today.month, today.day) < (birthdate.month, birthdate.day):
        age -= 1
    return age
birth_year = int(input("Enter your birth year (e.g. 2000): "))
birth_month = int(input("Enter your birth month (1-12): "))
birth_day = int(input("Enter your birth day (1-31): "))
birthdate = date(birth_year, birth_month, birth_day)
age = calculate_age(birthdate)
print(f"You are born on {age}")
