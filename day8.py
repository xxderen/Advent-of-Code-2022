with open("day8.txt", 'r') as f:
    lines = f.read().splitlines()
trees = []
for row in lines:
    row = list(row)
    trees.append(row)
def count_visible_trees(trees):
    visible_trees = 0
    rows, cols = len(trees), len(trees[0])

    visible_trees += 2 * rows + 2 * (cols - 2)

    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            tree_height = trees[i][j]

            if all(trees[i][k] < tree_height for k in range(j)):
                visible_trees += 1
                continue

            if all(trees[i][k] < tree_height for k in range(j + 1, cols)):
                visible_trees += 1
                continue

            if all(trees[k][j] < tree_height for k in range(i)):
                visible_trees += 1
                continue

            if all(trees[k][j] < tree_height for k in range(i + 1, rows)):
                visible_trees += 1
                continue

    return visible_trees


print(count_visible_trees(trees))  

def scenic_score(trees, x, y):
    height = trees[x][y]
    up = down = left = right = 0

    for i in range(x - 1, -1, -1):
        up += 1
        if trees[i][y] >= height:
            break

    for i in range(x + 1, len(trees)):
        down += 1
        if trees[i][y] >= height:
            break

    for i in range(y - 1, -1, -1):
        left += 1
        if trees[x][i] >= height:
            break

    for i in range(y + 1, len(trees[0])):
        right += 1
        if trees[x][i] >= height:
            break

    return up * down * left * right

def highest_scenic_score(trees):
    max_score = 0
    for x in range(len(trees)):
        for y in range(len(trees[0])):
            score = scenic_score(trees, x, y)
            max_score = max(max_score, score)
    return max_score


print(highest_scenic_score(trees))  