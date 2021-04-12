class Solutions:
    def generateDocument(self,characters, document):
        # creating hashTables to store frequency of char
        hashTableForChar = {}
        for char in characters:
            if hashTableForChar.get(char) is not None:
                hashTableForChar[char] = hashTableForChar.get(char) + 1
            else:
                hashTableForChar[char] = 1

        # use frequencies to create doc and test
        for char in document:
            if hashTableForChar.get(char) is None:
                return False
            elif hashTableForChar[char] == 0:
                return False
            else:
                hashTableForChar[char] = hashTableForChar.get(char) - 1
        return True


obj = Solutions()
print(obj.generateDocument("aheaolabbhb","hello"))