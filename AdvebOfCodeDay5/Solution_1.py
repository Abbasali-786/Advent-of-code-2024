def parse_input(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    rules_section, updates_section = content.strip().split('\n\n')
    rules = [tuple(map(int, line.split('|'))) for line in rules_section.splitlines()]
    updates = [list(map(int, line.split(','))) for line in updates_section.splitlines()]
    return rules, updates

def is_update_valid(update, rules):
    for x, y in rules:
        if x in update and y in update:
            if update.index(x) > update.index(y):
                return False
    return True

def sum_middle_pages(file_path):
    rules, updates = parse_input(file_path)
    total = 0
    for pages in updates:
        if is_update_valid(pages, rules):
            middle_page = pages[len(pages) // 2]
            total += middle_page
    return total

file_path = 'input.txt'
result = sum_middle_pages(file_path)
print("Sum of middle pages:", result)

