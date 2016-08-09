"""
Given an array nums, write a function to move all 0's to the end of it while
maintaining the relative order of the non-zero elements.
For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums
should be [1, 3, 12, 0, 0].
Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        count = 0
        for i in range(0, length):
        	if (nums[i]!=0): # was considering doing == 0 be4. interesting reverse thought.
        		nums[count]=nums[i]
        		count = count+1 
        # after this for loop. nums=[1, 3, 12, 3, 12], count = 3
        for j in range(count,length):
        	nums[j]=0
        	
"""
# false answer but good to know,its not working
class Solution(object):#not REALLY working, 
    def moveZeroes(self, nums):
        length = len(nums)
        count = 0
        for i in range(0, length):
            if (nums[i] == 0):# if we find a zero in the list
                count = count +1 #count how many zero is in the string
        nums = [x for x in nums if x!=0]
        for i in range (0, count):
        	nums.extend([0])
        print(nums)#it will work here.
--------comment of the false code--------
a1 = [0, 1, 0, 3, 12]
s = Solution()
s.moveZeroes(a1) #here print out: [1, 3, 12, 0, 0]
print (a1)  #if i print a1 here,[0, 1, 0, 3, 12], the list won't change...weird.
"""
