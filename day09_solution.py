from itertools import pairwise

day = 9
input_fn = f"day{day:02d}_input.txt"

with open(input_fn) as f:
    data = f.readlines()

data = [[int(num) for num in row.replace("\n", "").split(" ")] for row in data]




##################################################
# Part 1
##################################################



history = []
for row in data:
    values = [row]
    current_row = row
    all_zeros = False
    while not all_zeros:
        current_row = [y - x for (x, y) in pairwise(current_row)]
        values.append(current_row)
        all_zeros = all(x == 0 for x in current_row)

    # Need to do diffs of all but the 0s I added on
    for i in range(len(values) - 2, -1, -1):
        values[i] = values[i] + [values[i][-1] + values[i + 1][-1]]
    history.append(values[0][-1])

# 1798691765
print(f"Part 1 answer: {sum(history)}")


##################################################
# Part 2
##################################################


history = []
for row in data:
    values = [row]
    current_row = row
    all_zeros = False
    while not all_zeros:
        current_row = [y - x for (x, y) in pairwise(current_row)]
        values.append(current_row)
        all_zeros = all(x == 0 for x in current_row)

    # Need to do diffs of all but the 0s I added on
    for i in range(len(values) - 2, -1, -1):
        values[i] = [values[i][0] - values[i + 1][0]] + values[i]
    history.append(values[0][0])

# 1104
print(f"Part 2 answer: {sum(history)}")


