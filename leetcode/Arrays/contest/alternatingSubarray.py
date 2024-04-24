class Solution:
    def alternatingSubarray(self, nums: list[int]) -> int:
        n=len(nums)
        length=0
        result=-1
        i=0
        start_index=0
        #flag=0
        while i<n-1:
            flag=0
            if  nums[i+1]-nums[i]==1 and i<n-1:
                length+=1
                i+=1
                flag=1
            if i<n-1 and flag==1 and nums[i+1]-nums[i]==-1:
            
                length+=1
                i+=1
            print(length,i)
            if length!=0:
                result=max(result,length)
            if flag==0:
                length=0
                start_index+=1
                i=start_index
            
        return result
                
print(Solution().alternatingSubarray([2,3,4,3,4]))