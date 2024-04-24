class Solution:
    # @param A : list of integers               8 6 
    # @param B : list of list of integers
    # @return a list of integers
    def solve(self, A, B):
        for i in range(len(A)):
            if A[i]%2==0:
                A[i]=1
            else:
                A[i]=0
            if i>0:
                A[i]+=A[i-1]
        print(A)
        d=[]
        for i in range(len(B)):
            
            l=B[i][0]
            r=B[i][1]
            if i==0:
                d.append(A[r])
            else:
                d.append(A[r]-A[l-1])
        return d
print(Solution().solve([8,6,7,10,3,10,10,3],[[0,4],[4,7],[2,7],[6,7],[6,7],[0,1],[2,6],[4,6],[0,1],[1,2]]))