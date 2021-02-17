# space : O(1) , time : O(n^2)
def twoNumberSum(array, targetSum):
	for i in range(len(array) - 1):
		firstNum = array[i]
		for j in range(i+1,len(array)):
			secondNum = array[j]
			if firstNum + secondNum == targetSum:
				return [firstNum, secondNum]
	return []

# space : O(n) , time : O(n)
def twoNumberSum(array, targetSum):
	twoSumTable = {}
	for elem in array:
		numberToCheckInTable = targetSum - elem
		if numberToCheckInTable in twoSumTable:
			return [numberToCheckInTable, elem]
		else:
			twoSumTable[elem] = True
	return []

# time : O(nlogn), space : O(1)
def twoNumberSum(array, targetSum):
    array.sort()
	lPointer = 0
	rPointer = len(array)-1
	while lPointer < rPointer:
		cSum = array[lPointer] + array[rPointer]
		if (cSum) == targetSum:
			return [array[lPointer], array[rPointer]]		
		if (cSum) < targetSum:
			lPointer += 1
		elif (cSum) > targetSum:
			rPointer -= 1
	return []
	
