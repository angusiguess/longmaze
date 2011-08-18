import sys

def read_grid():
	rows_cols = sys.stdin.readline()
	
	rows, cols = rows_cols.split(' ')
	rows = int(rows)
	cols = int(cols)
	
	grid = []
	
	for curr_row in range(rows):
		grid.append(sys.stdin.readline().rstrip())
		
	start_pos = []
	end_pos = []
	
	#Get the start and end positions in the grid.
	for curr_row in grid:
		for curr_col in curr_row:
			if curr_col == 'S':
				start_pos = curr_row.index(curr_col), grid.index(curr_row)
			elif curr_col == 'E':
				end_pos = curr_row.index(curr_col), grid.index(curr_row)
				
	return grid, start_pos, end_pos
