def is_leap_year(year):

    if (year % 4 == 0):
        if (year % 100 == 0):
            if (year % 400 == 0):
                return True
            else:
                return False
        else:
            return False
    
    else:
        return False

print(is_leap_year(2000))
print(is_leap_year(2001))
print(is_leap_year(1999))
print(is_leap_year(1995))

