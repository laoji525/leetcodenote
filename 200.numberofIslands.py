def nOI(self, grid):
	if not grid:
		return 0
	row = len(grid)
	col = len(grid[0])
	islands = 0
	for r in range(row):
		for c in range(col):
			if grid[r][c] == '1':
				islands += 1
				self.setIsland(r, c, grid)
	return islands
	
def setIsland(self, r, c, grid):
	if r => len(grid) or r < 0 or c >= len(grid[0]) or c < 0:
		return
	if grid[r][c] != '1':
		return
	grid[r][c] = '0'
	self.setIsland(r+1, c, grid)
	self.setIsland(r-1, c, grid)
	self.setIsland(r, c+1, grid)
	self.setIsland(r, c-1, grid)
