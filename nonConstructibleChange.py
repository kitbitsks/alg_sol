class Solution:
    def nonConstructibleChange(self,coins):
        coins.sort()
        if coins[0] != 1:
            return 1
        minChangeCanBeCreated = 0
        for coin in coins:
            if coin <= minChangeCanBeCreated+1:
                minChangeCanBeCreated += coin
            else:
                break
        return (minChangeCanBeCreated + 1)


Obj = Solution()
print(Obj.nonConstructibleChange([1,1,3]))
