elf_cache = []
food = 0

with open("day1.txt", 'r') as f:
    lines = f.readlines()
    for line in lines:
        if (line.strip()):
            food += int(line)
        else:
            elf_cache.append(food)
            food = 0
calorie_list = elf_cache
largest = max(calorie_list)
print(largest)
top_three = sum(sorted(calorie_list)[-3:])
print(top_three)