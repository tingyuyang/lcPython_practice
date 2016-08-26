# Time:  O(n^2)
# Space: O(1)
#
# Given an array S of n integers,
# are there elements a, b, c in S such that a + b + c = 0?
# Find all unique triplets in the array which gives the sum of zero.
#
# Note:
# Elements in a triplet (a,b,c) must be in non-descending order. (ie, a <= b <= c)
# The solution set must not contain duplicate triplets.
#    For example, given array S = {-1 0 1 2 -1 -4},
#
#    A solution set is:
#    (-1, 0, 1)
#    (-1, -1, 2)
#
def threeSum(nums):
	nums=sorted(nums)
	result = []
	i=0
	count = 0
	while i < len(nums)-1:
		if i == 0 or nums[i]!=nums[i-1]:
			j= i+1
			k=len(nums)-1
			while j<k:
				if nums[i]+nums[j]+nums[k]<0:
					j+=1
				elif nums[i]+nums[j]+nums[k]>0:
					k-=1
				else:
					result.append([nums[i], nums[j], nums[k]])
					j=j+1 
					k=k-1
					while j < k and nums[j] == nums[j - 1]: #so maybe the list[-4, -1, -1, 0, 1, 2], for item"-1", because it repeated, we do not wanna print the same list，so we will compare the next item  搜
						j =j+1
					while j < k and nums[k] == nums[k + 1]:
						k =k- 1
		i+=1
	return result
		
	

nums = [-1, 0, 1, 2, -1, -4]
print(threeSum(nums)) #[[-1, -1, 2], [-1, 0, 1]]
