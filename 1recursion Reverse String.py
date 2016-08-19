def rreverse(s):
	i=0
	if s == "":
		return s
	else:
		return rreverse(s[i+1:]) + s[i]

print(rreverse("hello"))
