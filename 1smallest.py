def kthsmallest(arr1, arr2, k):
    if len(arr1) == 0:
        return arr2[k] # coz it is sorted array, so return kth index
    elif len(arr2) == 0:
        return arr1[k]
    mida1 = int(len(arr1)/2) #the middle index of arr1
    mida2 = int(len(arr2)/2)
    if mida1+mida2<k: # if the sum of middle index of both array less than k
        if arr1[mida1]>arr2[mida2]: # if 
            return kthsmallest(arr1, arr2[mida2+1:], k-mida2-1)
        else:
            return kthsmallest(arr1[mida1+1:], arr2, k-mida1-1)
    else:
        if arr1[mida1]>arr2[mida2]:
            return kthsmallest(arr1[:mida1], arr2, k)
        else:
            return kthsmallest(arr1, arr2[:mida2], k)
  """      
a = (0,2,9,10,12,13,14,16)
b = (8,6) 
k=4
kthlargest(a,b,k)
=> 9
 """
        
