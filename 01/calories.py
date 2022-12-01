# ---------------------------------------------------------------------
# PART 1: Elf with most calories
# ---------------------------------------------------------------------

# read 'input.txt' file line by line into a list
with open('input.txt', 'r') as f:
    lines = f.readlines()
    
# result list
elfs = []

# current calories
calories = 0
    
# loop through the list
for i, line in enumerate(lines):
    
    # add numbers up until first empty line or end of file
    if line == '\n' or i == len(lines) - 1:
        elfs.append(calories)
        calories = 0
    
    else:
        calories += int(line.replace('\n', ''))

# get the highest number
max_calories = max(elfs)
print(max_calories)

# ---------------------------------------------------------------------
# PART 2: Top 3 elves with most calories
# ---------------------------------------------------------------------

# sort the list
elfs_sorted = sorted(elfs, reverse=True)

# get the top 3
top_3 = elfs_sorted[:3]
top_3_sum = sum(top_3)

print(top_3_sum)