# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = [0]
        self.__dfs(root, float("-inf"), count)
        return count[0]
    
    def __dfs(self, root, currentMax, count):
        
        if root is None:
            return
        
        if root.val >= currentMax:
            count[0] += 1
            currentMax = max(currentMax, root.val)
        
        self.__dfs(root.left, currentMax, count)
        self.__dfs(root.right, currentMax, count)
        
        return
        