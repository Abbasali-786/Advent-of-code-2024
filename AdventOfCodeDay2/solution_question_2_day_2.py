def is_safe_report(report):
    for i in range(len(report) - 1):
        diff = abs(report[i] - report[i + 1])
        if diff < 1 or diff > 3:
            return False
    
    increasing = all(report[i] <= report[i + 1] for i in range(len(report) - 1))
    decreasing = all(report[i] >= report[i + 1] for i in range(len(report) - 1))
    
    return increasing or decreasing

def is_safe_with_one_removal(report):
    for i in range(len(report)):
        new_report = report[:i] + report[i+1:]
        if is_safe_report(new_report):
            return True
    return False

safe_count = 0

with open("inputd2q2.txt", "r") as file:
    for line in file:
        report = list(map(int, line.split()))
        
        if is_safe_report(report):
            safe_count += 1
        elif is_safe_with_one_removal(report):
            safe_count += 1

print(f"Safe count : {safe_count}")
