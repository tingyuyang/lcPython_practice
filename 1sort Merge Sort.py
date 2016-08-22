def mergeSort(list):
	if len(list)>1:
		mid = len(list)//2
		left = list[:mid]
		right = list[mid:]
		
		mergeSort(left)
		mergeSort(right)

		i=0
		j=0
		k=0
		while i <len(left) and j<len(right):
			if left[i]<right[j]:
				list[k]=left[i]
				i=i+1
			else:
				list[k]=right[j]
				j=j+1
			k=k+1
		while i<len(left):
			list[k]=left[i]
			i=i+1
			k=k+1
		while j<len(right):
			list[k]=right[j]
			j=j+1
			k=k+1
			
alist = [54,26,93,17,77,31,44,55,20]
mergeSort(alist)
print(alist)
