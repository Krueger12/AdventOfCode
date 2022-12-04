
# read './04/input.txt' file line by line into a list called 'pairs'
with open('./04/input_test.txt', 'r') as f:
    pairs = f.readlines()
    
# counter for valid pairs
counter = 0

part1 = False
# loop through the list
for pair in pairs:
    
    # split the line into two halves
    elf1, elf2 = pair.split(',')
    
    # split the halves into two lists of integers
    elf1 = [int(x) for x in elf1.split('-')]
    elf2 = [int(x) for x in elf2.split('-')]
    
    # part 1: check if one elf is in the range of the other elf
    
    # check if the range of one of the elfs is inside the range of the other
    if part1:
        if elf1[0] >= elf2[0] and elf1[1] <= elf2[1]:
            counter += 1
            continue
        
        if elf2[0] >= elf1[0] and elf2[1] <= elf1[1]:
            counter += 1
            continue
    
    # part 2: check if the ranges overlap
    else:
        if min(elf2) <= min(elf1) <= max(elf2) or min(elf2) <= max(elf1) <= max(elf2) or min(elf1) <= min(elf2) <= max(elf1) or min(elf1) <= max(elf2) <= max(elf1):
            counter += 1
            continue
    
print(counter)
    