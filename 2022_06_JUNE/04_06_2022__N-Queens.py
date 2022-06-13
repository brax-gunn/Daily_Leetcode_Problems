class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.n = n
        self.answer = []
        
        chessBoard = []
        for i in range(0, self.n):
            temp = []
            for j in range(0 , self.n):
                temp.append('.')
            chessBoard.append(temp)
        
        self.recursionOnBoard(0, chessBoard)
        
        return self.answer
        
    def recursionOnBoard(self, currentRow, chessBoard):
        if currentRow >= self.n:
            temp = []
            for row in range(0, self.n):
                tempStr = ''
                for col in range(0, self.n):
                    tempStr+=chessBoard[row][col]
                temp.append(tempStr)
                    
            self.answer.append(temp.copy())
            return
        
        
        for col in range(0, self.n):
            if self.isPosValid(currentRow, col, chessBoard):
                chessBoard[currentRow][col] = 'Q'
                self.recursionOnBoard(currentRow+1, chessBoard)
                chessBoard[currentRow][col] = '.'
                
        return

    def isPosValid(self, currentRow, currentCol, chessBoard):
        # check in row
        for pos in range(0, self.n):
            if chessBoard[currentRow][pos] == 'Q':
                return False
        # check in column
        for pos in range(0, self.n):
            if chessBoard[pos][currentCol] == 'Q':
                return False
        # for diagonal top left
        currentX = currentRow
        currentY = currentCol
        while currentX >= 0 and currentY >= 0:
            if chessBoard[currentX][currentY] == 'Q':
                return False
            currentX -= 1
            currentY -= 1
        # for diagonal top right
        currentX = currentRow
        currentY = currentCol
        while currentX >= 0 and currentY < self.n:
            if chessBoard[currentX][currentY] == 'Q':
                return False
            currentX -= 1
            currentY += 1
        # for diagonal bottom left
        currentX = currentRow
        currentY = currentCol
        while currentX < self.n and currentY >= 0:
            if chessBoard[currentX][currentY] == 'Q':
                return False
            currentX += 1
            currentY -= 1
        # for diagonal bottom right
        currentX = currentRow
        currentY = currentCol
        while currentX < self.n and currentY < self.n:
            if chessBoard[currentX][currentY] == 'Q':
                return False
            currentX += 1
            currentY += 1
        
        return True