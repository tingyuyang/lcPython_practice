#clearly, the solution is not efficient enough.

class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        count = 0
        if (a>0):
            while (a>0):
                count = count +1
                a = a-1
        if (a<0):
            while (a !=0):
                count = count -1
         		a = a+1
        if (b>0):
            while (b>0):
                count = count +1
                b = b -1
        if (b<0):
            while (b !=0):
         		count = count -1
         		b = b+1 		
        return (count)  
