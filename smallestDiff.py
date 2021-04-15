class Solutions:
    def smallestDifference(self,arrayOne, arrayTwo):
        arrayOne.sort()
        arrayTwo.sort()
        firstPointer = 0
        secondPointer = 0
        difference = float("inf")
		newDiff = float("inf")
        pairFirst , pairSecond = arrayOne[0], arrayTwo[0]
        while firstPointer < len(arrayOne) and secondPointer < len(arrayTwo):
			firstNum = arrayOne[firstPointer]
			secondNum = arrayTwo[secondPointer]
			if firstNum < secondNum:
				newDiff = secondNum - firstNum
                firstPointer += 1
            elif firstNum > secondNum:
				newDiff = firstNum - secondNum
                secondPointer += 1
			else:
				return [firstNum,secondNum]
            if newDiff < difference:
				difference = newDiff
                pairFirst , pairSecond = firstNum, secondNum
        return [pairFirst,pairSecond]

obj = Solutions()
print(obj.smallestDifference([3,4,37,8,9],[1,2,3]))