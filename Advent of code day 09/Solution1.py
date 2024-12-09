filename = "input.txt"

# Read data from file
data = open(filename).read().strip().split("\n")

# Make sure that the sequence contains only valid digits
sequence = data[0]

# Check if the sequence contains only digits
if not sequence.isdigit():
    raise ValueError("Input sequence contains invalid characters. Only digits are allowed.")

configurations = []
arrangement = []
current_file = 0

# Process the sequence of digits, alternating between file lengths and free space lengths
for index, character in enumerate(sequence):
    try:
        block_length = int(character)  # Convert character to block length
    except ValueError:
        raise ValueError(f"Invalid character '{character}' found at position {index}. Only digits are allowed.")
    
    if index % 2 == 0:
        # Add file blocks, using current_file as the file ID
        arrangement.extend([str(current_file)] * block_length)
        current_file += 1
    else:
        # Add free space blocks ('.')
        arrangement.extend(["."] * block_length)

# Now we simulate the file compaction process
while True:
    try:
        empty_position = arrangement.index(".")
    except ValueError:
        # No empty space left
        break

    # Check if there is any non-empty space to the right
    right_side_empty = any(ch != "." for ch in arrangement[empty_position + 1:])
    if not right_side_empty:
        break

    # Move the last non-empty block to the empty position
    for reverse_index in range(len(arrangement) - 1, -1, -1):
        if arrangement[reverse_index] != ".":
            arrangement[empty_position], arrangement[reverse_index] = arrangement[reverse_index], "."
            break

# Calculate the total score (checksum)
total_score = 0
for index, file_marker in enumerate(arrangement):
    if file_marker != ".":
        total_score += index * int(file_marker)

# Print the result (checksum)
print(total_score)
