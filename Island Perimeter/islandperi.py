*****************************************************************************
You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

 

Example:

Input:
[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Output: 16

*****************************************************************************
class Solution:    
        def islandPerimeter(self, grid):
            def land_around(x,y): 
                return  ((y != 0 and grid[x][y-1] == 1) + 
                         (y != len(grid[0])-1   and grid[x][y+1] == 1) +
                         (x!= 0  and grid[x-1][y] == 1) +
                         (x != len(grid)-1 and grid[x+1][y] == 1))
            return sum(4-land_around(x,y) for x in range(len(grid)) for y in range(len(grid[0])) if grid[x][y])
        
