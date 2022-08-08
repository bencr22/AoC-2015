square_foot = 0

with open("day2/input.txt", "r") as file:
    for line in file:
        numbers = line.split("x")

        values = []
        values.append( int(numbers[0]) * int(numbers[1] ))
        values.append( int(numbers[0]) * int(numbers[2] ))
        values.append( int(numbers[1]) * int(numbers[2] ))

        spare = min(values)
        square_foot += spare + sum(values)


print(square_foot)