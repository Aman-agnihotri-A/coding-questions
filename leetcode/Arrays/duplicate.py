class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        d=set(nums)
        if len(nums)==len(d):
            return "false"
        return "true"
    
print(Solution().containsDuplicate([1,2,3,4]))