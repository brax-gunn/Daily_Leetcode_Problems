class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        R = len(triangle)
        cache = [[0 for i in range(R)] for j in range(R)]
        
        ci = 0
        for i in range(R):
            for j in range(0, i+1):
                cache[i][j] = triangle[i][j]
        
        # print(cache)
        cr = R-2
        while cr >= 0:
            cc = R-2
            while cc >= 0:
                cache[cr][cc] = cache[cr][cc] + min(cache[cr+1][cc], cache[cr+1][cc+1])
                cc -= 1
            cr -= 1
        
        return cache[0][0]