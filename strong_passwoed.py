password=input("enter the password")
if len(password)>=6:
    if "@"  in password or "#"  in password :
        
        if "1"  in password or "2"  in password or "3"  in password or "4"  in password or "5"  in password or "6"  in password or "7"  in password or "8"  in password or "9"  in password:
            print("strong password")
        else:
            print("password should have at;least one number")
    else:
        print("password should have atleast one special charecter")
      
    
else:
    print("password at least 6 charecters")