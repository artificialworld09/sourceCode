from datetime import date
dob = date(1992, 12, 30)
today = date.today()
age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))

print(age)
