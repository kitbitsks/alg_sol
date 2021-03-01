
class Solve:
    
    def isValidSubsequence(self,array, sequence):
        # via while loop
        arrayIndex = 0
        sequenceIndex = 0
        while (arrayIndex < len(array)  and sequenceIndex <len(sequence)):
            if sequence[sequenceIndex] == array[arrayIndex]:
                sequenceIndex += 1
            arrayIndex += 1
        return sequenceIndex == (len(sequence))

        # via for loop
        sequenceIndex = 0
        for element in array:
            print(sequenceIndex)
            if sequenceIndex == len(sequence):
                break            
            if element == sequence[sequenceIndex]:
                sequenceIndex += 1
        return len(sequence) == sequenceIndex



