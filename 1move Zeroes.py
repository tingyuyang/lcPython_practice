# sth is wrong apparently, but if i run in repl.it, is was ok...
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        count = 0
        for i in range(0, length):
            if (nums[i] == 0):# if we find a zero in the list
                count = count +1 #count how many zero is in the string
        nums = [x for x in nums if x!=0]
        for i in range (0, count):
        	nums.extend([0])
