"""
Given a non-negative number represented as an array of digits, plus one to the number.

The digits are stored such that the most significant digit is at the head of the list.

so [1,2,3,4]->[1,2,3,5]
[1,9,9]->[2,0,0]
***[9,9]->[1,0,0]
"""
def plusOne(list):
	i=len(list)-1
	up=True
	while i>=0:
		list[i]+=1
		if list[i]<10:
			up=False
			break
		else:
			list[i]=list[i]%10 #i think it could be list[i]=0,since it will be 10%10=0...right???
			up=True
		i-=1
	if up:
		list.insert(0,1)
	return list
list=[1,9,9]
print(plusOne(list))
