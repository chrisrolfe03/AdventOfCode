with open("test_input.txt", "r") as f:
    ranges = f.read().split(",")

def isInvalid(id):
    id_length = len(id)
    if id_length % 2 == 0:
        idx = int(id_length / 2)
        first, second = id[:idx], id[idx:]
        if first == second:
            return True
    return False

invalid_ids = []

for num_range in ranges:
    start, end = num_range.split("-")
    for id in range(int(start), int(end) + 1):
        if isInvalid(str(id)):
            invalid_ids.append(id)

print(sum(invalid_ids))