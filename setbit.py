A=53
B=5
result=''
while A>0:
    result+=str(A%2)
    A=A//2
l1=list(result)
print(l1)
ans=0
for i in range(B,len(l1)):
    if l1[i]=='1':
        ans+=2**i

print(ans)