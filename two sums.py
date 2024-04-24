class Solution:
    def twoSum(self, nums, target):
        f= dict()
        for i,x in enumerate(nums):
            diff=target - x
            if diff in f:
                return [f[diff],i]
            f[x]= i
        print(f)
s=Solution()
print(s.twoSum([2,7,11,15],9))
