A=[ 2, 3, -1, 4, 2, 1 ]
B=4
prefix_sum=[]
suffix_sum=[]
n=len(A)
prefix_sum.append(A[0])
suffix_sum.append(A[n-1])
for i in range(1,B):
    prefix_sum.append(A[i]+prefix_sum[i-1])
    suffix_sum.append(A[n-i-1]+suffix_sum[i-1])
max_sum=max(prefix_sum[B-1],suffix_sum[B-1])
h=0
B-=1
for i in range(B):
    h=prefix_sum[i]+suffix_sum[B-i-1]
    max_sum=max(max_sum,h)
print(max_sum)