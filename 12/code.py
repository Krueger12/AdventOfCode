import string
from collections import deque
from dataclasses import dataclass
import sys
import time


def parse(path):
    char_vals = string.ascii_lowercase
    with open(path) as f:
        lines = f.read().splitlines()
        return [[char_vals.find(char) if char in char_vals else char for char in line] for line in lines]
    
def get_location_pos(grid, char):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == char:
                return (i, j)
            
def render_history(grid, history):
    out = sys.stdout
    out.flush()
    for pos in history:
        x, y = pos
        grid[x][y] = 'X'
        output = '\033[H' + '\n'*10 + '\n'.join([''.join(str(item) for item in row) for row in grid]) + '\n'*10
        out.write(output)
        time.sleep(0.01)

def bfs(grid, start_pos, end_pos):
    visited = set()
    history = []
    q = deque()
    q.append((start_pos, 0))
    visited.add(start_pos)
    while q:
        pos, dist = q.popleft()
        history.append(pos)
        if pos == end_pos:
            return dist, history
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_pos = (pos[0] + dx, pos[1] + dy)
            x, y = pos
            nx, ny = new_pos
            if new_pos not in visited and 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] <= grid[x][y] + 1:
                q.append((new_pos, dist + 1))
                visited.add(new_pos)
                
    return -1, []
    
def part_1(grid):
    start_pos = get_location_pos(grid, 'S')
    end_pos = get_location_pos(grid, 'E')
    grid[start_pos[0]][start_pos[1]] = 0
    grid[end_pos[0]][end_pos[1]] = 25
    
    result, history = bfs(grid, start_pos, end_pos)
    render_history(grid, history)
    return result

def part_2(grid):
    start_pos = get_location_pos(grid, 'S')
    end_pos = get_location_pos(grid, 'E')
    grid[start_pos[0]][start_pos[1]] = 0
    grid[end_pos[0]][end_pos[1]] = 25
    
    starting_points = []
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y] == 0:
                starting_points.append((x, y))
    
    steps = []
    for start in starting_points:
        result, history = bfs(grid, start, end_pos)
        if result != -1:
            steps.append(result)
    return min(steps)

def run(part):
    grid = parse('12/input.txt')
    if part == 1:
        print(part_1(grid))
        
    if part == 2:
        print(part_2(grid))
        
        
    
    
if __name__ == '__main__':
    run(2)


    
