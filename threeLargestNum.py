class Solution:
        def findThreeLargestNumbers(self,array):
                threeLargestArr = [None,None,None]
                for num in array:
                        self.threeLargestArr(threeLargestArr,num)
                return threeLargestArr

        def threeLargestArr(self, threeLargestArr, num):
                if threeLargestArr[2] is None or num > threeLargestArr[2]:
                        self.updateAndSwap(threeLargestArr, 2, num)
                elif threeLargestArr[1] is None or num > threeLargestArr[1]:
                        self.updateAndSwap(threeLargestArr, 1, num)
                elif threeLargestArr[0] is None or num > threeLargestArr[0]:
                        self.updateAndSwap(threeLargestArr,0, num)
                return threeLargestArr

        def updateAndSwap(self, array, index, num):
                for idx in range(index + 1):
                        if idx == index:
                                array[index] = num
                        else:
                                array[idx] = array[idx+1]
                return array
                

obj = Solution()
print(obj.findThreeLargestNumbers([6,8,1,22,21,90]))
