a=[4]
b=78
total=0
start_index=0
max_sum=0
n=len(a)
i=0
print(n)
while i<n:
    if a[i]+total<=b:
        total+=a[i]
        print(total)
        max_sum=max(max_sum,total)
        i+=1
    else:
        total=0
        start_index+=1
        i=start_index
print(max_sum)