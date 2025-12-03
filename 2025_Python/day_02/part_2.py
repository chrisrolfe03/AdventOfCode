with open("test_input.txt", "r") as f:
    ranges = f.read().split(",")

def isInvalid(id):
    # I hate all this code but it somehow works!

    base = ''
    matches_idx = [i for i in range(len(id))]

    for i in range(len(id)):
        base += id[i]

        #print(f"Loop #{i} | Base: {base} | Matches: {matches_idx}")
        
        new_matches_idx = []
        for match_idx in matches_idx:

            if match_idx > i:
                possible_match = id[match_idx:match_idx+i+1]
                
                if possible_match == base:
                    new_matches_idx.append(match_idx)

                    if len(id) % len(possible_match) == 0:
                        div = len(id) // len(possible_match)
                        full_attempt = possible_match * div
                        if full_attempt == id:

                            print(f"Full attempt = {full_attempt}")
                            return True

        matches_idx = new_matches_idx
                   
        if len(matches_idx) == 0:
            return False


invalid_ids = []
for num_range in ranges:
    start, end = num_range.split("-")
    for id in range(int(start), int(end) + 1):
        if isInvalid(str(id)):
            invalid_ids.append(id)

print(sum(invalid_ids))