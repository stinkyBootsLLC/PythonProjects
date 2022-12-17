import numpy as np


def get_highest_scenic_score(lines):
    grid = [list(map(int, list(line))) for line in lines]

    rows = len(grid)
    columns = len(grid[0])

    grid = np.array(grid)

    dd = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    ans = 0
    for i in range(rows):
        for j in range(columns):
            height = grid[i, j]
            score = 1

            # Scan in 4 directions
            for di, dj in dd:
                ii, jj = i + di, j + dj
                dist = 0

                while (0 <= ii < rows and 0 <= jj < columns) and grid[ii, jj] < height:
                    dist += 1
                    ii += di
                    jj += dj

                    if (0 <= ii < rows and 0 <= jj < columns) and grid[ii, jj] >= height:
                        dist += 1

                score *= dist

            ans = max(ans, score)


    print(ans)    













def get_visible_trees_from_outside_grid(lines):
   
    grid = [list(map(int, list(line))) for line in lines]

    rows = len(grid)
    columns = len(grid[0])

    grid = np.array(grid)
   
    visible_trees = 0
    for i in range(rows):
        for j in range(columns):
            height = grid[i, j]
            # look in all 4 directions 
            # row up to the current column but not including the current column 
            # scan left
            if j == 0 or np.amax(grid[i, :j]) < height:
                visible_trees += 1
            # scan right
            elif j == columns - 1 or np.amax(grid[i, (j+1):]) < height:
                visible_trees += 1
            # scan up
            elif i == 0 or np.amax(grid[:i, j]) < height:
                visible_trees += 1
            # scan down
            elif i == rows - 1 or np.amax(grid[(i+1):, j]) < height:
                visible_trees += 1

    return visible_trees

with open("input.txt", "r") as file_in:
    lines = file_in.read().strip().split()
# how many trees are visible from outside the grid?
p1_ans = get_visible_trees_from_outside_grid(lines)
print(p1_ans)
