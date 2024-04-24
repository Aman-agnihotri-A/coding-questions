A=[26,23,23,16,27,18,7]
lengthOfArray=len(A)
countOfTriplet=0
for i in range(1,lengthOfArray-1):
    smaller=0
    greater=0
    for j in range(0,i):
        if A[j]>A[i]:
            smaller+=1
            print(A[i],A[j])
    for j in range(i+1,lengthOfArray):
        if A[i]>A[j]:
            greater+=1
            print(A[i],A[j])
    countOfTriplet+=smaller*greater
    print(smaller,greater)