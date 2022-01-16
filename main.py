print("How much time left untill you reach your 90s.")
age = input("How old are you now? ")
age_as_int = int(age)
years_left = 90 - age_as_int
days_left = years_left * 365
weekes_left = years_left * 52
months_left = years_left * 12
message = f"You have {days_left} days, {weekes_left} weeks, {months_left} months."
print(message)
