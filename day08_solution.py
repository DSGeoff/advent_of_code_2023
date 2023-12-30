import math

import pandas as pd

day = 8
input_fn = f"day{day:02d}_input.txt"

with open(input_fn) as f:
    data = f.readlines()


# First line contains left/right instructions
left_right = data[0].replace("\n", "")

# Next elements start on the third line
next_elements_df = pd.DataFrame([(line[:3], line[7:10], line[12:15]) for line in data[2:]], columns=["temp_index", "L", "R"])
next_elements_df.index = next_elements_df["temp_index"]
next_elements_df.drop(columns="temp_index", inplace=True)



##################################################
# Part 1
##################################################


current_location = "AAA"
found_ZZZ = False
steps = 0
while not found_ZZZ:
    for LR in left_right:
        steps += 1
        current_location = next_elements_df.at[current_location, LR]
        if current_location == "ZZZ":
            found_ZZZ = True
            break

# 15989
print(f"Part 1 answer: {steps}")


##################################################
# Part 2
##################################################

# Let's find the number of steps for each path that ends with A separately.
# Then, we can take the LCM of those.

# Find all that end with A
current_locations = []
for item in next_elements_df.index:
    if item[-1] == "A":
        current_locations.append(item)

steps_list = [0] * len(current_locations)
for i, current_location in enumerate(current_locations):
    steps = 0
    found_ZZZ = False
    while not found_ZZZ:
        for LR in left_right:
            steps += 1
            current_location = next_elements_df.at[current_location, LR]
            if current_location[-1] == "Z":
                found_ZZZ = True
                break
    steps_list[i] = steps


# 13830919117339
print(f"Part 2 answer: {math.lcm(*steps_list)}")

