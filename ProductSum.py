class Solution:
    def productSum(array, level=1):
        sum = 0
        for element in array:
            if type(element) is list:
                sum+= productSum(element, level+1)
            else:
                sum+=element
        return sum * level
