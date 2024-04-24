A = "abcabbccd"
B=3
c={}
for i in range(len(A)):
    if A[i] in c:
        c[A[i]]+=1
    else:
        c[A[i]]=1
count=0
for i in sorted(c.values()):
    if (B-i)>=0:
        print(B)
        B-=i
    else:
        count+=1
print(count)
