import re

def extract_and_evaluate_mul_expressions_with_conditions(text):
    pattern_mul = r"mul\((\d+),(\d+)\)"
    pattern_do = r"do\(\)"
    pattern_dont = r"don't\(\)"
    results = []
    total_sum = 0
    mul_enabled = True
    tokens = re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", text)
    
    for token in tokens:
        if token == "do()":
            mul_enabled = True
        elif token == "don't()":
            mul_enabled = False
        elif mul_enabled and token.startswith("mul("):
            match = re.match(pattern_mul, token)
            if match:
                a, b = int(match.group(1)), int(match.group(2))
                result = a * b
                results.append((a, b, result))
                total_sum += result
    
    return results, total_sum

with open('inputd3q2.txt', 'r') as file:
    input_text = file.read()

results, total_sum = extract_and_evaluate_mul_expressions_with_conditions(input_text)

for a, b, result in results:
    print(f"mul({a}, {b}) = {result}")

print(f"Total sum of all products: {total_sum}")
