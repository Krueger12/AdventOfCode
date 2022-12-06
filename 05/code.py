import re

# get the stacks from './05/stacks.txt' and store them in a list
with open('./05/stacks.txt', 'r') as f:
    stacks_raw = f.read().splitlines()

# get only the values
stacks_raw2 = []
for i, line in enumerate(stacks_raw):
    new_line = []
    for j, char in enumerate(line):
        if j == 1 or (j-1) % 4 == 0:
            new_line.append(char)
    stacks_raw2.append(new_line)
    
# convert rows into columns
stacks = []
for i in range(len(stacks_raw2[0])):
    stacks.append([])
    for line in reversed(stacks_raw2):
        if line[i] != ' ':
            stacks[i].append(line[i])
    
# get the moves from './05/moves.txt' and store them in a list
with open('./05/moves.txt') as f:
    moves_raw = f.readlines()

# get only the values
moves = []
for raw_move in moves_raw:
    move = re.findall(r'\d+', raw_move.strip('\n'))
    moves.append(move)

# move the crates
for move in moves:
    amount = int(move[0])
    src_index = int(move[1]) - 1 
    trgt_index = int(move[2]) - 1
    
    # part 1: move the crates one by one
    # for i in range(amount):
    #     stacks[trgt_index].append(stacks[src_index].pop())
    
    # part 2: move the crates all at once
    stacks[trgt_index].extend(stacks[src_index][-amount:])
    del stacks[src_index][-amount:]

    
        
# get the last item in each stack
output = [stack.pop() for stack in stacks]
output = ''.join(output)
    
    
print(output)