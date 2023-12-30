import pandas as pd

day = 10
input_fn = f"day{day:02d}_input.txt"

with open(input_fn) as f:
    data = f.readlines()

moves = {
    "|": ["north", "south"],
    "-": ["east", "west"],
    "L": ["north", "east"],
    "J": ["north", "west"],
    "7": ["south", "west"],
    "F": ["south", "east"],
}

opposite_map = {
    "north": "south",
    "east": "west",
    "south": "north",
    "west": "east",
}

loop_df = pd.DataFrame({
    "symbol": pd.Series(dtype="object"),
    "row": pd.Series(dtype="int64"),
    "column": pd.Series(dtype="int64"),
    "move_direction": pd.Series(dtype="string")
})

##################################################
# Part 1
##################################################

# Searches grid for S
def find_S(data):
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == "S":
                return (i, j)

# Look around S to see which adjacent blocks go into S
def move(data, row, column, move_direction):
    if move_direction == "north":
        return data[row-1][column], row - 1, column
    elif move_direction == "east":
        return data[row][column+1], row, column + 1
    elif move_direction == "south":
        return data[row+1][column], row + 1, column
    elif move_direction == "west":
        return data[row][column-1], row, column - 1



# Step 1: Find S
symbol = "S"
row, column = find_S(data)
step_number = 0
move_direction = "" # Currently, unknown
loop_df.loc[step_number] = [symbol, row, column, ""]



# Step 2: Determine direction to move from S
for move_direction in ["north", "east", "south", "west"]:
    temp_symbol, temp_row, temp_column = move(data, row, column, move_direction)
    if opposite_map[move_direction] in moves[temp_symbol]:
        loop_df.loc[step_number, "move_direction"] = move_direction
        opposite_direction = opposite_map[move_direction]
        symbol = temp_symbol
        row = temp_row
        column = temp_column
        step_number += 1
        # print(symbol, row, column, step_number)
        loop_df.loc[step_number, ["symbol", "row", "column", "move_direction"]] = [symbol, row, column, ""]
        break

# Step 3: Based on the current symbol and the last move_direction, continue on path until we get back to S
while symbol != "S":
    # print(opposite_direction)
    # Each symbol has two possible moves.  We came from the opposite of move_direction and should continue to the other direction.
    if moves[symbol][0] == opposite_direction:
        move_direction = moves[symbol][1]
    else:
        move_direction = moves[symbol][0]
    opposite_direction = opposite_map[move_direction]
    # print(move_direction)
    loop_df.loc[step_number, "move_direction"] = move_direction
    symbol, row, column = move(data, row, column, move_direction)
    step_number += 1
    # print(symbol, row, column, step_number)
    loop_df.loc[step_number, ["symbol", "row", "column", "move_direction"]] = [symbol, row, column, ""]


# print(loop_df)

# 
print(f"Part 1 answer: {loop_df.index[-1] // 2}")


##################################################
# Part 2
##################################################


# 
print(f"Part 2 answer: {}")

