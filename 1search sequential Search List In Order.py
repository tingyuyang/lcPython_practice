#if the list is in order, search the item
def searchList(list,item):
	found = False
	i = 0
	exceed = False #if the list[i] already exceed searching item (because list is in order)
	while i<len(list) and not found and not exceed:
		if list[i]==item:
			found = True
		else:
			if list[i]>item:
				exceed= True
				print("Exceed")
			else:
				i = i+1
	return found
list = [1,2,3,4]
print(searchList(list,1.5)) #>>Exceed, False
