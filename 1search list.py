def searchList(list,item):
	found = False
	i = 0
	while i<len(list) and not found:
		if list[i]==item:
			found = True
		else:
			i = i+1
	return found
list = [1,2,3]
print(searchList(list,1)) #output >> True
print(searchList(list,4)) #output >> False
