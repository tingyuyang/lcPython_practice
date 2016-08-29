"""
- Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by its upper left corner (row1, col1) 
and lower right corner (row2, col2).

- The above rectangle (with the red border) is defined by (row1, col1) = (2, 1) and (row2, col2) = (4, 3), which contains sum = 8.

- Given matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

sumRegion(2, 1, 4, 3) -> 8
sumRegion(1, 1, 2, 2) -> 11
sumRegion(1, 2, 2, 4) -> 12
"""
class NumMatrix(object):
    def __init__(self, matrix):
        self.matrix = matrix
        if matrix:
        	row0=[]
        	sum=0 
        	
        	#1.find the sum of first row
        	for m in matrix[0]:
        		sum+=m 
        		row0.append(sum) 
        	self.sums=[row0] # rmb to store in self.sum after step 1.
        	
        	#2. then find sum for first column+*0 to other item
        	sumr0=3
        	for i in range(1,len(matrix)):
        		sumr0+=matrix[i][0]
        		row=[sumr0]+[0]*(len(matrix)-1)
        		self.sums.append(row)
        	
        	#3.construct overall sum matrix
        	for i in range(1, len(matrix)):
        		for j in range(1, len(matrix[0])):
        			self.sums[i][j] = matrix[i][j] + self.sums[i-1][j] + self.sums[i][j-1] - self.sums[i-1][j-1]
        	print(self.sums)
        	
    def sumRegion(self, row1, col1, row2, col2):
        if not self.matrix:
        	return 0 
        sum=self.sums[row2][col2]
        if row1>0:
        	sum-=self.sums[row1-1][col2]
        if col1>0:
        	sum-=self.sums[row2][col1-1]
        if row1>0 and col1>0:
        	sum+=self.sums[row1-1][col1-1]
        return sum
        

# Your NumMatrix object will be instantiated and called as such:
matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]
numMatrix = NumMatrix(matrix)
print(numMatrix.sumRegion(2, 1, 4, 3))
