class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        memoInorder = self.__populateInorderIndex(inorder)
        
        self.__preorderIndex = 0
        root = self.__createTree(preorder, memoInorder, 0, len(inorder)-1)
        return root
        
    def __populateInorderIndex(self, inorder):
        N = len(inorder)
        memoInorder = {}
        for i in range(N):
            memoInorder[ inorder[i] ] = i
        
        return memoInorder
    
    def __createTree(self, preorder, memoInorder, startIndex, endIndex):
        if startIndex > endIndex:
            return None
        
        tempNode = TreeNode( preorder[ self.__preorderIndex ] )
        inorderIndex = memoInorder[ preorder[ self.__preorderIndex ] ]
        self.__preorderIndex += 1 
        
        
        tempNode.left = self.__createTree(preorder, memoInorder, startIndex, inorderIndex-1)
        tempNode.right = self.__createTree(preorder, memoInorder, inorderIndex+1, endIndex)
        
        return tempNode