def printUnion(arr1, arr2, n1, n2):
	s = set()
	for i in range(0, n1):
		s.add(arr1[i])
	for i in range(0, n2):
		s.add(arr2[i])
	print("Union:")
	for i in s:
		print(i, end=" ")
	print("\n")



def printIntersection(arr1, arr2, n1, n2):
	s = set()

	for i in range(0, n1):
		s.add(arr1[i])
	print("Intersection:")
	for i in range(0, n2):

		if arr2[i] in s:
			print(arr2[i], end=" ")


# Driver Program
arr1 = [7, 1, 5, 2, 3, 6]
arr2 = [3, 8, 6, 21, 7,2]
n1 = len(arr1)
n2 = len(arr2)


printUnion(arr1, arr2, n1, n2)
printIntersection(arr1, arr2, n1, n2)


