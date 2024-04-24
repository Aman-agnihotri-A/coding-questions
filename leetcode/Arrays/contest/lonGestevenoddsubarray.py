class Solution:
    def longestAlternatingSubarray(self, nums: list[int], threshold: int) -> int:
        i=0
        lSubarray=0
        m=0
        n=len(nums)
        while i < n:
            
            if nums[i]%2==0 and nums[i]<=threshold:
                lSubarray+=1
                i+=1
                print(i,n)
                if i<n:
                    
                    if nums[i]%2!=0 and nums[i]<=threshold:
                        lSubarray+=1
                        i+=1
                        #m=max(m,lSubarray)
                        #print(nums[i],lSubarray)
                    else:
                        m=max(m,lSubarray)
                        lSubarray=0
                    

                m=max(m,lSubarray)
            else:
                lSubarray=0
                i+=1

        m=max(m,lSubarray)
        return m

                
print(Solution().longestAlternatingSubarray([2,3,4,5,6],18))