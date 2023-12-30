import pandas as pd


day = 7
input_fn = f"day{day:02d}_input.txt"

with open(input_fn) as f:
    data = f.readlines()



##################################################
# Part 1
##################################################

df = pd.DataFrame({
    "hand": pd.Series(dtype="string"),
    "bid": pd.Series(dtype=int),
    "hand_type": pd.Series(dtype=int),
    "sort_friendly_hand": pd.Series(dtype="string"),
})

for row in data:
    hand, bid = row.split(" ")
    bid = int(bid)

    # Get counts of types of cards
    hand_count = {}
    for card in hand:
        hand_count[card] = hand_count.get(card, 0) + 1

    hand_count = sorted(hand_count.values(), reverse=True)

    # Will use number to denote different hands
    # Then, sorting by the number automatically ranks the hands
    # five of a kind = 7
    # four of a kind = 6
    # full house = 5
    # three of a kind = 4
    # two pair = 3
    # one pair = 2
    # high card = 1

    if hand_count == [5]:
        hand_type = 7
    elif hand_count == [4, 1]:
        hand_type = 6
    elif hand_count == [3, 2]:
        hand_type = 5
    elif hand_count == [3, 1, 1]:
        hand_type = 4
    elif hand_count == [2, 2, 1]:
        hand_type = 3
    elif hand_count == [2, 1, 1, 1]:
        hand_type = 2
    elif hand_count == [1, 1, 1, 1, 1]:
        hand_type = 1
    else:
        print("oops")

    # To make sorting easier, we'll replace T, J, Q, K, A with A, B, C, D, E
    # Have to do this replacing in reverse order, otherwise replacing T with A, then A with E will convert T to E
    sort_friendly_hand = hand.replace("A", "E").replace("K", "D").replace("Q", "C").replace("J", "B").replace("T", "A")

    df.loc[len(df.index)] = [hand, bid, hand_type, sort_friendly_hand]


df.sort_values(["hand_type", "sort_friendly_hand"], ignore_index=True, inplace=True)
df["rank"] = df.index + 1

# 248217452
ans = (df["rank"] * df["bid"]).sum()
print(f"Part 1 answer: {ans}")


##################################################
# Part 2
##################################################

df = pd.DataFrame({
    "hand": pd.Series(dtype="string"),
    "bid": pd.Series(dtype=int),
    "hand_type": pd.Series(dtype=int),
    "sort_friendly_hand": pd.Series(dtype="string")
})

for row in data:
    hand, bid = row.split(" ")
    bid = int(bid)

    # Get counts of types of cards
    hand_count = {}
    joker_count = 0
    for card in hand:
        if card == "J":
            joker_count += 1
        else:
            hand_count[card] = hand_count.get(card, 0) + 1

    if joker_count == 5:
        hand_count = [5]
    else:
        hand_count = sorted(hand_count.values(), reverse=True)
        hand_count[0] += joker_count

    # Will use number to denote different hands
    # Then, sorting by the number automatically ranks the hands
    # five of a kind = 7
    # four of a kind = 6
    # full house = 5
    # three of a kind = 4
    # two pair = 3
    # one pair = 2
    # high card = 1

    if hand_count == [5]:
        hand_type = 7
    elif hand_count == [4, 1]:
        hand_type = 6
    elif hand_count == [3, 2]:
        hand_type = 5
    elif hand_count == [3, 1, 1]:
        hand_type = 4
    elif hand_count == [2, 2, 1]:
        hand_type = 3
    elif hand_count == [2, 1, 1, 1]:
        hand_type = 2
    elif hand_count == [1, 1, 1, 1, 1]:
        hand_type = 1
    else:
        print("oops")

    # To make sorting easier, we'll replace T, J, Q, K, A with A, B, C, D, E
    # Have to do it in reverse order, otherwise, I'll replace "T" with "A", then "A" with "E"
    # Changing to replace J with . so it's lower than 2 when sorted
    sort_friendly_hand = hand.replace("A", "E").replace("K", "D").replace("Q", "C").replace("J", ".").replace("T", "A")

    df.loc[len(df.index)] = [hand, bid, hand_type, sort_friendly_hand]


df.sort_values(["hand_type", "sort_friendly_hand"], ignore_index=True, inplace=True)
df["rank"] = df.index + 1

# 245576185
ans = (df["rank"] * df["bid"]).sum()
print(f"Part 2 answer: {ans}")

