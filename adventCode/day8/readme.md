https://adventofcode.com/2022/day/8
### --- Day 8: Treetop Tree House ---

### --- Part One ---
How many trees are visible from outside the grid?
<span style="color:#013b5e">
get_visible_trees_from_outside_grid():<br>
Returns visible_trees{int}
</span>
<span style="color:#0476bd">Ingest puzzle input</span>
```
grid = [list(map(int, list(line))) for line in lines]
```
<span style="color:#0476bd">Use NumPy to create a 2D Array</span>
```
grid = np.array(grid)
```
<span style="color:#0476bd">Loop through grid</span>
 
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


