import sys, time

def get_new_knot_positions(knot_positions):
    
    for index in range(len(knot_positions)-1):
        
        h = knot_positions[index]
        t = knot_positions[index+1]
    
        dx = h[0] - t[0]
        dy = h[1] - t[1]
        
        # cases
        if abs(dx) == 2 and dy == 0:
            if dx > 0:
                t[0] += 1
            else:
                t[0] -= 1
        
        elif abs(dy) == 2 and dx == 0:
            if dy > 0:
                t[1] += 1
            else:
                t[1] -= 1
        
        elif (abs(dy) == 2 and abs(dx) > 0) or (abs(dx) == 2 and abs(dy) > 0):
            if dx > 0:
                t[0] += 1
            else:
                t[0] -= 1
            
            if dy > 0:
                t[1] += 1
            else:
                t[1] -= 1
    
    return knot_positions

def render(sleep_time=0):
    # get the matrix size
    all_x = [knot[0] for knots in history for knot in knots]
    all_y = [knot[1] for knots in history for knot in knots]

    max_x = max(all_x)
    min_x = min(all_x)
    max_y = max(all_y)
    min_y = min(all_y)

    # noramlize positions
    for knots in history:
        for knot in knots:
            knot[0] -= min_x
            knot[1] -= min_y

    max_x -= min_x
    max_y -= min_y

    out = sys.stdout
    out.flush()
    
    matrix = [['.' for x in range(min_x, max_x+1)] for y in range(min_y, max_y+1)]

    for knot_positions in history:
        for x in range(min_x, max_x+1):
            for y in range(min_y, max_y+1):
                
                
                try:
                    knot_index = knot_positions.index([x,y])
                except ValueError:
                    knot_index = None
                
                if knot_index is None:
                    matrix[y][x] = '.'
                    if x == abs(min_x) and y == abs(min_y):
                        matrix[y][x] = 'S'
                else:
                    if knot_index == 0:
                        matrix[y][x] = 'H'
                    elif knot_index == len(knot_positions)-1:
                        matrix[y][x] = 'T'
                    else:
                        matrix[y][x] = str(knot_index)
                        
                if (x+min_x,y+min_y) in t_visited:
                    matrix[y][x] = '#'
        
        output = '\033[H' + '\n'*10 + '\n'.join([''.join(row) for row in matrix])
        out.write(output)
        time.sleep(sleep_time)
        

# ------------------- 
# Script
# -------------------

# read input from '09/input.txt' to list 'commands'
with open('09/input.txt', 'r') as f:
    moves = f.read().splitlines()
    

# set start positions
knots = 9
knot_positions = [[0,0] for i in range(knots)]

# visited positions by the tail
h_visited = [(0,0)]
t_visited = [(0,0)]
history = [tuple([pos[:] for pos in knot_positions])]

# loop through moves
for move in moves:
    
    move = move.split(' ')
    direction, length = move[0], int(move[1])
    
    # doing one step at a time
    for i in range(length):
        
        # first move the head
        if direction == 'U':
            knot_positions[0][1] += 1
        elif direction == 'D':
            knot_positions[0][1] -= 1
        elif direction == 'L':
            knot_positions[0][0] -= 1
        elif direction == 'R':
            knot_positions[0][0] += 1
        
        # move the tail accordingly
        knot_positions = get_new_knot_positions(knot_positions)
        
        
        # append the new positions
        h_visited.append(tuple(knot_positions[0][::]))
        t_visited.append(tuple(knot_positions[-1][::]))
        history.append(tuple([pos[:] for pos in knot_positions]))
        
        

# get unique positions of the tail
# print(set(t_visited))
print(len(set(t_visited)))
# print(history)

# render the path

render(0.1)



                
