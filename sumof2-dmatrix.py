a=[[1,2,3],[4,5,6],[7,8,9]]
n=len(a)
c=[]
for i in range(n):
    b=[0]*n
    j=i
    k=0
    while j>=0 and k<=i:
        b[k]=a[k][j]
        j-=1
        k+=1
    c.append(b)

#k=n-1
for i in range(n-1):
    b=[0]*n
    f=0
    j=i+1
    print(j)
    k=n-1
    #print(j,k)
    while j<n and k>=0:
        b[f]=a[j][k]
        #print(j,k)
        f+=1

        j+=1
        k-=1
    c.append(b)



print(c)