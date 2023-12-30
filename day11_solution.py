import numpy as np

day = 11
input_fn = f"day{day:02d}_input.txt"

with open(input_fn) as f:
    data = f.readlines()

data = [row.replace("\n", "") for row in data]
nrows = len(data)
ncols = len(data[0])

# Initialize to all . and then fill in #
data_array = np.full((nrows, ncols), ".")

galaxy_rows = set()
galaxy_cols = set()
galaxy_positions = []

for row in range(nrows):
    for col in range(ncols):
        if data[row][col] == "#":
            data_array[row, col] = "#"
            galaxy_rows.add(row)
            galaxy_cols.add(col)
            galaxy_positions.append((row, col))

no_galaxy_rows = set(range(nrows)).difference(galaxy_rows)
no_galaxy_cols = set(range(ncols)).difference(galaxy_cols)


# We don't need to expand the data frame to find the distance, we can just figure out
# how much the expansion would impact the count while counting
def find_distance(row1, col1, row2, col2, extra_row_multiplier = 1):
    if row1 <= row2:
        min_row, max_row = row1, row2
    else:
        min_row, max_row = row2, row1

    if col1 <= col2:
        min_col, max_col = col1, col2
    else:
        min_col, max_col = col2, col1

    pre_expansion_distance = max_row - min_row + max_col - min_col
    num_extra_rows = len(set(range(min_row, max_row)).intersection(no_galaxy_rows)) * extra_row_multiplier
    num_extra_cols = len(set(range(min_col, max_col)).intersection(no_galaxy_cols)) * extra_row_multiplier
    return pre_expansion_distance + num_extra_rows + num_extra_cols



##################################################
# Part 1
##################################################

total_distance = 0
for galaxy_position1 in galaxy_positions:
    for galaxy_position2 in galaxy_positions:
        # Only add distance for each pair once
        if (galaxy_position1[0] < galaxy_position2[0]) or (galaxy_position1[0] == galaxy_position2[0] and (galaxy_position1[1] < galaxy_position2[1])):
            distance = find_distance(*galaxy_position1, *galaxy_position2)
            total_distance += distance


# 9769724
print(f"Part 1 answer: {total_distance}")


##################################################
# Part 2
##################################################


total_distance = 0
for galaxy_position1 in galaxy_positions:
    for galaxy_position2 in galaxy_positions:
            # Only add distance for each pair once
            if (galaxy_position1[0] < galaxy_position2[0]) or (galaxy_position1[0] == galaxy_position2[0] and (galaxy_position1[1] < galaxy_position2[1])):
                distance = find_distance(*galaxy_position1, *galaxy_position2, 999999)
                total_distance += distance


# 603020563700
print(f"Part 2 answer: {total_distance}")

