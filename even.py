s = "This is a python language"
str=s.split()
i=0
while i<len(str):
    if len(str[i])%2==0:
        print(str[i])
    i=i+1

