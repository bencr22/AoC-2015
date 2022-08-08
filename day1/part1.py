level = 0

with open("day1/input.txt", "r") as file:
    for line in file:
        data = str(line)

for character in data:
    if character == "(":
        level += 1
    else:
        level -= 1

print(level)