ribbon = 0

with open("day2/input.txt", "r") as file:
    for line in file:
        numbers = line.split("x")

        # creates a list of the side lengths
        sides = []
        sides.append(int(numbers[0]))
        sides.append(int(numbers[1]))
        sides.append(int(numbers[2]))
        
        # for the bow 
        ribbon += (sides[0] * sides[1] * sides[2])

        sides.remove(max(sides))
        
        # for the main ribbon
        ribbon += sum(sides) + sum(sides)

print(ribbon)