def selectionSort(list): #arrange the list in order
	for i in range(len(list)-1,0,-1):
		maxPosition = 0
		for current in range(1,i+1):
			if list[current]>list[maxPosition]:
				maxPosition=current
		temp = list[i]
		list[i]=list[maxPosition]
		list[maxPosition]=temp
			
list=[54,26,93,17,77,31,44,55,20]
selectionSort(list)
print(list)
