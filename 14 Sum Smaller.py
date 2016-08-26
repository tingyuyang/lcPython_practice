"""
Implemented based on 3sum...
You are given a int[N] array num, count how many triplets (x, y, z) that
num[x] + num[y] + num[z] < K
assuming x < y < z

num[] = {5, 3, 6, 1, 8, 10}  K = 13

5 + 3 + 1 = 9 < 13
5 + 6 + 1 = 12 < 13
3 + 6 + 1 = 10 < 13
3 + 1 + 8 = 12 < 13
"""
def sumSmaller(nums,input):
	result = []
	i=0
	count = 0
	while i < len(nums)-1:
		if i == 0 or nums[i]!=nums[i-1]:
			j= i+1
			k=len(nums)-1
			while j<k:
				if nums[i]+nums[j]+nums[k]<input:
					result.append([nums[i],nums[j],nums[k]])
					count +=1
					j+=1
					k=len(nums)-1 #so once i found the "<" as required. i will count from the last item compare against j
				elif nums[i]+nums[j]+nums[k]>=input:
					print("been here")
					k-=1

		i+=1
	print(count)
	return result
		
	

nums = [5, 3, 6, 1, 8, 10]
print(sumSmaller(nums,13))
