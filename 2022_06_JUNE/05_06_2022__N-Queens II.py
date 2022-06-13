class Solution:
    def totalNQueens(self, n: int) -> int:
        self.n = n
        self.answer = 0
        
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
            self.answer+=1
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