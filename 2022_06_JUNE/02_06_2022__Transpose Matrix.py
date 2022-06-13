class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        
        newMatrix = []
        for col in range(0, len(matrix[0])):
            temp = []
            for row in range(0, len(matrix)):
                temp.append(matrix[row][col])
            newMatrix.append(temp)
            
        return newMatrix