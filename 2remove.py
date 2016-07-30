#remove the small digits
#123-> 23,13

def remove(n):
	if (n<10 or n>1000000000):
		print('The input number is out of range, please enter another number')
		return -1
	s = str(n) # change the int into string
	min = n
	check = s[0]
	sub =""
	for i in range(0,len(s)-1):
		#curChar = s[i]
		if (s[i] < s[i+1]):
			a =s[i+1]
		else:
			a =s[i]
		sub = s[:i] + a + s[i+2:]
		if(min > int(sub)):
				min = int(sub)
	return (min)
