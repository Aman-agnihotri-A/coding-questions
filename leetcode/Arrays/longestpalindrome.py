class Solution:
	# @param A : string
	# @return a strings
    def palindrome(A,p1,p2,n):
        while p1>=0 and p2<n and A[p1]==A[p2]:
            p1-=1
            p2+=1
        #print(A[p1+1:p2],A[p1:p2])
        return A[p1+1:p2]

    def longestPalindrome(A):
        n=len(A)
        ans=''
        if n==1:
            return 1
        for i in range(n):
            odd=Solution.palindrome(A,i,i,n)
            even=Solution.palindrome(A,i,i+1,n)
            print(even)
            if len(odd)>len(ans):
                ans=odd
            if len(even)>len(ans):
                ans=even
        return ans
print(Solution.longestPalindrome('bb'))
