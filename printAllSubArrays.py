a=[1,2,3]
n=3
g=[]
for i in range(n):          #1,2,3
    
    for j in range(n):      # 1to1 1 to 2 1 to 3
        f=[]
        for k in range(i,j+1): #1 to 1  
            f.append(a[k])
        g.append(f)
print(g)