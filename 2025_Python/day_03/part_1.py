with open("test_input.txt", "r") as f:
    banks = [line.strip() for line in f.readlines()]

# Brute force approach
max_joltage_total = 0

for bank in banks:
    combinations = []
    for i in range(len(bank)):
        for j in range(i+1, len(bank)):
            combinations.append(int(bank[i] + bank[j]))
    
    max_joltage_total += max(combinations)

print(max_joltage_total)