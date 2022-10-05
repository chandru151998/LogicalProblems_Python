def leap_year(year):
    '''
    leap_year
    :param year:
    :return:
    '''
    if (year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)):
        print(year,"is a leap year")
    else:
        print(year,"is not a leap year")

if __name__ == '__main__':
    year = int(input("Enter a year: "))
    leap_year(year)