# Comment out any solution to run the other #

import unittest
# Solution 1 #
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def nodeDepths(self,root):
        currentNode = root
        parentLevel = 0
        totalLen = 0
        currentLevelArray = []
        if currentNode.left is not None:
            self.calculateLengthOfNodes(currentNode.left, currentLevelArray, parentLevel+1)
        if currentNode.right is not None:
            self.calculateLengthOfNodes(currentNode.right,currentLevelArray, parentLevel+1)
        finalRes = 0
        for sum in currentLevelArray:
            finalRes+=sum
        return finalRes

    def calculateLengthOfNodes(self, node,currentLevelArray, currentLevel):
        currentLevelArray.append(currentLevel)
        if node is None:
            return
        if node.left is not None:
            self.calculateLengthOfNodes(node.left,currentLevelArray,currentLevel+1)
        if node.right is not None:
            self.calculateLengthOfNodes(node.right,currentLevelArray, currentLevel+1)	

# Solution 2 #
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def nodeDepths(self,root, depth = 0):
        if root is None:
            return 0
        return depth + self.nodeDepths(root.left, depth + 1) + self.nodeDepths(root.right, depth + 1)

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        root = BinaryTree(1)
        root.left = BinaryTree(2)
        root.left.left = BinaryTree(4)
        root.left.left.left = BinaryTree(8)
        root.left.left.right = BinaryTree(9)
        root.left.right = BinaryTree(5)
        root.right = BinaryTree(3)
        root.right.left = BinaryTree(6)
        root.right.right = BinaryTree(7)
        objectForBin = BinaryTree(root)
        actual = objectForBin.nodeDepths(root)
        # print(actual)
        try:
            # make it fail by passing any wrong value
            self.assertEqual(actual, 16)
            print("Test Successfull. Expected matches with Actual !")
        except Exception as e:
            print("Test case failed !")
            print(e)
        
        
        

obj = TestProgram()
obj.test_case_1()        