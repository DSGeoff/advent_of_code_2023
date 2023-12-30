import re
import numpy as np
import pandas as pd

day = 3
input_fn = f"day{day:02d}_input.txt"

with open(input_fn) as f:
    data = f.read().split()

##################################################
# Part 1
##################################################

def is_ascii_digit(char):
     return 48 <= ord(char) <= 57

ncols = len(data[0])
nrows = len(data)

grid = np.empty((nrows, ncols), dtype=str)

part_numbers_df = pd.DataFrame({
    "part_number": pd.Series(dtype="int"),
    "row": pd.Series(dtype="int"),
    "start_col": pd.Series(dtype="int"),
    "end_col": pd.Series(dtype="int"),

})

symbols_df = pd.DataFrame({
    "symbol": pd.Series(dtype="str"),
    "row": pd.Series(dtype="int"),
    "col": pd.Series(dtype="int"),
})

for i in range(nrows):
    for j in range(ncols):
        grid[i, j] = data[i][j]

# find numbers
for i in range(nrows):
    # If we're in the middle of reading a number, we'll look at next
    # entries in the matrix to see if the number continues
    # Otherwise, we'll check if a new number is starting
    j = 0
    while j < ncols:
        if is_ascii_digit(grid[i, j]):
            part_number = grid[i, j]
            start_col = j
            row = i
            reading_number = True
            while reading_number and j < ncols - 1:
                j += 1
                if is_ascii_digit(grid[i, j]):
                    part_number += grid[i, j]
                else:
                    reading_number = False
                    if grid[i, j] != ".":
                        symbols_df.loc[len(symbols_df.index)] = [grid[i, j], i, j]
            end_col = j - 1
            part_number = int(part_number)
            part_numbers_df.loc[len(part_numbers_df.index)] = [part_number, row, start_col, end_col]
        elif grid[i, j] != ".":
            symbols_df.loc[len(symbols_df.index)] = [grid[i, j], i, j]
        j += 1

part_numbers_df["is_part_number"] = False




# Figure out if each number should count
# Loop through each number, look around the number to see if there's a symbol
# that's not a period or a digit
# If start_x is 0, don't look to left
# If start_x is ncols - 1, don't look right
# If start_y is 0, don't look up
# If start_y is nrows - 1, don't look up
# Then, sum up the value of part_number for rows where that variable is True

for current_row_index in part_numbers_df.index:

    current_start_col = part_numbers_df.loc[current_row_index, "start_col"]
    current_end_col = part_numbers_df.loc[current_row_index, "end_col"]
    current_row = part_numbers_df.loc[current_row_index, "row"]
    current_is_part_number = False

    def is_symbol(i, j):
        if not is_ascii_digit(grid[i, j]) and grid[i, j] != ".":
            return True
        else:
            return False

    # Look for symbols above if it's not row 0
    if current_row > 0:
        for j in range(current_start_col, current_end_col + 1):
            current_is_part_number = is_symbol(current_row - 1, j)
            if current_is_part_number:
                break
        
        if current_start_col > 0 and not current_is_part_number:
            current_is_part_number = is_symbol(current_row - 1, current_start_col - 1)
        
        if current_end_col < ncols - 1 and not current_is_part_number:
            current_is_part_number = is_symbol(current_row - 1, current_end_col + 1)

    # Look for symbols below if it's not the last row
    if current_row < nrows - 1 and not current_is_part_number:
        for j in range(current_start_col, current_end_col + 1):
            current_is_part_number = is_symbol(current_row + 1, j)
            if current_is_part_number:
                break
        
        if current_start_col > 0 and not current_is_part_number:
            current_is_part_number = is_symbol(current_row + 1, current_start_col - 1)
        
        if current_end_col < ncols - 1 and not current_is_part_number:
            current_is_part_number = is_symbol(current_row + 1, current_end_col + 1)

    # Check sides
    if current_start_col > 0 and not current_is_part_number:
        current_is_part_number = is_symbol(current_row, current_start_col - 1)

    if current_end_col < ncols - 1 and not current_is_part_number:
        current_is_part_number = is_symbol(current_row, current_end_col + 1)


    part_numbers_df.loc[current_row_index, "is_part_number"] = current_is_part_number


part_numbers_df["is_part_number"]

# 517021
print(f"Part 1 answer: {part_numbers_df.loc[part_numbers_df['is_part_number'], 'part_number'].sum()}")




##################################################
# Part 2
##################################################

# Create asterisks_df as only the rows of symbols_df that have asterisks.  We'll then loop through it
# and find adjacent numbers

asterisks_df = symbols_df[symbols_df["symbol"] == "*"].reset_index(drop=True)
asterisks_df["digit_count"] = 0
asterisks_df["num1"] = 0
asterisks_df["num2"] = 0

for current_row_index in asterisks_df.index:
    current_num_count = 0
    current_row = asterisks_df.loc[current_row_index, "row"]
    current_col = asterisks_df.loc[current_row_index, "col"]

    # Look in part_numbers_df for adjacent numbers
    # Count numbers above if it's not row 0
    if current_row > 0:
        above = "".join(grid[current_row - 1, (current_col-1):(current_col+2)])
        # If it's 3 digits, that is the number
        if re.search(r"\d{3}", above) is not None:
            part_number = part_numbers_df.loc[(part_numbers_df["row"] == current_row - 1) & (part_numbers_df["start_col"] == current_col - 1), "part_number"].item()
            current_num_count += 1
            asterisks_df.loc[current_row_index, f"num{current_num_count}"] = part_number

        # If it's two digits, then a non-digit, the middle digit is the end
        if re.search(r"\d\d\D", above) is not None:
            part_number = part_numbers_df.loc[(part_numbers_df["row"] == current_row - 1) & (part_numbers_df["end_col"] == current_col), "part_number"].item()
            current_num_count += 1
            asterisks_df.loc[current_row_index, f"num{current_num_count}"] = part_number

        # If it's a non-digit, then two digits, the middle digit is the start
        if re.search(r"\D\d\d", above) is not None:
            part_number = part_numbers_df.loc[(part_numbers_df["row"] == current_row - 1) & (part_numbers_df["start_col"] == current_col), "part_number"].item()
            current_num_count += 1
            asterisks_df.loc[current_row_index, f"num{current_num_count}"] = part_number

        # If it starts with a digit, then a non-digit, the digit is the end of a number
        if re.search(r"^\d\D", above) is not None:
            part_number = part_numbers_df.loc[(part_numbers_df["row"] == current_row - 1) & (part_numbers_df["end_col"] == current_col - 1), "part_number"].item()
            current_num_count += 1
            asterisks_df.loc[current_row_index, f"num{current_num_count}"] = part_number

        # If the last two characters are a non-digit, then a digit, the digit is the start of a number
        if re.search(r"\D\d$", above) is not None:
            part_number = part_numbers_df.loc[(part_numbers_df["row"] == current_row - 1) & (part_numbers_df["start_col"] == current_col + 1), "part_number"].item()
            current_num_count += 1
            asterisks_df.loc[current_row_index, f"num{current_num_count}"] = part_number

        # If it has a 1 digit number in the middle
        if re.search(r"\D\d\D", above) is not None:
            part_number = part_numbers_df.loc[(part_numbers_df["row"] == current_row - 1) & (part_numbers_df["end_col"] == current_col), "part_number"].item()
            current_num_count += 1
            asterisks_df.loc[current_row_index, f"num{current_num_count}"] = part_number


    # Count numbers below if it's not the last row
    if current_row < nrows - 1:
        below = "".join(grid[current_row + 1, (current_col-1):(current_col+2)])

        # If it's 3 digits, that is the number
        if re.search(r"\d{3}", below) is not None:
            part_number = part_numbers_df.loc[(part_numbers_df["row"] == current_row + 1) & (part_numbers_df["start_col"] == current_col - 1), "part_number"].item()
            current_num_count += 1
            asterisks_df.loc[current_row_index, f"num{current_num_count}"] = part_number

        # If it's two digits, then a non-digit, the middle digit is the end
        if re.search(r"\d\d\D", below) is not None:
            part_number = part_numbers_df.loc[(part_numbers_df["row"] == current_row + 1) & (part_numbers_df["end_col"] == current_col), "part_number"].item()
            current_num_count += 1
            asterisks_df.loc[current_row_index, f"num{current_num_count}"] = part_number

        # If it's a non-digit, then two digits, the middle digit is the start
        if re.search(r"\D\d\d", below) is not None:
            part_number = part_numbers_df.loc[(part_numbers_df["row"] == current_row + 1) & (part_numbers_df["start_col"] == current_col), "part_number"].item()
            current_num_count += 1
            asterisks_df.loc[current_row_index, f"num{current_num_count}"] = part_number

        # If it starts with a digit, then a non-digit, the digit is the end of a number
        if re.search(r"^\d\D", below) is not None:
            part_number = part_numbers_df.loc[(part_numbers_df["row"] == current_row + 1) & (part_numbers_df["end_col"] == current_col - 1), "part_number"].item()
            current_num_count += 1
            asterisks_df.loc[current_row_index, f"num{current_num_count}"] = part_number

        # If the last two characters are a non-digit, then a digit, the digit is the start of a number
        if re.search(r"\D\d$", below) is not None:
            part_number = part_numbers_df.loc[(part_numbers_df["row"] == current_row + 1) & (part_numbers_df["start_col"] == current_col + 1), "part_number"].item()
            current_num_count += 1
            asterisks_df.loc[current_row_index, f"num{current_num_count}"] = part_number

        # If it has a 1 digit number in the middle
        if re.search(r"\D\d\D", below) is not None:
            part_number = part_numbers_df.loc[(part_numbers_df["row"] == current_row + 1) & (part_numbers_df["end_col"] == current_col), "part_number"].item()
            current_num_count += 1
            asterisks_df.loc[current_row_index, f"num{current_num_count}"] = part_number

        # Check sides
        if current_col > 0:
            part_number = part_numbers_df.loc[(part_numbers_df["row"] == current_row) & (part_numbers_df["end_col"] == current_col - 1), "part_number"]
            if part_number.shape[0] > 0:
                current_num_count += 1
                asterisks_df.loc[current_row_index, f"num{current_num_count}"] = part_number.item()
        
        if current_col < ncols - 1:
            part_number = part_numbers_df.loc[(part_numbers_df["row"] == current_row) & (part_numbers_df["start_col"] == current_col + 1), "part_number"]
            if part_number.shape[0] > 0:
                current_num_count += 1
                asterisks_df.loc[current_row_index, f"num{current_num_count}"] = part_number.item()

    asterisks_df.at[current_row_index, "digit_count"] = current_num_count

asterisks_df["gear_ratio"] = asterisks_df["num1"] * asterisks_df["num2"]

# 81296995
print(f"Part 2 answer: {asterisks_df.gear_ratio.sum()}")


