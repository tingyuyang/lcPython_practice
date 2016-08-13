#Problem: You are given an integer n. Count result of sum=  1+2+ ... + n
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
n=5
result = 0
for i in range(n):
	result = result + (i + 1) # i will be 0,1,2,3 every time the for loop runs
print(result)
#print out 15
# very interesting, the complexity will be O(N) then ::)
