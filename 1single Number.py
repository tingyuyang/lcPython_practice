"""
Given an array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. > Could you implement it without using extra memory?
"""

#simple solution:
num=[1,1,2,2,3]
def singleNumber(self,nums):
    	if len(nums)==1:
    		return nums[len(nums)-1]
    	nums.sort()
    	for i in range(1,len(nums)-1):
    		if nums[i]!=nums[i-1] and nums[i]!=nums[i+1]:
    			return (nums[i])
    	if nums[0]!=nums[1]:
    		return nums[0]
    	else:
    		return(nums[len(nums)-1])

print(singleNumber(num))
