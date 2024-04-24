class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        if int(A)<10:
            A='10'
        #print(type(A))
        A= str(int(A)+1)
        
        #print(A[(len(A)//2)+1::-1])
        if len(A)%2==0:
            x=A[len(A)//2:]
            y=A[:len(A)//2]
            if int(y[::-1])<int(x):
                y=str(int(y)+1)

                return y+y[::-1]
            else:
                return y+y[::-1]
            
        else:
            x=A[(len(A)//2)+1:]
            y=A[:len(A)//2]
            f=A[:len(A)//2+1]
            print(f)
            if int(y[::-1])<int(x):
                f=str(int(y)+1)

                return f+y[::-1]
            else:
                return f+y[::-1]

                
            
            
        
c='88245' 
print(Solution().solve(c))
