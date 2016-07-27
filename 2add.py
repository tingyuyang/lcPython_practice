def add(n):
	if (n<1 or n>100000000):
		print('The input number is out of range, please enter another number')
		return -1
	s=str(n)+' '
	sub=""
	max=0
	for i in range(0, len(s)-1):
		if (s[i]!=s[i+1]):
			a =s[i]
			sub = s[:i+1]+a+s[i+1:]
			if(max<int(sub)):
				max =int(sub)
		i=i+1
	print (max)
