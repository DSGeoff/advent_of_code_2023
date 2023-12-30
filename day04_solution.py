import re

day = 4
input_fn = f"day{day:02d}_input.txt"

with open(input_fn) as f:
    data = f.readlines()



##################################################
# Part 1
##################################################
points = []
count_list = []

for card in data:
    card_num = re.search(r"Card\s+(\d+)", card)[1]

    temp = (
        re.sub(r"Card\s+(\d+):\s+", "", card)
        .replace("\n", "")
    )

    winning_numbers, our_numbers = re.split(r"\s+\|\s+", temp)

    winning_numbers = set(int(num) for num in re.split(r"\s+", winning_numbers))
    our_numbers = [int(num) for num in re.split(r"\s+", our_numbers)]

    count = 0
    for num in our_numbers:
        if num in winning_numbers:
            count += 1
    count_list.append(count)

    if count == 0:
        points.append(0)
    else:
        points.append(2**(count - 1))

# 21919
print(f"Part 1 answer: {sum(points)}")


##################################################
# Part 2
##################################################

# Just need to use count_list to figure out how many of each card we get

# Initialize a list to all 0s to count the number of instances of each card
num_instances = [0] * len(count_list)

for i, count in enumerate(count_list):
    # Add one for the original card
    num_instances[i] += 1
    # Add the number of instances of the current card onto the next {count} cards
    for j in range(1, count + 1):
        num_instances[i + j] += num_instances[i]

# 9881048
print(f"Part 2 answer: {sum(num_instances)}")

