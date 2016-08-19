def convert(n,base):
	convertBase = "0123456789ABCDEF"
	if (n<base):
		return convertBase[n]
	else:
		return convert(n//base,base) + convertBase[n-base*(n//base)] #method to found reminder, could also be "convertBase[n%base]"
print(convert(1453,16))

#>> 5AD
# so the first calculation will be at the end of the string.
