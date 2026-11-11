class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        print(len(matrix))
        self.pre_mat = [[] for i in range(len(matrix))]
        print(self.pre_mat)
        for i in range(len(matrix)):
            pre_sm =0
            for j in range(len(matrix[i])):
                pre_sm+=matrix[i][j]
                self.pre_mat[i].append(pre_sm)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        result = 0
        for row in range(row1, row2+1):
            if col1 == 0:
                result+= self.pre_mat[row][col2]
            else:
                result+= self.pre_mat[row][col2]-self.pre_mat[row][col1-1]
        return result


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)