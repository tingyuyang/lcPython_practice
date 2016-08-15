#need further revise
#https://www.glassdoor.com/Interview/Get-the-kth-largest-number-from-two-sorted-arrays-QTN_290643.htm
def kthlargest(arr1, arr2, k):
    if len(arr1) == 0:
        return arr2[k] # coz it is sorted array, so return kth index
    elif len(arr2) == 0:
        return arr1[k]
    mida1 = int(len(arr1)/2) #the middle index of arr1
    mida2 = int(len(arr2)/2)
    if mida1+mida2<k: # if the sum of middle index of both array less than k
        if arr1[mida1]>arr2[mida2]:
        	return kthlargest(arr1[:mida1+1], arr2[mida2:], k-mida1-1)
        else:
        	return kthlargest(arr1[mida1:], arr2[:mida2+1], k-mida2)
    else:
        if arr1[mida1]>arr2[mida2]:
        	return kthlargest(arr1, arr2[mida2+1:], k+mida1) #this line is fixed
        else:
        	return kthlargest(arr1[mida1+1:], arr2, k+mida2) #fixed
