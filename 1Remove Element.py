"""
Given an array and a value, remove all instances of that value in place and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example:
Given input array nums = [3,2,2,3], val = 3

Your function should return length = 2, with the first two elements of nums being 2.
"""
class Solution(object):
    def removeElement(self, nums, val):
        j = len(nums)-1
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == val:
                nums[i], nums[j] = nums[j], nums[i] #for the last round, exchange nums[0] with nums[2]--->(3,2) to (2,3)
                j -= 1
        return j+1
#final nums=[2，2，3，3]
