a=[1, 1, 1, 1]
n=len(a)
start_index=0
count=0
for i in range(n):
    start_index=i
    if a[i]==0:
        a[i]=1
        count+=1
        start_index=i+1
        while start_index<n:
            if a[start_index]==0:
                a[start_index]=1
            else:
                a[start_index]=0
            start_index+=1
print(count)