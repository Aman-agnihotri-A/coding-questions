class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        b=set()
        count =0
        if 'o'  not in A:
            return -1
        elif 'x' not in A:
            return -1
        for i in range(len(A)):
            if A[i]=='x':
                for j in range(len(A)):
                    if A[j]=='o':
                        b.add(abs(i-j))
        print(b)
        return min(b)
            
b=Solution()
c= b.solve('xxx...xxx')
print(c)