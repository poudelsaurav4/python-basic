year = int(input("enter a year to check"))

if year % 4 == 0:
    if year%100 == 0:
        if year%400 == 0:
            print(f"{year} is a leap year")
        
        else:
            print(year," not a leap")
    else:
        print(year , "year is leap")

else:
    print(year,"is not a leap year")