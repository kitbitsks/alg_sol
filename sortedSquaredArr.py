# Time : O(n) , Space : O(n)
class Solutions:
    def sortedSquaredArray(self, array):
        sortedArray = []
        sortedArray = [0 for _ in array]
        leftMostElem = 0
        rightMostElem = len(array)-1
        for idx in range(len(array)):
            if abs(array[leftMostElem]) > abs(array[rightMostElem]):
                sortedArray[(len(array)-1)-idx] = array[leftMostElem] * array[leftMostElem]
                leftMostElem += 1
            else:
                print((len(array)-1)-idx)
                sortedArray[(len(array)-1)-idx] = array[rightMostElem] * array[rightMostElem]
                rightMostElem -= 1
        return sortedArray

            



obj = Solutions()
print(obj.sortedSquaredArray([-2,-1,0,1,2]))