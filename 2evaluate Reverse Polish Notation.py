"""
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Some examples:

  ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
  ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
"""
def evalRPN(tokens):
	stack=[]
	for t in tokens:
		if t not in "+-*/":
			stack.append(int(t)) #convert string to integer
		else:
			b=stack.pop() #pay attention to the order!!!
			a=stack.pop()
			if t=="+":
				stack.append(a+b)
			elif t=="-":
				stack.append(a-b)
			elif t=='*':
				stack.append(a*b)
			else:
				stack.append(a/b)
	return int(stack[0]) #make the result to int
tokens=["4", "13", "5", "/", "+"]
print(evalRPN(tokens))
