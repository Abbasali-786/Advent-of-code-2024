def is_safe_report(report):
    for i in range(len(report) - 1):
        diff = abs(report[i] - report[i + 1])
        if diff < 1 or diff > 3:
            return False
    
    increasing = all(report[i] <= report[i + 1] for i in range(len(report) - 1))
    decreasing = all(report[i] >= report[i + 1] for i in range(len(report) - 1))
    
    return increasing or decreasing

safe_count = 0

with open("input.txt", "r") as file:
    for line in file:
        report = list(map(int, line.split()))
        
        if is_safe_report(report):
            safe_count += 1

print(f"Safe count : {safe_count}")
