with open("day2.txt", 'r') as f:
    lines = f.read().splitlines()
points = 0
for entry in lines:
    entry = entry.split(" ")
    entry[1] = entry[1].replace('X', 'A')
    entry[1] = entry[1].replace('Y', 'B')
    entry[1] = entry[1].replace('Z', 'C')
    if entry[1] == "A" and entry[0] == entry[1]:
        points += 4
    elif entry[1] == "A" and entry[0] == "B":
        points += 1
    elif entry[1] == "A" and entry[0] == "C":
        points += 7
    elif entry[1] == "B" and entry[0] == entry[1]:
        points += 5
    elif entry[1] == "B" and entry[0] == "A":
        points += 8
    elif entry[1] == "B" and entry[0] == "C":
        points += 2
    elif entry[1] == "C" and entry[0] == entry[1]:
        points += 6
    elif entry[1] == "C" and entry[0] == "A":
        points += 3
    elif entry[1] == "C" and entry[0] == "B":
        points += 9
print(points)

points = 0
for entry in lines:
    entry = entry.split(" ")
    if entry[0] == "A" :
        if entry[1] == "X":
            points += 3
        elif entry[1] == "Y":
            points += 4
        elif entry[1] == "Z":
            points += 8
    elif entry[0] == "B":
        if entry[1] == "X":
            points += 1
        elif entry[1] == "Y":
            points += 5
        elif entry[1] == "Z":
            points += 9
    elif entry[0] == "C":
        if entry[1] == "X":
            points += 2
        elif entry[1] == "Y":
            points += 6
        elif entry[1] == "Z":
            points += 7
print(points)

