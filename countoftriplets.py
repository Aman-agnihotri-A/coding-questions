a=[2,6,9,4,10]
n=len(a)
count=0
for i in range(n-2):
    j=i+1
    k=i+2
    while k<n:
        if a[i]<a[j]<a[k]:
            count+=1
        
            print(a[i],a[j],a[k])
        k+=1
        if k==n:
            j+=1
            k=j+1
            #print(j,k)
    j=i+1
    k=i+2
        
    
        
        
        
            
        
        
print(count)