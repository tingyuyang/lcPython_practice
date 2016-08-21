def selectionSort(list):
	for i in range(len(list)-1,0,-1):#count reverse, because we put the large at the end
		maxPosition =0
		for current in range(1,i+1):#start with 1, because it compares against the # in first integer, we try to find the largest #,put the end, ->then second largest, to the second last place
			if list[maxPosition]<list[current]:
				maxPosition=current
		temp=list[i]
		list[i]=list[maxPosition]
		list[maxPosition]=temp
			
list=[54,26,93,17,77,31,44,55,20]
selectionSort(list)
print(list)
