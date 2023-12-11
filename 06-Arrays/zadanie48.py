def create_2d_arr(x, y):
    # Create a 2D array with dimensions x by y and initialize all values to 0
    return [[0 for _ in range(y)] for _ in range(x)]

def display_2d_arr(arr):
    # Display the contents of the 2D array
    for row in arr:
        print(row)

# Create a 3x5 array
array_3x5 = create_2d_arr(3, 5)

# Display the created array
print("Created 3x5 Array:")
display_2d_arr(array_3x5)