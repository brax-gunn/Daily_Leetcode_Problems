class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
        currentIndex = 0
        runningSum = 0
        
        while currentIndex < len(nums):
            
            runningSum += nums[currentIndex]
            nums[currentIndex] = runningSum
            
            currentIndex += 1
            
        return nums