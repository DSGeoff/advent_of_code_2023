import re
from functools import reduce

day = 6
input_fn = f"day{day:02d}_input.txt"

with open(input_fn) as f:
    data = f.readlines()



##################################################
# Part 1
##################################################

time = re.sub(r"Time:\s+", "", data[0]).replace("\n", "")
time = [int(num) for num in re.split(r"\s+", time)]

record_distance = re.sub(r"Distance:\s+", "", data[1])
record_distance = [int(num) for num in re.split(r"\s+", record_distance)]

ways_to_win_list = []
for i in range(len(time)):
    ways_to_win = 0
    for hold_time in range(time[i]):
        distance = (time[i] - hold_time) * hold_time
        if distance > record_distance[i]:
            ways_to_win += 1
    ways_to_win_list.append(ways_to_win)

ways_to_win_list

# 
print(f"Part 1 answer: {reduce(lambda x, y: x * y, ways_to_win_list)}")


##################################################
# Part 2
##################################################

time = int(data[0].replace("Time:", "").replace(" ", "").replace("\n", ""))
record_distance = int(data[1].replace("Distance:", "").replace(" ", "").replace("\n", ""))

ways_to_win = 0
for hold_time in range(time):
    distance = (time - hold_time) * hold_time
    if distance > record_distance:
        ways_to_win += 1

# 21039729
print(f"Part 2 answer: {ways_to_win}")

