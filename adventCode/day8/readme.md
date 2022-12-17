https://adventofcode.com/2022/day/8
### --- Day 8: Treetop Tree House ---

### --- Part One ---
How many trees are visible from outside the grid?
 
get_visible_trees_from_outside_grid():<br>
Returns visible_trees{int}
 
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


