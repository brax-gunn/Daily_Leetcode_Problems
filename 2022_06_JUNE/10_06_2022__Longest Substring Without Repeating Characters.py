class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        currentIndex = 0
        n = len(s)
        
        memo = [-1 for i in range(127)]
        
        maxSize = 0
        position = -1
        
        while currentIndex < n:

            currentChar = s[currentIndex]
            
            position = max(position, memo[ord(currentChar)])
            maxSize = max(maxSize, currentIndex-position)
            
            memo[ord(currentChar)] = currentIndex
            currentIndex += 1

        # maxSize = max(maxSize, currentIndex-memo[ord(currentChar)])
        return maxSize
        