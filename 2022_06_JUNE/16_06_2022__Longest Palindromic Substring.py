class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        N = len(s)
        best = 0
        start = None
        
        for center in range(N):
            left = center
            right = center 
            
            while left >= 0 and right < N and s[left]==s[right]:
                
                L = right - left + 1
                if L > best:
                    best = L
                    start = left
                    
                left -= 1
                right += 1
        
    
        for center in range(N-1):
            left = center
            right = center + 1
            
            while left >= 0 and right < N and s[left]==s[right]:
                
                L = right - left + 1
                if L > best:
                    best = L
                    start = left
                    
                left -= 1
                right += 1
        return s[start:start+best]
            