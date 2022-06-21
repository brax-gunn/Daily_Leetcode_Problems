from heapq import heappop, heappush, heapify 

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        
        N = len(heights)
        hSum = 0
        
        maxHeap = []
        heapify(maxHeap)
        
        ci = 0
        while ci < N-1:
            
            if heights[ci+1] > heights[ci]:
                hSum += (heights[ci+1]-heights[ci])
                heappush(maxHeap, -(heights[ci+1]-heights[ci]))
                
                while (hSum > bricks) and (ladders > 0):
                    hSum -= ( -heappop(maxHeap) )
                    ladders -= 1
                
                if (hSum > bricks) and (ladders == 0):
                    break
            
            ci += 1
        
        return ci
        
        

            