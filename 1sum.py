#Problem: You are given an integer n. Count result of sum=  1+2+ ... + n

#the SlOWEST SOLUTION
"""
def slow_solution(n):
  result = 0
  for i in xrange(n):
    for j in xrange(i + 1):
      result += 1
  return result
  
because this method is nested loop, so the time complexity wil be O(N^2), 
so here is the fast one
"""

# FASTER SOLUTION
def faster_solution(n):
	result = 0
	for i in range(n):
		result = result + (i + 1) # i will be 0,1,2,3 every time the for loop runs
	print(result)
# if n = 5, result is 15
# very interesting, the complexity will be O(N) then ::)

# FASTEST SOLUTION with complexity of O(1)
def model_solution(n):
	result = n * (n + 1) // 2 #based on our middle school math knowledge.FUNCTION
	return result

