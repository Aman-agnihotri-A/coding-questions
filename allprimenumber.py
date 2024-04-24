class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        if A<=1:
            return 0
        elif A==2:
            return 1
        elif A==3:
            return 2
        count=2
        for i in range(4,A+1):
            flag=0
            
            x=int(i**0.5)
            for j in range(2,x+1):
                if i%j==0:
                    flag=1
            print(count,i,x)
            if flag==0:
                count+=1
        return count
print(Solution().solve(10))