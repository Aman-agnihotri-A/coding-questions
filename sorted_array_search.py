class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def search(self, A, B):
        return A.index(B)
print(Solution().search([3,4,5,6,7,0,1,2],5))