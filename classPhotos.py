class Solution:
    def classPhotos(self,redShirtHeights, blueShirtHeights):
        redShirtHeights.sort()
        blueShirtHeights.sort()
        frontRow = []
        backRow = []
        if (redShirtHeights[len(redShirtHeights)-1] < blueShirtHeights[len(blueShirtHeights)-1]):
            frontRow = redShirtHeights
            backRow = blueShirtHeights
        else:
            frontRow = blueShirtHeights
            backRow = redShirtHeights
        for index in range(len(frontRow)):
            if frontRow[index] >= backRow[index]:
                return False 
        return True
    
# Testing
redShirt = [5,8,1,3,4]
blueShirt = [6,9,2,4,5]
object = Solution()
print(object.classPhotos(redShirt,blueShirt))
