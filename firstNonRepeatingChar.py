class Solutions:
    def firstNonRepeatingCharacter(self,string):
        hashMapToStoreCharsCount = {}
        for character in string:
            if hashMapToStoreCharsCount.get(character) is not None:
                hashMapToStoreCharsCount[character] = hashMapToStoreCharsCount.get(character)+1
            else:
                hashMapToStoreCharsCount[character] = 1
        
        for idx in range(len(string)):
            character = string[idx]
            if hashMapToStoreCharsCount[character]==1:
                return idx
        return -1

obj = Solutions()
print(obj.firstNonRepeatingCharacter(['b','b','c','d']))