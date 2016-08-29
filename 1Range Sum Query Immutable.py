""""
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.
list = [-2, 0, 3, -5, 2, -1]
find sum from index 0 to 5,(-2+0+3-5+2-1)=-3
from index 2 to 5(3-5+2-1)=-1
"""
class NumArray(object):
    def __init__(self, nums):
        self.nums = nums
        self.sums = [] #the sum list
        sum = 0
        for num in self.nums:
            sum =sum+ num
            self.sums.append(sum)
        # print(self.sums)

    def sumRange(self, i, j):
    	if i>j: return 0
    	elif i==j:return (self.nums[i])
    	elif i!=0:
    		return self.sums[j]-self.sums[i-1]
    	else:# i==0
    		return self.sums[j]
list = [-2, 0, 3, -5, 2, -1]
s=NumArray(list)
print(s.sumRange(0,2))
