class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        startPointer = 0
        endPointer = len(numbers)-1
        
        while startPointer < endPointer:
            if numbers[startPointer] + numbers[endPointer] < target:
                startPointer += 1
            elif numbers[startPointer] + numbers[endPointer] > target:
                endPointer -= 1
            else:
                return [startPointer+1, endPointer+1]
            
        return -1
        