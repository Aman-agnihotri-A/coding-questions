A=[2,3,4,5]
g=max(A)
f=[1]*g
for i in range(2,g):
    for j in range(i,g):
        f[j]+=1
        j+=i
print(f)