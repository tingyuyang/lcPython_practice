def shellSort(list):
	sublistGap = len(list)//2
	while sublistGap>0:
		for start in range(sublistGap):
			gapInsertionSort(list,start,sublistGap)
		sublistGap=sublistGap//2

def gapInsertionSort(list,start,gap):
	for i in range(start+gap,len(list),gap):#compare the later item against the first item
		current=list[i]
		position = i
		while position>=gap and list[position-gap]>current: #if BEFORE item is larger than LATER item
			list[position]=list[position-gap] #list[position]=list[i]=current
			position= position-gap
		list[position]=current
			
			
		
list=[54,26,93,17,77,31,44,55,20]
shellSort(list)
print(list)
