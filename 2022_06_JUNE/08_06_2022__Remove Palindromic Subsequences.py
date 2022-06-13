class Solution:
    def removePalindromeSub(self, s: str) -> int:
        startPointer = 0
        endPointer = len(s)-1
        
        while startPointer <= endPointer:
            if s[startPointer] != s[endPointer]:
                return 2
            startPointer += 1
            endPointer -= 1
        
        return 1