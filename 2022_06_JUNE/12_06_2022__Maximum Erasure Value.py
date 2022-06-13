class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        
        N = len(nums)
        
        prefixSum = [0 for _ in range(N+1)]
        
        currentSum = 0
        for i in range(N):
            currentSum += nums[i]
            prefixSum[i] = currentSum
            
        lookUp = {}
        lastIndex = 0
        currentSum = 0
        maxSum = 0
        for i in range(N):
            if nums[i] in lookUp:
                lastIndex = max(lookUp[ nums[i] ] + 1, lastIndex)
            
            lookUp[nums[i]] = i
            currentSum = prefixSum[i] - prefixSum[lastIndex-1]
            maxSum = max(currentSum, maxSum)
            
        return maxSum