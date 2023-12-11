with open('Lorem.txt','r') as file:
    lines = file.readlines()

    # Initialize a variable to keep track of the current line
    current_line = 0

    # Continue displaying lines until the end of the file
    while current_line < len(lines):
        # Display the next five lines
        for i in range(current_line, min(current_line + 5, len(lines))):
            print(lines[i].strip())

        # Wait for the Enter key to be pressed
        input("Press Enter to continue...")

        # Move to the next set of five lines
        current_line += 5