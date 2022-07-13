from collections import deque, defaultdict

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if root is None:
            return []
        
        
        myQueue = deque()
        myQueue.append(root)
        
        levelOrderArr = []
        
        while len(myQueue) > 0:

            currentSize = len(myQueue)
            temp = []
            
            while currentSize > 0:
                
                topNode = myQueue.popleft()
                temp.append(topNode.val)
                
                if topNode.left != None:
                    myQueue.append(topNode.left)
            
                if topNode.right != None:
                    myQueue.append(topNode.right)
                
                currentSize -= 1
            
            
            levelOrderArr.append(temp)
            
        return levelOrderArr