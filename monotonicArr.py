class Solutions:
    def isMonotonic(self,array):
        isNonDecreasing = True
        isNonIncreasing = True
        for idx in range(1,len(array)):
            if array[idx] < array[idx - 1]:
                isNonIncreasing = False
            if array[idx] > array[idx - 1]:
                isNonDecreasing = False  

        return isNonDecreasing or isNonIncreasing
        
obj = Solutions()

print(obj.isMonotonic([1,2,3,4,5,1]))
