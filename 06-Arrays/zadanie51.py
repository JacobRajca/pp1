def display_array(arr):
    for row in arr:
        print(" ".join(map(str, row)))

def swap_first_and_last_row(arr):
    arr[0], arr[-1] = arr[-1], arr[0]

# Create a 3x5 array with integer numbers
array_2d = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15]
]

# Display the array before swapping
print("Array before swapping:")
display_array(array_2d)

# Swap the first and last row
swap_first_and_last_row(array_2d)

# Display the array after swapping
print("\nArray after swapping:")
display_array(array_2d)