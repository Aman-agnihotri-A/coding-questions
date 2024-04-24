class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        f=set(A)
        A=list(f)
        A.sort()
        return A[-2]%A[-1]
        
print(Solution().solve([1,2,3,4,5,6,3]))