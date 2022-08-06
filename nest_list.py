list=[[1,4,5],[1,3,4],[2,6]]

l=[]
li=[]
i=0
while i<len(list):
    j=0
    while j<len(list[i]):
        a=list[i][j]
        li.append(a)
        j=j+1
    i=i+1 
print(sorted(li))