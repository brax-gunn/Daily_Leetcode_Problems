class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        
        MODULO = 10 ** 9 + 7
        
        horizontalCuts.append(0)
        horizontalCuts.append(h)
        
        verticalCuts.append(0)
        verticalCuts.append(w)
        
        horizontalCuts.sort()
        verticalCuts.sort()
        
        H = len(horizontalCuts)
        V = len(verticalCuts)
        
        maxHeightDiff = 0
        maxWidthDiff = 0
        
        for h in range(1, H):
            maxHeightDiff = max( maxHeightDiff, horizontalCuts[h]-horizontalCuts[h-1] )
            
        for w in range(1, V):
            maxWidthDiff = max( maxWidthDiff, verticalCuts[w]-verticalCuts[w-1] )
            
        return (maxHeightDiff * maxWidthDiff) % MODULO