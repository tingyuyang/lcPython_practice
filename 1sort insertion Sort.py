def insertionSort(list):
	for i in range(1,len(list)):
		storedValue=list[i]
		index =i
		while index>0 and storedValue< list[index-1]: #if storedValue smaller than index-1, we will stop the loop
			list[index]=list[index-1]
			index=index-1
		list[index]=storedValue #must be index not "i"
		
list=[54,26,93,17,77,31,44,55,20]
insertionSort(list)
print(list)
