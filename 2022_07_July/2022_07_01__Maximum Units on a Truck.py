class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort( key = lambda boxType: boxType[1] )
        
        N = len(boxTypes)
        
        totalUnits = 0
        for i in range(N-1, -1, -1):
            unitsTaken = min(boxTypes[i][0], truckSize)
            totalUnits += ( unitsTaken * boxTypes[i][1] )
            truckSize -= unitsTaken
            if truckSize <= 0:
                break
        
        return totalUnits