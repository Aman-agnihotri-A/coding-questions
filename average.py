A=[4,3,17,3,8,8,14,19,4,10,6,17,19,13,10,12,7,8,17,5]
B=8
sum_window=0
for i in range(B):
    sum_window+=A[i]

index=0
result=sum_window/B
print(result)
start_index=1
end_index=B
n=len(A)
while end_index<n:
    sum_window=sum_window-A[start_index-1]+A[end_index]
    f=sum_window/B
    if f<result:
        index=start_index
        result=f
        print(result,index)
    start_index+=1
    end_index+=1
print(index)
