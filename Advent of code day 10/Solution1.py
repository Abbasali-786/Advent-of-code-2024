from collections import deque

# Directions for moving up, down, left, and right
DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# Function to check if a position is valid (inside the map and not a wall)
def is_valid(x, y, rows, cols):
    return 0 <= x < rows and 0 <= y < cols

# Function to perform a BFS search from a given trailhead to count reachable '9' positions
def bfs(map_data, start_x, start_y, rows, cols):
    queue = deque([(start_x, start_y)])
    visited = set([(start_x, start_y)])
    count_nines = 0
    
    while queue:
        x, y = queue.popleft()
        
        # If we reach a '9', increase the count
        if map_data[x][y] == 9:
            count_nines += 1
        
        # Explore neighbors (up, down, left, right)
        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny, rows, cols) and (nx, ny) not in visited:
                if map_data[nx][ny] == map_data[x][y] + 1:
                    queue.append((nx, ny))
                    visited.add((nx, ny))
    
    return count_nines

# Main function to process the input and calculate the result
def main():
    # Read the input from the file
    with open("input.txt") as file:
        map_data = [list(map(int, line.strip())) for line in file.readlines()]
    
    rows = len(map_data)
    cols = len(map_data[0])
    total_score = 0
    
    # Loop through the map and find all trailheads (positions with height 0)
    for i in range(rows):
        for j in range(cols):
            if map_data[i][j] == 0:
                # Perform BFS from each trailhead and add the score
                score = bfs(map_data, i, j, rows, cols)
                total_score += score
    
    print("Total score of all trailheads:", total_score)

# Run the main function
if __name__ == "__main__":
    main()
