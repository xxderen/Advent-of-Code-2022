with open("day10.txt", 'r') as f:
    lines = f.read().splitlines()

cycles = 0
value = 1
result = 0

for entry in lines:
    entry = entry.split(" ")
    if entry[0] == "noop":
        cycles += 1
        if cycles in [20, 60, 100, 140, 180, 220]:
            result += cycles * value
    elif entry[0] == "addx":
        for i in range(2):
            cycles += 1
            if cycles in [20, 60, 100, 140, 180, 220]:
                result += cycles * value
        value += int(entry[1])

print(result)