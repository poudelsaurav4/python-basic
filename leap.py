def leap_year(year):

    if year % 4 == 0 and year%100 != 0 or year % 400 == 0:
        # if year%100 == 0:
        #     if year%400 == 0:
        #         print(f"{year} is a leap year")
            
        #     else:
        #         print(year," not a leap")
        # else:
        #     print(year , "year is leap")

        print(year, "leap year")

    else:
        print(year,"is not a leap year")


leap_year(3123)