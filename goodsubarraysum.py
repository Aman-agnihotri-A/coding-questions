a=[15,8,16]
b=242
count=0
n=len(a)
for i in range(n):
    sum_subarray=0
    f=0
    for j in range(i,n):
        sum_subarray+=a[j]
        f+=1
        if sum_subarray>b and f%2==1:
            count+=1
            print(sum_subarray,a[i:j+1])
        if sum_subarray<b and f%2==0:
            count+=1
print(count)
