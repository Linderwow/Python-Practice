how_many_years=input("What is your current age?")
yearsleft=90-int(how_many_years)
days = int(yearsleft)*365
weeks=int(yearsleft)*52
months=int(yearsleft)*12
print(f"{days} days, {weeks} weeks, {months} months left")