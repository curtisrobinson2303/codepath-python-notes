# I - Inputs
    # 2d matrix of nxn 

# O  - Output
    # 2d matrix of nxn size with rows and columns transposed
  
# C - Constraints/considerations
    # Check its size greater than 1
    # Check row and column length for traspose target

# E - Edge Cases
    # None other

def transpose(matrix): 
    row = len(matrix)
    col = len(matrix[0])

    resultMatrix = [[0]*row for _ in range(col)]
    # resultMatrix = [[0,0,0],[0,0,0],[0,0,0]]

    print(resultMatrix)

    for i in range(row):
        for j in range(col):
           resultMatrix[j][i] = matrix[i][j]

    print(resultMatrix)

    return resultMatrix

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix)

transpose(matrix)
