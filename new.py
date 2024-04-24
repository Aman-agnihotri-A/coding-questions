a=[0,1,1,0,1]
count=0
c=[]

for i in range(len(a)):
    b=[]
    for j in range(len(a)):
        for k in range(i,j+1):
            c.append(a[k])
            if a[k]==1:
                count+=1
    c.append(b)
                
print(count,c)