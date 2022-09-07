# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        return self.__traversal(root, "")
    
    def __traversal(self, root, myStr):
        
        if root is None:
            return ""
        
        left = self.__traversal(root.left, myStr)
        right = self.__traversal(root.right, myStr)
        
        if left != "" and right != "":
            return str(root.val) + "(" + left + ")" + "(" + right + ")"
        elif left == "" and right != "":
            return str(root.val) + "(" + left + ")" + "(" + right + ")"
        elif left != "" and right == "":
            return str(root.val) + "(" + left + ")"
        else:
            return str(root.val)
        
        
        