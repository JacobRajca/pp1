def identity_matrix(n):
    matrix = []
    i = 0
    while i < n:
        row = [1 if j == i else 0 for j in range(n)]
        matrix.append(row)
        i += 1
    return matrix

def display_matrix(matrix):
    """
    Display a 2D array (matrix) in rows and columns.
    """
    for row in matrix:
        print(row)

def main():
    # Display identity matrices with dimensions 3, 5, and 8
    dimensions = [3, 5, 8]

    for n in dimensions:
        print(f"Identity Matrix of size {n}:")
        matrix = identity_matrix(n)
        display_matrix(matrix)
        print("\n" + "="*20 + "\n")
        
if __name__ == "__main__":
    main()