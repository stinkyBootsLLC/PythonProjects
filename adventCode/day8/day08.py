import numpy as np


def get_highest_scenic_score(lines):
    grid = [list(map(int, list(line))) for line in lines]

    rows = len(grid)
    columns = len(grid[0])

    grid = np.array(grid)
    # right, left, down, up
    movement_directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    scenic_score = 0
    for i in range(rows):
        for j in range(columns):
            height = grid[i, j]
            score = 1

            # Scan in 4 directions
            for direction_i, direction_j in movement_directions:
                ii, jj = i + direction_i, j + direction_j
                distance = 0

                while (0 <= ii < rows and 0 <= jj < columns) and grid[ii, jj] < height:
                    distance += 1
                    ii += direction_i
                    jj += direction_j

                    if (0 <= ii < rows and 0 <= jj < columns) and grid[ii, jj] >= height:
                        distance += 1

                score *= distance

            scenic_score = max(scenic_score, score)


    return scenic_score   













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
# What is the highest scenic score possible for any tree?
p2_ans = get_highest_scenic_score(lines)
print(p2_ans)
