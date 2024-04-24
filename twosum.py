A=[2,7,11,45,65]
t=9
f={}
for i,x in enumerate(A):
    d=t-x
    
    if d in f:
        print(d)
        print([f[d],i])
    else:
        f[x]=i
print(f)