A=[1,2,3]
n=len(A)
print(n)
if n==1:
    print(0)
y=[]
for i in range(n-2,-1,-1):
    if A[i]<A[i+1]:
        
        y=A[i+1:]
        y=y[::-1]
        print(y)
        A=A[0:i+1]
        print(A)
        break
for i in range(len(y)):
    A.append(y[i])
print(A)