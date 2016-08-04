def remove(n):
	s = str(n) # change the int into string
	max = 0
	lastChar = s[0]
	sub =""
	for i in range(1,len(s)):
		curChar = s[i]
		if (lastChar != curChar):
			lastChar =curChar
		else:
			sub = s[0:i]+s[i+1:]
			if(max <int(sub)):
				max = int(sub)
	return (max)
