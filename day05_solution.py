import re

import pandas as pd

day = 5
input_fn = f"day{day:02d}_input.txt"

with open(input_fn) as f:
    data = f.read()



##################################################
# Part 1
##################################################
which_conversions = [
    "seed-to-soil", "soil-to-fertilizer", "fertilizer-to-water", "water-to-light",
    "light-to-temperature", "temperature-to-humidity", "humidity-to-location"
]




def make_conversion_df(which_conversion):

    conversion_num = {
        "seed-to-soil": 1,
        "soil-to-fertilizer": 2,
        "fertilizer-to-water": 3,
        "water-to-light": 4,
        "light-to-temperature": 5,
        "temperature-to-humidity": 6,
        "humidity-to-location": 7
    }

    which_conversion_num = conversion_num[which_conversion]

    conversion = (
        # re.DOTALL makes the \n one of the characters included in .
        re.search(fr"{which_conversion} map:\n(.+)", data_split[which_conversion_num], re.DOTALL)[1]
        .split("\n")
    )

    conversion_df = pd.DataFrame({
        "source_start": pd.Series(dtype="int"),
        "source_end": pd.Series(dtype="int"),
        "destination_start": pd.Series(dtype="int"),
        "destination_end": pd.Series(dtype="int"),
    })

    for entry in conversion:
        destination_start, source_start, range_length = [int(num) for num in entry.split(" ")]
        conversion_df.loc[len(conversion_df.index)] = [
            source_start,
            source_start + range_length - 1,
            destination_start,
            destination_start + range_length - 1
            ]

    return conversion_df


# This does a binary search to find a range that works, which relies on the data frames being sorted
# For Part 2, we want to do the conversion in the reverse order, which we can do with forward=False
def do_conversion(source_variable, which_conversion, forward=True):
    conversion_df = conversions_all[which_conversion]

    if forward:
        source_start = "source_start"
        source_end = "source_end"
        destination_start = "destination_start"
        # destination_end = "destination_end"
    else:
        source_start = "destination_start"
        source_end = "destination_end"
        destination_start = "source_start"
        # destination_end = "source_end"

    low = 0
    high = len(conversion_df.index) - 1
    while low <= high:
        mid = (low + high) // 2
        if source_variable < conversion_df.at[mid, source_start]:
            high = mid - 1
        elif source_variable > conversion_df.at[mid, source_end]:
            low = mid + 1
        else:
            return source_variable + conversion_df.at[mid, destination_start] - conversion_df.at[mid, source_start]

    return source_variable

data_split = data.split("\n\n")

# Seeds
seeds_str = data_split[0]

seeds = [
    int(num) for num in
    re.search(r"seeds: (.+)", seeds_str)[1]
    .split(" ")
]


# Make dictionary of all conversion dataframes
conversions_all = {}

for which_conversion in which_conversions:
    conversions_all[which_conversion] = make_conversion_df(which_conversion)

# For Part 1, sort according to source variables
for which_conversion in which_conversions:
    conversions_all[which_conversion] = conversions_all[which_conversion].sort_values("source_start", ignore_index=True)


# Do conversions
min_location = 999999999999999

seed_count = 0
for seed in seeds:
    seed_count += 1
    soil = do_conversion(seed, "seed-to-soil")
    fertilizer = do_conversion(soil, "soil-to-fertilizer")
    water = do_conversion(fertilizer, "fertilizer-to-water")
    light = do_conversion(water, "water-to-light")
    temperature = do_conversion(light, "light-to-temperature")
    humidity = do_conversion(temperature, "temperature-to-humidity")
    location = do_conversion(humidity, "humidity-to-location")

    if location < min_location:
        min_location = location
    

# 993500720
print(f"Part 1 answer: {min_location}")


##################################################
# Part 2
##################################################

# Doing all possibilities from Part 1 would take way too long because there are so many.
# If we're looking for the lowest location number, let's start with location number equal
# to 1 and go up, converting backward until we find one that corresponds to a seed number.
# This still takes a few minutes to run, but oh well.

# For Part 2, sort according to destination variables
for which_conversion in which_conversions:
    conversions_all[which_conversion] = conversions_all[which_conversion].sort_values("destination_start", ignore_index=True)



found = False
location = -1
while not found:
    location += 1
    humidity = do_conversion(location, "humidity-to-location", forward=False)
    temperature = do_conversion(humidity, "temperature-to-humidity", forward = False)
    light = do_conversion(temperature, "light-to-temperature", forward = False)
    water = do_conversion(light, "water-to-light", forward = False)
    fertilizer = do_conversion(water, "fertilizer-to-water", forward = False)
    soil = do_conversion(fertilizer, "soil-to-fertilizer", forward = False)
    seed = do_conversion(soil, "seed-to-soil", forward = False)
    
    # Check if the seed corresponds to an initial value
    for i in range(len(seeds) // 2):
        seed_range_start = seeds[2 * i]
        seed_range_length = seeds[2 * i + 1]
        seed_range_end = seed_range_start + seed_range_length - 1
        if seed_range_start <= seed <= seed_range_end:
            found = True
            break

    if location % 1000000 == 0:
        print(location)

location




# 4917124
print(f"Part 2 answer: {location}")




