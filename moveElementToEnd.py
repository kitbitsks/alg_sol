class Solutions:
    def moveElementToEnd(self,array, toMove):
        i = 0
        j = len(array) - 1
        while i < j:
            while i < j and array[j] == toMove:
                j -= 1
            if array[i] == toMove:
                array[i], array[j] = array[j],array[i]
            i+=1
        return array

obj = Solutions()
print(obj.moveElementToEnd([2,1,3,4,2],2))