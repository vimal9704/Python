def leap_year(year):
    if year % 4 == 0:
        return True
        
    if year % 400 == 0:
        return False
        
    if year % 100 == 0:
        return True
       
    else:
        print("The year is not a leap year")

year = int(input())
print(leap_year(year))