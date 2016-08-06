"""
Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

For example:
Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.

Have not try***
Follow up:
Could you do it without any loop/recursion in O(1) runtime?
"""
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        s = str(num) #convert str to int
        a = 0
        while len(s) != 1:
            for i in range(0, len(s)):#***its not len(s)-1 here***
            	a = a+ int(s[i])
            s = str(a)
            a = 0
        return(int(s))
