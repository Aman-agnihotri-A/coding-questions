a=[[1,2],[3,4]]
n=len(a)
for i in range(n):
    for j in range(n):
        if i<j:
            temp=a[i][j]
            a[i][j]=a[j][i]
            a[j][i]=temp
print(a)
for i in range(n):
    a[i]=a[i].reverse()
print(a)