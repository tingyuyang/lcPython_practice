def selectionSort(list): #arrange the list in order
	length=len(list)-1
	currentMax=list[length]
	for i in range(0,len(list)):
		if list[i]>currentMax:
			currentMax=list[i]
			temp = list[length]
			list[length]=currentMax
			list[i] = temp
			length=length-1

list=[3,6,7,9,8]
selectionSort(list)
print(list)
"""
def selectionSort(alist):
   for fillslot in range(len(alist)-1,0,-1):
       positionOfMax=0
       for location in range(1,fillslot+1):
           if alist[location]>alist[positionOfMax]:
               positionOfMax = location

       temp = alist[fillslot]
       alist[fillslot] = alist[positionOfMax]
       alist[positionOfMax] = temp
"""
