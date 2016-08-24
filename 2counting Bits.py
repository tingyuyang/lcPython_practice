def countBits(num):
	list=[0,1]
	counter=0
	threshold=2
	for i in range(2,num+1):
		counter+=1
		list.append(list[i-threshold]+1)
		if counter==threshold:
			threshold*=2
			counter=0
	return list
print(countBits(8))

#[0, 1, 1, 2, 1, 2, 2, 3, 1]
