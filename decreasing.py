nums=[10,4,9,1,3,5]
res = 0
sum = 0
for i in range(len(nums)):
    if i == 0 or nums[i - 1]> nums[i]:
        sum += nums[i]
        print(sum,nums[i])
    else:
        sum = nums[i]
    res = max(res, sum)
print(res)