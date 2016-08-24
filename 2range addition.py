def getModifiedArray(length, updates):
	result=[0]*length
	for update in updates:
		result[update[0]] += update[2]
		if(update[1]+1<length):
			result[update[1]+1]=result[update[1]+1]-update[2]
	print(result) #[-2, 2, 3, 2, -2]
	for i in range(1,length):
		result[i]+=result[i-1]
	return (result) #[-2, 0, 3, 5, 3]
            
length = 5
updates =  [
	[1,  3,  2],
	[2,  4,  3],
	[0,  2, -2]
]
new=getModifiedArray(length,updates)
print(new)
