a=[2,9,5]
total=0
i=0
start_index=0
f=0
n=len(a)
while i<n:
    f+=a[i]*(i+1)*(n-i)
    i+=1
print(f)