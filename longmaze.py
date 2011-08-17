import sys

longest_path = 0

def find_paths(grid, start, end):
	candidate = []
	candidate.append(start)
	backtrack_path(grid, start, end, candidate)
	
def process_solution(candidate, rows, cols):
	print len(candidate)
	out_string = []
	for i in range(rows):
		out_string.append(list('#' * cols))
	for curr_coord in candidate:
		y, x = curr_coord
		out_string[x][y] = '.'
	
	for curr_line in out_string:
		print ''.join(curr_line)
	print ""
		
		
		
def backtrack_path(grid, start, end, candidate):
	rows = len(grid)
	cols = len(grid[0])
	
	global longest_path
	
	if is_complete(candidate, end):
		if len(candidate) >= longest_path:
			longest_path = len(candidate)
			process_solution(candidate, rows, cols)
		return
	
	for i in range(-1, 2, 1):
		new_move = candidate[-1][0] + i, candidate[-1][1]
		next_candidate = candidate[:]
		next_candidate.append(new_move)
	
		if is_valid(next_candidate, rows, cols):
			backtrack_path(grid, start, end, next_candidate)
		new_move = candidate[-1][0], candidate[-1][1] + i
		next_candidate = candidate[:]
		next_candidate.append(new_move)
		if is_valid(next_candidate, rows, cols):
			backtrack_path(grid, start, end, next_candidate)
			
def is_complete(candidate, end):
	if candidate[-1] == end:
		return True
	return False
		
	
		
		
	
def is_valid(candidate, rows, cols):
	cand_set = set(candidate)
	if len(cand_set) < len(candidate):
		return False
	if candidate[-1] in candidate[:-1]:
		return False
	
	last_move = candidate[-1]
		
	if last_move[0] < 0 or last_move[0] >= rows:
		return False
		
	if last_move[1] < 0 or last_move[1] >= cols:
		return False
	
	adjacencies = 0
	for move in candidate[:-1]:
		#distance = [a - b for a, b in zip(move, candidate[-1])]
		#distance = [abs(i) for i in distance]
		deltax = abs(move[0] - candidate[-1][0])
		deltay = abs(move[1] - candidate[-1][1])
		distance = deltax, deltay
		
		
		if distance == (0, 1) or distance == (1, 0):
			adjacencies += 1
	
	if adjacencies > 1:
		return False
	
	return True
	
			
		
	

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
			
print start_pos
print end_pos
			
find_paths(grid, start_pos, end_pos)	