class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        x=A[::-1]
        #x=x[0:2]+A[2]+x[2:]
        print(x)
        for i in range(len(A)):
            if x==x[::-1]:
                return i
            x=x[0:i]+A[i]+x[i:]
            print(x)

print(Solution().solve("abbas"))