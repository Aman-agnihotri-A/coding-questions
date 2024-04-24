class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        if A<=3:
            return 0
        
        count=0
        for i in range(1,A//2+1):
            if A%i==0:
                count+=i
        #print(count)
        if count == A:
            return 1
        else:
            return 0
print(Solution().solve(6))