year=int(input("enter the year"))
month=int(input("enter the month"))
date=int(input("enter the date"))
if month>=1 and month<=12:
    if date>=1 and date<=31:
        print("the nest date is",year,"-",month,"-",date+1)