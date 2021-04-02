# Iterative Solution
def binarySearch(array, target):
    right = len(array)-1
	left = 0
	while left <= right:
		middle = (left + right) // 2
		numberToBeMatchedAfterSearch = array[middle]
		if numberToBeMatchedAfterSearch == target:
			return middle
		elif numberToBeMatchedAfterSearch < target:
			left = middle + 1
		else:
			right = middle - 1
	return -1


# Recursive Solution 
def binarySearch(array, target):
	return binarySearchHelperFunc(array, 0, len(array)-1, target)
	
def binarySearchHelperFunc(array, left, right, target):
	if left > right:
		return -1
	middle = (left + right) // 2
	elemFoundAfterSearching = array[middle]
	if elemFoundAfterSearching == target:
		return middle
	elif elemFoundAfterSearching < target:
		return binarySearchHelperFunc(array, middle + 1, right, target)
	else:
		return binarySearchHelperFunc(array, left, middle - 1, target)
	
