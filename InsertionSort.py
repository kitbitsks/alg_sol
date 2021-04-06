class Solutions:
    def insertionSort(self, array):
        for j in range(1,len(array)):
            while j>0 and array[j] < array[j-1]:
                self.swapElementsInArray(j,j-1,array)
                j -= 1
        return array

    def swapElementsInArray(self, i, j, array):
        array[i] , array[j] = array[j], array[i]


obj = Solutions()
print(obj.insertionSort([23,43,12,22,11,10]))