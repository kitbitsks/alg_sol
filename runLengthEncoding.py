class Solutions:
    def runLengthEncoding(self,string):
        countOfChar = 1
        currentChar = string[0]
        resultantString = ""
        for index in range(1,len(string)):
            if (currentChar == string[index]):
                countOfChar += 1
            else:
                resultantString += self.calculateString(currentChar,countOfChar)
                currentChar = string[index]
                countOfChar = 1
        resultantString += self.calculateString(currentChar,countOfChar)
        return resultantString

    def calculateString(self,currentChar,countOfChar):
        dividedValue = countOfChar//9
        moduloValue = countOfChar%9
        calculatedString = ""
        for i in range(dividedValue):
            calculatedString += str(9) + currentChar
            print(calculatedString)
        if moduloValue != 0:
            calculatedString += str(moduloValue) + currentChar
        return calculatedString

obj = Solutions()
print(obj.runLengthEncoding("A"))