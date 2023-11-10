











with open('10/input.txt', 'r') as f:
    instructions = f.read().splitlines()
    
x = 1
cycles = []

for instruction in instructions:
    
    if instruction == 'noop':
        cycles.append(int(x))
        continue
    
    cycles.append(int(x))
    cycles.append(int(x))
    
    x += int(instruction.split(' ')[-1])

target_cycles = [20, 60, 100, 140, 180, 220]
total_sum = 0

for target_cycle in target_cycles:
    value = cycles[target_cycle-1]
    product = value * target_cycle
    # print(f"Target cycle: {target_cycle}, value: {value}")
    total_sum += product
    
# print(total_sum)   

image = []
row = []
for cycle, sprite_pos in enumerate(cycles):
    
    if abs(sprite_pos - cycle % 40) < 2:
        row.append('#')
    else:
        row.append('.')

    if (cycle + 1) % 40 == 0:
        image.append(row[:])
        row = []
        
output = '\n'.join([''.join(row) for row in image])
print(output)