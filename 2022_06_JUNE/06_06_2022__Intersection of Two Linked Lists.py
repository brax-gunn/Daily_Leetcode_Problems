# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        memo = {}
        
        currentNode = headA
        while currentNode is not None:
            memo[currentNode] = 1
            currentNode = currentNode.next
        
        currentNode = headB
        while currentNode is not None:
            if currentNode in memo:
                return currentNode
            currentNode = currentNode.next
        
        return None
        
        