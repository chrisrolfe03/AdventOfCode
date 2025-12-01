with open("test_input.txt", "r") as f:
    moves = f.readlines()

list_len = 100
safe_pos = 50
num_zero = 0

for move in moves:
    move = move.strip()
    dir = move[0]
    num = int(move[1:])
    print(move)

    extra_zeroes = num // list_len
    remaining_num = num % list_len

    if dir == "L":
        remaining_num *= -1

    prev_safe_pos = safe_pos
    safe_pos += remaining_num

    if prev_safe_pos != 0 and (safe_pos <= 0 or safe_pos >= list_len):
        extra_zeroes += 1

    safe_pos %= list_len
    num_zero += extra_zeroes

print(num_zero)