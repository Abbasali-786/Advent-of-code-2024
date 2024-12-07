import itertools

def evaluate_expression(numbers, operators):
    """Evaluate the expression left to right given numbers and operators."""
    result = numbers[0]
    for i in range(len(operators)):
        if operators[i] == '+':
            result += numbers[i + 1]
        elif operators[i] == '*':
            result *= numbers[i + 1]
        elif operators[i] == '||':
            # Concatenate numbers as strings and convert to integer
            result = int(str(result) + str(numbers[i + 1]))
    return result

def process_input(file_path):
    """Process the input file and return the test values that are valid."""
    valid_test_values = []
    
    with open(file_path, 'r') as file:
        for line in file:
            # Parse the line into test value and numbers
            test_value_str, numbers_str = line.split(':')
            test_value = int(test_value_str.strip())
            numbers = list(map(int, numbers_str.strip().split()))
            
            # Generate all possible combinations of operators (+, *, ||)
            operator_combinations = itertools.product(['+', '*', '||'], repeat=len(numbers) - 1)
            
            # Check if any combination of operators makes the equation valid
            for operators in operator_combinations:
                if evaluate_expression(numbers, operators) == test_value:
                    valid_test_values.append(test_value)
                    break  # We only need one valid combination to count this test value
    
    return valid_test_values

def main():
    file_path = 'input.txt'  # Input file path
    valid_test_values = process_input(file_path)
    total = sum(valid_test_values)
    print(f"Total sum of valid test values: {total}")

if __name__ == "__main__":
    main()
