class Solution:
    def tournamentWinner(self,competitions, results):
        # Write your code here.
        resultHashTable = {}
        for index in range(len(competitions)):
            if results[index] == 0:
                try:
                    resultHashTable[competitions[index][1]] += 3
                except:
                    resultHashTable[competitions[index][1]] = 3
            else:
                try:
                    resultHashTable[competitions[index][0]] += 3
                except:
                    resultHashTable[competitions[index][0]] = 3
        return max(resultHashTable,key=resultHashTable.get)

Obj = Solution()
print(Obj.tournamentWinner([["Html","C#"],["C#","Python"],["Python","Html"]],[0,0,1]))