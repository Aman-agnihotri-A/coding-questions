class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):
        b=B%len(A)
        i=0
        j=len(A)-1
        while  i<j:
            temp=A[j]
            A[j]=A[i]
            A[i]=temp
            i+=1
            j-=1
        i=0
        j=b-1
        while i<j:
            temp=A[j]
            A[j]=A[i]
            A[i]=temp
            i+=1
            j-=1
        print(A)
        i=b
        j=len(A)-1
        while i<j:
            temp=A[j]
            A[j]=A[i]
            A[i]=temp
            i+=1
            j-=1
        return A
print(Solution().solve([1,2,3,4,5],2))
        