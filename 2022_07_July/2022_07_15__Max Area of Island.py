class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        maxIsland = 0
        
        m = len(grid)
        n = len(grid[0])
        
        
        for row in range(0, m):
            for col in range(0, n):
                if grid[row][col] == 1:
                    maxIsland = max(maxIsland, self.__neutralizeIsland(row, col, grid, {}))
                    
        return maxIsland
        
    def __neutralizeIsland(self, currentRow, currentCol, grid, visitedArray):
        
        if currentRow < 0 or currentRow >= len(grid) or currentCol < 0 or currentCol >= len(grid[0]):
            return 0
        
        
        if (currentRow, currentCol) in visitedArray:
            return 0
        
        visitedArray[(currentRow, currentCol)] = True
        
        if grid[currentRow][currentCol] != 1:
            return 0
        
        grid[currentRow][currentCol] = 0
        
        # move up
        a = self.__neutralizeIsland(currentRow-1, currentCol, grid, visitedArray)

        # move right
        b = self.__neutralizeIsland(currentRow, currentCol+1, grid, visitedArray)

        # move down
        c = self.__neutralizeIsland(currentRow+1, currentCol, grid, visitedArray)

        # move left
        d = self.__neutralizeIsland(currentRow, currentCol-1, grid, visitedArray)
        
        return 1 + a + b + c + d