a=[2, 1, 6, 4]
n=len(a)
print(n)
pre_even=[0]*n
pre_odd=[0]*n
post_even=[0]*n
post_odd=[0]*n
pre_even[0]=a[0]
pre_odd[0]=0
if (n-1)%2==0:
    post_even[n-1]=a[n-1]
    #post_odd[n-1]=0
else:
    post_odd[n-1]=a[n-1]
    #post_even[n-1]=0
for i in range(0,n):
    if i%2==0:
        pre_even[i]=a[i]+pre_even[i-1]
        pre_odd[i]=pre_odd[i-1]
        
    else:
        pre_even[i]=pre_even[i-1]
        pre_odd[i]=pre_odd[i-1]+a[i]

        
for i in range(n-2,-1,-1):
    if i%2==0:
        post_even[i]=post_even[i+1]+a[i]
        post_odd[i]=post_odd[i+1]
    else:
        post_odd[i]=post_odd[i+1]+a[i]
        post_even[i]=post_even[i+1]
print(pre_even,pre_odd,post_even,post_odd)
for i in range(n):
    if i==0 :
        if(post_even[i+1]==post_odd[i+1]):
            print(True,"first")
    elif i==(n-1) :
        if (pre_even[i-1]== pre_odd[i-1]):
            print(True,"second")
    elif pre_even[i-1]+post_odd[i+1]==pre_odd[i-1]+post_even[i+1]:
        print(True,"third")

    
