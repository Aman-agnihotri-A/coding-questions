class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @param D : integer
    # @return an integer
    def solve(self, A, B, C, D):
        l=list()
        l.append(A)
        l.append(B)
        l.append(C)
        l.append(D)
        g=set(l)
        if  len(g)==2 and l.count(l[0]) == 2:
            
            return 1
        else:
            return 0

g=Solution().solve(1,2,1,2)
print(g)
