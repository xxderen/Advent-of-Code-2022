with open("day6.txt", 'r') as f:
    line = f.read()

index = 0
while len(set(line[index:index+4])) != 4:
    index += 1
print(index+4)

index = 0
while len(set(line[index:index+14])) != 14:
    index += 1
print(index+14)
