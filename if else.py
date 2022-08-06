age=int(input("enter the age"))
sex=input('enter the sex')
if age>=18 and age<30:
    if sex=="m":
        print("700 days")
    if sex=="f":
        print("750 days")
elif age>=30 and age <=4:
    if sex=="m":
        print("800 days")
    if sex=="f":
        print("850 days")
else:
    print("enter the proper one")