class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @return a list of integers
    def solve(self, A, B, C):
        while B<C:
            temp=A[C]
            A[C]=A[B]
            A[B]=temp
            B+=1
            C-=1
        
        return A
print(Solution().solve([6,7,10,3,10,10,3,10],0,4))
                        
