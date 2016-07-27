def add(n):
	s = str(n) # change the int into string
	min = 0
	check = s[0]
	sub =""
	a ="" # a should be a digits enroll everytime when !=
	i=0
	while (i<len(s)):
		check2 =s[i]
		print('No',i)
		if (check != check2): # if two numbers are !=they should copy
			print('what')
			a = check
			sub = s[:i] + a + s[i:]
			print ('{}:{}'.format(i,sub))	
			check = check2
		i=i+1
	return (1)
