def binarySearch(list,item):
	if len(list) ==0:
		return False
	else:
		midpointi = len(list)//2
		if list[midpointi]==item:
			found = True
		else:
			if item<list[midpointi]:
				return binarySearch(list[:midpointi],item)
			else:
				return binarySearch(list[midpointi+1:],item)
	return found

list = [0,1,2,8,9,10,13]
print(binarySearch(list,1)) #>> True
print(binarySearch(list,3)) #>> False
