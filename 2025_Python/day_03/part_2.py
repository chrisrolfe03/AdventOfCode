with open("test_input.txt", "r") as f:
    banks = [line.strip() for line in f.readlines()]



def getMax(current_max, remaining_bank, nums_left):
    # Base case: return the final string created
    if nums_left == 0: 
        return current_max
    elif nums_left == len(remaining_bank):
        return current_max + remaining_bank
    
    max_indices = []
    max_value = -1
    for i in range(len(remaining_bank) - nums_left + 1):
        v = int(remaining_bank[i])
        if v > max_value:
            max_value = v
            max_indices = [i]
        elif v == max_value:
            max_indices.append(i)
    
    max_bank = -1
    for i in max_indices:
        bank = getMax(current_max + remaining_bank[i], remaining_bank[i+1:], nums_left - 1)
        max_bank = max(max_bank, int(bank))
    
    return str(max_bank)


    # loop through remaining_bank, check value at i, if it's == max_value then append to list, if > max_value, set max_indexes = new list with index only
    # now we have a list of indices - loop through whats there, call the function with the new values for each. Compare and return the highest returned value


num_digits = 12
max_joltage_total = 0

for bank in banks:
    max_joltage = getMax(current_max='', remaining_bank=bank, nums_left=num_digits)
    print(max_joltage)
    max_joltage_total += int(max_joltage)

print(f"\n = {max_joltage_total}")