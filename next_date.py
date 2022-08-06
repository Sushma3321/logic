year=int(input("enter the year:"))
date=int(input("enter the date:"))
month=int(input("enter the month:"))
if year>0 :
    if month>=1 and month<=12:
        if date>=1 and date<31:
            print(date+1,"-",month,"-",year)
        else:
            print("1","-","1","-",year+1)
    else:
        print("there are only 12 months")
else:
    print("enter proper year")
        
        
    
    