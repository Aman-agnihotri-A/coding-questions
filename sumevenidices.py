a=[16,3,3,6,7,8,17,13,7]
for i in range(1,len(a)):
    if i %2==0:
        a[i]+=a[i-1]
    else:
        a[i]=a[i-1]
print(a[6]-a[1])