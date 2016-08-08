class Solution(object):#not REALLY working, 
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
        print(nums)#it will work here.
"""
a1 = [0, 1, 0, 3, 12]
s = Solution()
s.moveZeroes(a1) #here print out: [1, 3, 12, 0, 0]
print (a1)  #if i print a1 here,[0, 1, 0, 3, 12], the list won't change...weird.
"""
