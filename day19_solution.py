import re

day = 19
input_fn = f"day{day:02d}_input.txt"

with open(input_fn) as f:
    data = f.read()


##################################################
# Part 1
##################################################

workflows_initial, parts_ratings_initial = [item.split("\n") for item in data.split("\n\n")]


# Get workflows

workflows = {}

for workflow_initial in workflows_initial:
    brace_position = workflow_initial.find("{")
    workflow_name = workflow_initial[:brace_position]
    workflow = workflow_initial[brace_position+1:].replace("}", "").split(",")
    current_workflow = []
    for item in workflow:
        item_split = item.split(":")
        if len(item_split) == 1:
            workflow_rule = "True"
            workflow_destination = item_split[0]
        else:
            workflow_rule = item_split[0]
            workflow_destination = item_split[1]
        current_workflow.append({"rule": workflow_rule, "destination": workflow_destination})
    workflows[workflow_name] = current_workflow


# Get parts_ratings
parts_ratings = []
for part_ratings in parts_ratings_initial:
    xmas = re.search(r"{x=(\d+),m=(\d+),a=(\d+),s=(\d+)}", part_ratings)
    parts_ratings.append([int(xmas[i]) for i in range(1, 5)])
 

accepted = []
for part_ratings in parts_ratings:
    x, m, a, s = part_ratings
    current_workflow_name = "in"
    complete = False
    while not complete:
        current_workflow = workflows[current_workflow_name]
        for i, current_rule_destination in enumerate(current_workflow):
            current_rule = current_rule_destination["rule"]
            current_destination = current_rule_destination["destination"]
            if eval(current_rule):
                current_workflow_name = current_destination
                break

        if current_workflow_name == "A":
            accepted.append(part_ratings)
            complete = True
        elif current_workflow_name == "R":
            complete = True

 

# 476889
print(f"Part 1 answer: {sum(sum(ratings) for ratings in accepted)}")


##################################################
# Part 2
##################################################


