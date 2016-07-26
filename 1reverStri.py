"""
Write a function that takes a string as input and returns the string reversed.

Example:
Given s = "hello", return "olleh".

Subscribe to see which companies asked this question
"""

class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = list(s) # if print (list[5]), ok if it is 5, it will be out of range
        i = 0
        result= [None] * len(s) #make an empty list with that length
        length = len(s)-1
        while i < len(s):
        	# we could do "print (i, length)" in python
        	result[i]= l[length]
        	i = i +1
        	length = length - 1
        string = "".join(result)
        return (string)
        
"""
online solution:

s = 'hello'
result =''
l =len(s)
while (l>0): #this is the ***key, if (l>=0), won't work
	l=l-1
	result = result +s[l]
print(result)
"""
