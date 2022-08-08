level = 0

with open("day1/input.txt", "r") as file:
    for line in file:
        data = str(line)

for index, character in enumerate(data):
    if character == ")":
        level -= 1
        if level < 0:
            print(index + 1)
            break
    else:
        level += 1