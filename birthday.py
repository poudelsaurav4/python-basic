import datetime

current_date = datetime.date.today()

user_date = input("enter date you want to calculate age with (yyyy-mm-dd): ") 
userdate_real = datetime.datetime.strptime(user_date, "%Y-%m-%d").date()
# print((current_date.year-userdate_real.year))


days_birthday = (datetime.date(current_date.year, userdate_real.month, userdate_real.day) - current_date).days
if days_birthday == 0:
    print("happy birthday")
elif days_birthday > 0:
    print(f"birthday in {days_birthday} days.")
else:
    year_birthday = (datetime.date(current_date.year +1,userdate_real.month,userdate_real.day)- current_date).days
    print(f"your birthday is after {year_birthday} days")