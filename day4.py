file = open('day4.txt', 'r')
file2 = open('day4.txt', 'r')

overlaps = 0
for line in file.read().splitlines():
    first_pair, second_pair = [list(map(int, pair.split('-'))) for pair in line.split(",")]
    if first_pair[0] != second_pair[0]:
        if first_pair[0] > second_pair[0]:
            inside_range, outside_range = first_pair, second_pair
        else:
            inside_range, outside_range = second_pair, first_pair
    else:
        if first_pair[1] < second_pair[1]:
            inside_range, outside_range = first_pair, second_pair
        else:
            inside_range, outside_range = second_pair, first_pair
    if inside_range[1] <= outside_range[1]:
        overlaps += 1
print(str(overlaps))




overlaps = 0
for line in file2.read().splitlines():
    first_pair, second_pair = [list(map(int, pair.split('-'))) for pair in line.split(",")]
    if first_pair[0] > second_pair[0]:
        inside_range_index, outside_range_index = first_pair, second_pair
    else:
        inside_range_index, outside_range_index = second_pair, first_pair
    if inside_range_index[0] <= outside_range_index[1]:
        overlaps += 1
print(str(overlaps))


