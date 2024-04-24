class Solution:
	# @param A : string
	# @param B : string
	# @return a strings
    def addBinary(self, A, B):
        n=len(A)
        m=len(B)
        first=0
        second=0
        for i in range(n-1,-1,-1):
            first+=2**i
        for i in range(m-1,-1,-1):
            second+=2**i
        print(first,second)
        
        ans=first+second
        print(ans)
        result=''
        while ans>0:
            result+=str(ans%2)
            ans=ans//2
        
        return result[::-1]
print(Solution().addBinary('100','11'))