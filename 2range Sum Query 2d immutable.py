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
