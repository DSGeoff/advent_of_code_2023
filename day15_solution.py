day = 15
input_fn = f"day{day:02d}_input.txt"

with open(input_fn) as f:
    data = f.read().split(",")


def hash_algorithm(string):
    current_value = 0
    for char in string:
        current_value += ord(char)
        current_value *= 17
        current_value %= 256
    return current_value



##################################################
# Part 1
##################################################

current_values = []
for string in data:
    current_values.append(hash_algorithm(string))

# 511343
print(f"Part 1 answer: {sum(current_values)}")



##################################################
# Part 2
##################################################

# For part 2, string.find() to find the position of the symbol, then split the string up into parts.
# The number is always a single digit, so don’t need to worry about figuring out length of it.

labels = []
operations = []
focal_lengths = []
which_boxes = []

boxes = {num: {} for num in range(256)}

for item in data:
    operation_position = item.find("=")
    if operation_position == -1:
        operation = "-"
        operation_position = item.find("-")
        focal_length = 0
    else:
        operation = "="
        focal_length = int(item[operation_position+1:])

    focal_lengths.append(focal_length)
    label = item[:operation_position]
    labels.append(label)
    which_box = hash_algorithm(label)
    operations.append(operation)
    which_boxes.append(which_box)

    if operation == "-":
        boxes[which_box].pop(label, None)
    else:
        boxes[which_box][label] = focal_length

focusing_powers = []

for box, items in boxes.items():
    for slot, (label, focal_length) in enumerate(items.items()):
        focusing_power = (box + 1) * (slot + 1) * focal_length
        focusing_powers.append(focusing_power)

# 294474
print(f"Part 2 answer: {sum(focusing_powers)}")

