def leap_years(year:int)->bool:
    if year%400==0:
        return True
    elif year%100!=0:
        if year%4==0:
            return True
    return False

def main():
    year=int(input('enter the year: '))
    if leap_years(year):
        print(f'{year} is  a leap year')
    else:
        print(f'{year} is not a  leap year')
        
main()
    