"""
Given an array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. > Could you implement it without using extra memory?
"""

#simple solution:
num=[1,1,2,2,3]
def singleNumber(num):
	num.sort()
	count = 0
	for i in range(1,len(num)-1):
		if num[i]!=num[i-1] and num[i]!=num[i+1]:
			return (num[i])
	return(num[len(num)-1])

print(singleNumber(num))
