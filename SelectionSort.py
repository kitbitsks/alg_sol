class Solutions:
    def selectionSort(self, array):
        for index in range(len(array)):
            IndexToBeSwapped = self.findMinimumIndex(index,array)
            self.swapNumbers(index, IndexToBeSwapped,array)
        return array

    def findMinimumIndex(self, fromIndex, array):
        minimum = array[fromIndex]
        indexToBeReturned = fromIndex
        for index in range(fromIndex+1,len(array)):
            if array[index] < minimum:
                indexToBeReturned = index
                minimum = array[index]
        return indexToBeReturned

    def swapNumbers(self, i,j, array):
        array[i] , array[j] = array[j], array[i]




obj = Solutions()
print(obj.selectionSort([9,45,12,34,32,11,7]))
