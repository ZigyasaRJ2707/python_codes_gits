from datetime import date 

current_year = date.today().year
age = int(input("Enter your age: "))

hundredth_year = current_year + (100-age)
print("You'll be turning hundred in the year", hundredth_year, "!")