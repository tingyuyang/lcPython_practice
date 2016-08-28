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
		i-=1 #plz remember this!!!
	if up:
		list.insert(0,1)
	return list
list=[1,9,9]
print(plusOne(list))
"""
比如可以扩展这个到两个数组相加，或者问一些OO设计，假设现在要设计一个BigInteger类，那么需要什么构造函数，然后用什么数据结构好，用数组和链表各有什么优劣势
。这些问题虽然不是很难，但是可以考到一些基本的理解，所以平时准备有机会还是可以多想想哈。
"""
