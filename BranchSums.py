class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Solution:
    def branchSums(self,root):
        sums = []
        self.calculateBranchSums(root,0,sums)
        return sums

    def calculateBranchSums(self, node, runningSum, sums):
        # if left or right node of node is None then do not perform any operation
        if node is None:
            return

        # calculate new sum of every k level by adding previous k level sum with current node.value
        newSum = runningSum + node.value
    
        # if reached leaf node then append that branch sum to array
        if node.left is None and node.right is None:
            sums.append(newSum)
    
        # recursively call each branch of node
        self.calculateBranchSums(node.left, newSum, sums)
        self.calculateBranchSums(node.right, newSum, sums)
