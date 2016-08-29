#this is BIT!!!!!!
# nums = [1, 3, 5]

class NumArray(object):
    def __init__(self, nums):
        self.nums = [0]*len(nums) #[0,0,0]
        self.sums = [0]*(len(nums)+1) #[0,0,0,0]
        for i, num in enumerate(nums):
            self.update(i, num)
    
    def update(self, i, val):
        old = self.nums[i]
        self.nums[i]=val
        diff = val-old
        i+=1
        while i<len(self.sums):
            self.sums[i]+=diff
            i += i&(-i)
    
    def sum(self, i):
        sum = 0
        i+=1
        while i!=0:
            sum+= self.sums[i]
            i -= i&(-i)
        return sum
        
    def sumRange(self, i, j):
        return self.sum(j)-self.sum(i-1)

nums = [1, 3, 5]
numArray = NumArray(nums)
print("///////////////")
print(numArray.sumRange(0, 2))

"""
sumRange(0, 2) -> 9
update(1, 2)
sumRange(0, 2) -> 8
"""
