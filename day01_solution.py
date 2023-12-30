import re

day = 1
input_fn = f"day{day:02d}_input.txt"

with open(input_fn) as f:
    data = f.readlines()


##################################################
# Part 1
##################################################

calibration_values = []

for line in data:
    digits_only = re.sub(r"[a-zA-z]", "", line.replace("\n", ""))
    # Concatenating the first digit with the last works, even for the case where there's only one number
    num = int(digits_only[0] + digits_only[-1])
    calibration_values.append(num)

# 54927
print(f"Part 1 answer: {sum(calibration_values)}")


##################################################
# Part 2
##################################################

def find_first_digit(string):
    for i in range(len(string)):
        # Check if ascii code is a digit 0-9
        if 48 <= ord(string[i]) <= 57:
            return string[i]
        elif string[i:i+3] == "one":
            return "1"
        elif string[i:i+3] == "two":
            return "2"
        elif string[i:i+5] == "three":
            return "3"
        elif string[i:i+4] == "four":
            return "4"
        elif string[i:i+4] == "five":
            return "5"
        elif string[i:i+3] == "six":
            return "6"
        elif string[i:i+5] == "seven":
            return "7"
        elif string[i:i+5] == "eight":
            return "8"
        elif string[i:i+4] == "nine":
            return "9"
    print("Oops, didn't find a digit")


def find_last_digit(string):
    for i in reversed(range(len(string))):
        # Check if ascii code is a digit 0-9
        if 48 <= ord(string[i]) <= 57:
            return string[i]
        elif string[i-2:i+1] == "one":
            return "1"
        elif string[i-2:i+1] == "two":
            return "2"
        elif string[i-4:i+1] == "three":
            return "3"
        elif string[i-3:i+1] == "four":
            return "4"
        elif string[i-3:i+1] == "five":
            return "5"
        elif string[i-2:i+1] == "six":
            return "6"
        elif string[i-4:i+1] == "seven":
            return "7"
        elif string[i-4:i+1] == "eight":
            return "8"
        elif string[i-3:i+1] == "nine":
            return "9"
    print("Oops, didn't find a digit")

calibration_values2 = []

for line in data:
    line = line.replace("\n", "")
    first_digit = find_first_digit(line)
    last_digit = find_last_digit(line)
    # Concatenating the first digit with the last works, even for the case where there's only one number
    num = int(first_digit + last_digit)
    calibration_values2.append(num)


# 54581
print(f"Part 2 answer: {sum(calibration_values2)}")


##################################################
# Part 2 - Solution 2
##################################################

convert = {
    "zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}


def find_first_digit2(string):
    digit = re.search(r"([0-9]|one|two|three|four|five|six|seven|eight|nine)", string)[0]
    if ord(digit[0]) > 57:
        return convert[digit]
    else:
        return digit


def find_last_digit2(string):
    string = string[::-1]
    reversed_digit = re.search(r"([0-9]|eno|owt|eerht|ruof|evif|xis|neves|thgie|enin)", string)[0]
    digit = reversed_digit[::-1]
    if ord(digit[0]) > 57:
        return convert[digit]
    else:
        return digit

calibration_values22 = []

for line in data:
    line = line.replace("\n", "")
    first_digit2 = find_first_digit2(line)
    last_digit2 = find_last_digit2(line)
    # Concatenating the first digit with the last works, even for the case where there's only one number
    num2 = int(first_digit2 + last_digit2)
    calibration_values22.append(num2)


# 54581
print(f"Part 2 answer: {sum(calibration_values22)}")



