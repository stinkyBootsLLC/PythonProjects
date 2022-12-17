https://adventofcode.com/2022/day/8

Answer by https://github.com/womogenes

### --- Day 8: Treetop Tree House ---

### --- Part One ---
How many trees are visible from outside the grid?
 
**get_visible_trees_from_outside_grid():** Returns visible_trees{int}
 
Ingest puzzle input 
```
grid = [list(map(int, list(line))) for line in lines]
```
Use NumPy to create a 2D Array 
```
grid = np.array(grid)
```
Loop through grid 
```
# All of the trees around the edge of the grid are visible 

# look left
if j == 0 or np.amax(grid[i, :j]) < height:
# look right
elif j == columns - 1 or np.amax(grid[i, (j+1):]) < height:
# look up
elif i == 0 or np.amax(grid[:i, j]) < height:       
# look down
elif i == rows - 1 or np.amax(grid[(i+1):, j]) < height:
```
### --- Part Two ---
What is the highest scenic score possible for any tree?

**get_highest_scenic_score():** Returns scenic_score{int}

List of directions
```
# right, left, down, up
movement_directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
```
Loop through the grid
```
# get the tree height value
height = grid[i, j] # intersection
# Scan in 4 directions
for direction_i, direction_j in movement_directions:
    ii, jj = i + direction_i, j + direction_j
    distance = 0
    while (0 <= ii < rows and 0 <= jj < columns) and grid[ii, jj] < height:
        distance += 1
        ii += direction_i
        jj += direction_j
        # compensate when stopped inside the grid and current tree is >= height
        if (0 <= ii < rows and 0 <= jj < columns) and grid[ii, jj] >= height:
            # include it
            distance += 1
```









