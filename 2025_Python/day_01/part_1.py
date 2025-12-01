with open("test_input.txt", "r") as f:
    moves = f.readlines()

list_len = 100
safe_pos = 50
num_zero = 0

for move in moves:
    move = move.strip()
    dir = move[0]
    num = int(move[1:])

    if dir == "L":
        num *= -1

    safe_pos = (safe_pos + num) % list_len
    
    if safe_pos == 0:
        num_zero += 1

print(num_zero)