class Solutions:
    def threeNumberSum(self,array, targetSum):
        finalArrayToBeReturned = []
        array.sort()
        for idx in range(len(array)):
            self.performOperation(array, idx,targetSum, finalArrayToBeReturned)
        return finalArrayToBeReturned

    def performOperation(self,array, index, targetSum, finalArrayToBeReturned):
        firstElement = array[index]
        start_index = index + 1
        end_index = len(array)-1
        while start_index < end_index:
            secondElement = array[start_index]
            thirdElement = array[end_index]
            if firstElement + secondElement + thirdElement < targetSum:
                start_index += 1
            elif firstElement + secondElement + thirdElement > targetSum:
                end_index -= 1
            else:
                finalArrayToBeReturned.append([firstElement,secondElement,thirdElement])
                start_index += 1
                end_index -= 1

# finding out the possible triplets for the given target out of the main array
# for example : given array as [12, 3, 1, 2, -6, 5, -8, 6]
# target sum as 0
# output to be [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]]
obj = Solutions()
print(obj.threeNumberSum([12, 3, 1, 2, -6, 5, -8, 6], 0))