def isPalindrome(string):
    reverseString = string[::-1]
	if reverseString == string:
		return True
	else:
		return False


def isPalindrome(string):
	leftIndex = 0
	rightIndex = len(string) -1
	while leftIndex <= rightIndex:
		if string[leftIndex] != string[rightIndex]:
			return False
		leftIndex += 1
		rightIndex -= 1
	return True
