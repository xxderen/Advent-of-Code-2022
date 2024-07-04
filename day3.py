with open("day3.txt", 'r') as f:
    lines = f.read().splitlines()
result = 0
for entry in lines:
    firstpart, secondpart = entry[:len(entry)//2], entry[len(entry)//2:]
    for char in firstpart:
        if char in secondpart:
            if char.islower():
                result += (ord(char) - 96)
            else:
                result += (ord(char) - 38)
            break
print(result)

result = 0
for i in range(0,len(lines),3):
    for char in lines[i]:
        if char in lines[i+1] and char in lines[i+2]:
            if char.islower():
                result += (ord(char) - 96)
            else:
                result += (ord(char) - 38)
            break
print(result)

            

