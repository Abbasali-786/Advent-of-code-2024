import re

def extract_and_evaluate_mul_expressions(text):
    pattern = r"mul\((\d+),(\d+)\)"
    matches = re.findall(pattern, text)
    results = []
    total_sum = 0
    
    for match in matches:
        a, b = int(match[0]), int(match[1])
        result = a * b
        results.append((a, b, result))
        total_sum += result
    
    return results, total_sum

with open('inputd3q1.txt', 'r') as file:
    input_text = file.read()

results, total_sum = extract_and_evaluate_mul_expressions(input_text)

for a, b, result in results:
    print(f"mul({a}, {b}) = {result}")

print(f"Total sum of all products: {total_sum}")
