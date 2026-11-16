class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
       row = len(matrix)
       col = len(matrix)
       for i in range(0,row):
         for j in range(0,i+1):
             if i!=j:
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
       for i in range (0,row):
        j,k=0,col-1
        while j<k:
            matrix[i][j],matrix[i][k] = matrix[i][k],matrix[i][j]
            j=j+1
            k=k-1