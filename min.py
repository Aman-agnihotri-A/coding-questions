class Solution:
    # @param A : list of integers
    # @return an integer
    def f(self,A):
        A[3]=5
        print(A)
    def solve(self, A):
        x=A[0]
        y=A[0]
        for i in range(1,len(A)):
            x=min(x,A[i])
            y=max(y,A[i])
        print(x,y)
        #print(max(-3,8))
        return x+y
print(Solution().f([3,-3,6,8,4,7,8,-2,0]))

