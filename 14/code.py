import sys
from copy import deepcopy
from time import sleep

def generate_grid(path, part = 1):
    with open(path) as f:
        content = f.read()
        
    stone_paths = content.splitlines()
    stone_paths = [[(int(x), int(y)) for x, y in [coord.split(',') for coord in path.split(' -> ')]] for path in stone_paths]
    min_x = min(x for path in stone_paths for x, y in path)
    max_x = max(x for path in stone_paths for x, y in path)
    max_y = max(y for path in stone_paths for x, y in path)
    
    if part == 2:
        min_x -= 500
        max_x += 500
        
    start = 500 - min_x, 0
    
    grid = [['.' for x in range(min_x, max_x + 1)] for y in range(max_y + 1)]
    
    for path in stone_paths:
        for i in range(len(path)-1):
            x1, y1 = path[i]
            x2, y2 = path[i+1]
            x_start, x_end = min(x1, x2), max(x1, x2)
            y_start, y_end = min(y1, y2), max(y1, y2)
            for x in range(x_start, x_end + 1):
                for y in range(y_start, y_end + 1):
                    grid[y][x - min_x] = '#'
                    
    if part == 2:
        grid.append(['.' for x in range(len(grid[0]))])
        grid.append(['#' for x in range(len(grid[0]))])
    
    grid[start[1]][start[0]] = '+'
    
    return grid, start
    

def render(grid):
    sys.stdout.flush()
    output = '\033[H' + '\n'*2 + '\n'.join([''.join(row) for row in grid])
    sys.stdout.write(output)
    

def simulate(empty_grid, start, do_render = True):
    orig_grid = deepcopy(empty_grid)
    ax, ay = deepcopy(start)
    run = True
    while run:
        if do_render:
            grid = deepcopy(orig_grid)
        if orig_grid[start[1]][start[0]] == 'O':
            run = False
            continue
        if ax-1 < 0 or ax+1 >= len(orig_grid[0]) or ay+1 >= len(orig_grid):
            run = False
            continue
        dl, dc, dr = orig_grid[ay+1][ax-1], orig_grid[ay+1][ax], orig_grid[ay+1][ax+1]
        if dc == '.':
            ay += 1
        elif dl == '.':
            ax -= 1
            ay += 1
        elif dr == '.':
            ax += 1
            ay += 1
        else:
            orig_grid[ay][ax] = 'O'
            ax, ay = deepcopy(start)
            continue
        if do_render:
            grid[ay][ax] = 'O'    
            render(grid)
            sleep (0.01)
    render(orig_grid)
    return orig_grid

        
part = 2    
grid, start = generate_grid('14/input.txt', part)

grid = simulate(grid, start, False)


count = sum(1 for row in grid for cell in row if cell == 'O')
print(count)