#the list will be in order
def binarySearch(list,item):
	found = False
	firsti= 0
	lasti = len(list)
	while firsti<=lasti and not found:
		midpointi = (firsti+lasti)//2
		if list[midpointi]==item:
			found = True
		else:
			if item<list[midpointi]:
				lasti=midpointi-1
			else:
				firsti=midpointi+1
	return found

list = [0,1,2,8,9,10,13]
print(binarySearch(list,1)) #>> True
print(binarySearch(list,3)) #>> False

