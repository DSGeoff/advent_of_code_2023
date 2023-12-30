import re

day = 2
input_fn = f"day{day:02d}_input.txt"

with open(input_fn) as f:
    games = f.readlines()


##################################################
# Parts 1 and 2
##################################################
allowed = {"blue": 14, "green": 13, "red": 12}

possible_games = []
game_power = []

for game in games:

    game_num = int(re.search(r"Game (\d+): ", game)[1])
    reveals = re.sub(r"Game (\d+): ", "", game).split("; ")

    game_maxes = {"blue": 0, "green": 0, "red": 0}

    for reveal in reveals:
        reveal_counts = {"blue": 0, "green": 0, "red": 0}
        for color in ["blue", "green", "red"]:
            temp_count = re.search(fr"(\d+) {color}", reveal)
            if temp_count is not None:
                reveal_counts[color] = int(temp_count[1])

            game_maxes[color] = max(reveal_counts[color], game_maxes[color])

    if game_maxes["blue"] <= allowed["blue"] and game_maxes["green"] <= allowed["green"] and game_maxes["red"] <= allowed["red"]:
        possible_games.append(game_num)

    game_power.append(game_maxes["blue"] * game_maxes["green"] * game_maxes["red"])


# 2593
print(f"Part 1 answer: {sum(possible_games)}")

# 54699
print(f"Part 2 answer: {sum(game_power)}")