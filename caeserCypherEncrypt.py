class Solutions:
    def caesarCipherEncryptor(self,string, key):
        key = key % 26
        calculatedString = ""
        for elem in string:
            calculatedAscii = ord(elem) + key
            if calculatedAscii <= 122:
                calculatedString += chr(calculatedAscii)
            else:
                calculatedString += chr(96 + (calculatedAscii % 122))
        return calculatedString

    


obj = Solutions()
print(obj.caesarCipherEncryptor("xyz",2))