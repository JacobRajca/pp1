def transpose_matrix(m):
    # Use the zip function to transpose the matrix
    transposed = list(zip(*m))
    
    # Convert the transposed result back to a list of lists
    transposed_matrix = [list(row) for row in transposed]
    
    return transposed_matrix

# Example usage:
matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix2 = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 0]
]

matrix3 = [
    [5,6,7,8]
]

result1 = transpose_matrix(matrix1)
result2 = transpose_matrix(matrix2)
result3 = transpose_matrix(matrix3)

for row in result1:
    for element in row:
        print(element,end=' ')
    print('')

for row in result2:
    for element in row:
        print(element,end=' ')
    print('')

for row in result3:
    for element in row:
        print(element,end=' ')
    print('')