def find_xmas(word_search):
    rows = len(word_search)
    cols = len(word_search[0])
    
    directions = [
        (0, 1),
        (0, -1),
        (1, 0),
        (-1, 0),
        (1, 1),
        (-1, -1),
        (1, -1),
        (-1, 1),
    ]
    
    def check_word(x, y, dx, dy):
        word = "XMAS"
        for i in range(len(word)):
            new_x = x + i * dx
            new_y = y + i * dy
            if not (0 <= new_x < rows and 0 <= new_y < cols):
                return False
            if word[i] != word_search[new_x][new_y]:
                return False
        return True

    count = 0
    for i in range(rows):
        for j in range(cols):
            for dx, dy in directions:
                if check_word(i, j, dx, dy):
                    count += 1
    
    return count

def read_input(file_path):
    with open(file_path, 'r') as file:
        word_search = [line.strip() for line in file.readlines()]
    return word_search

file_path = 'input.txt'
word_search = read_input(file_path)
print(find_xmas(word_search))
