day = 13
input_fn = f"day{day:02d}_input.txt"

with open(input_fn) as f:
    data = f.read()




##################################################
# Part 1
##################################################

patterns = [pattern.split("\n") for pattern in data.split("\n\n")]

total = 0

for pattern in patterns:
    nrows = len(pattern)
    # print(f"nrows = {nrows}")
    # print(f"ncols = {ncols}")
    ncols = len(pattern[0])
    row_symmetry_found = False
    for row in range(nrows-1):
        # print(f"row = {row}")
        rows_to_check = min(row + 1, nrows - row - 1)
        # print(f"rows_to_check = {rows_to_check}")
        if pattern[row + 1 - rows_to_check:row + 1] == pattern[row + 1:row + 1 + rows_to_check][::-1]:
            # print(pattern[row + 1 - rows_to_check:row + 1])
            # print(pattern[row + 1:row + 1 + rows_to_check][::-1])
            row_symmetry_found = True
            total += (row + 1) * 100
            break
        
    col_symmetry_found = False
    for col in range(ncols-1):
        # print(f"col = {col}")
        cols_to_check = min(col + 1, ncols - col - 1)
        # print(f"cols_to_check = {cols_to_check}")
        if [row[col + 1 - cols_to_check:col + 1] for row in pattern] == [row[col + 1:col + 1 + cols_to_check][::-1] for row in pattern]:
            # print([row[col + 1 - cols_to_check:col + 1] for row in pattern])
            # print([row[col + 1:col + 1 + cols_to_check][::-1] for row in pattern])
            col_symmetry_found = True
            total += col + 1
            break
        

# 31877
print(f"Part 1 answer: {total}")


##################################################
# Part 2
##################################################


# 
print(f"Part 2 answer: {}")

