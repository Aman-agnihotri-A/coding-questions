A=[43,38,72,11,43,47]
B=4
C=43
prefix_sum=0
for i in range(B):
    prefix_sum+=A[i]
    if prefix_sum==C:
        print(1,prefix_sum)
start_index=0
end_index=B
n=len(A)
while end_index <n:
    prefix_sum=prefix_sum-A[start_index]+A[end_index]
    if prefix_sum==C:
        print(1,prefix_sum)
    start_index+=1
    end_index+=1
print(0)