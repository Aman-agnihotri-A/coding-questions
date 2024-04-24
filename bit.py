A=[1, 2, 4, 3, 3, 2, 2, 3, 1, 1]
ans=0
for i in range(32):
    c=0
    for j in range(len(A)):
        x=(A[j]>>i)&1
        print(x)
        if x==True:
            c+=1
    if c%3!=0:
        ans=(1<<i)|ans
print(ans)