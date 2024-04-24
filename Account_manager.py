class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : list of integers
    # @return a list of integers
    def solve(self, A, B, C):
        result=[]
        stack=[]
        stack.append(C[0]+B)
        result.append(A-1)
        for i in range(1,len(C)):
            n=len(stack)-1
            while n>=0 and n<A:
                print(stack,n)
                if C[i]>=stack[n]:
                    if n==len(stack)-1:
                        stack=[]
                        break
                    else:
                        stack=stack[n+1:]
                        break
                n-=1
            stack.append(C[i]+B)
            if A-len(stack)<0:
                result.append('0')
            else:
                result.append(A-len(stack))
        return result
                


print(Solution().solve(6,6,[1,2,4,6,11,14,17,19]))
        
                

                    
