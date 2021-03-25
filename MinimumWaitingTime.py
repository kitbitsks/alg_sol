class Solution:
    def minimumWaitingTime(self,queries):
        queries.sort()
        minimumWaitingTime = 0
        totalWaitingTime = 0
        for index in range(0,len(queries)-1):
            minimumWaitingTime += queries[index]
            totalWaitingTime += minimumWaitingTime
        return (totalWaitingTime)

obj = Solution()
print(obj.minimumWaitingTime([3,2,1,2,6]))


