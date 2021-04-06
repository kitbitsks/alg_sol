class Solutions:
    def bubbleSort(self, array):
        for i in range(len(array)):
            for j in range(len(array)-(i)-1):
                if array[j] > array[j+1]:
                    temp = array[j]
                    array[j] = array[j+1]
                    array[j+1] = temp
        return array





obj = Solutions()
print(obj.bubbleSort([23,21,34,212]))