def count_x_mas_patterns(grid):
    rows, cols = len(grid), len(grid[0])
    count = 0

    def check_diagonal(r, c, dr1, dc1, dr2, dc2):
        try:
            if (grid[r + dr1][c + dc1] == 'M' and
                grid[r][c] == 'A' and
                grid[r + dr2][c + dc2] == 'S'):
                return True
            if (grid[r + dr1][c + dc1] == 'S' and
                grid[r][c] == 'A' and
                grid[r + dr2][c + dc2] == 'M'):
                return True
        except IndexError:
            pass
        return False

    for r in range(1, rows - 1):
        for c in range(1, cols - 1):
            if grid[r][c] == 'A':
                if (check_diagonal(r, c, -1, -1, 1, 1) and
                    check_diagonal(r, c, -1, 1, 1, -1)):
                    count += 1

    return count


with open('input.txt', 'r') as file:
    grid = [line.strip() for line in file.readlines()]

result = count_x_mas_patterns(grid)
print(result)
