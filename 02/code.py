"""
this is not a good solution, but its a solution.
the mapping went a little bit out of hand
"""

# ---------------------------------------------------------------------
# PART 1: Following the strategy guide
# Rock - A | X - 1 Point
# Paper - B | Y - 2 Points
# Scissors - C | Z - 3 Points
# loss - 0 Points
# draw - 3 Points
# win - 6 Points
# ---------------------------------------------------------------------

# create a point map list
"""
    X   Y   Z
A   3   0   6
B   6   3   0
C   0   6   3
"""
win_map = [
    [3,6,0], 
    [0,3,6], 
    [6,0,3]
]

point_map = {
    'X': 1,
    'Y': 2,
    'Z': 3
}

# map chars to indexes
char_map = {
    'A': 0,
    'B': 1,
    'C': 2,
    'X': 0,
    'Y': 1,
    'Z': 2
}

# read 'input.txt' file line by line into a list
with open('./02/input.txt', 'r') as f:
    rounds = f.readlines()

# total points
total_points = 0

# loop through the rounds
for round in rounds:
    enemy, me = round.replace('\n', '').split(' ')
    result_points = win_map[char_map[enemy]][char_map[me]]
    type_points = point_map[me]
    total_points += result_points + type_points
    
print(total_points)

# ---------------------------------------------------------------------
# PART 2: Win/ Loose/ Draw as given in the strategy guide
# X - loss
# Y - draw
# Z - win
# ---------------------------------------------------------------------

# create maps
result_map = {
    'X': 0,
    'Y': 3,
    'Z': 6
}
index_map = ['X', 'Y', 'Z']

# total points
total_points = 0

# loop through the rounds
for round in rounds:
    enemy, result = round.replace('\n', '').split(' ')
    me = index_map[win_map[char_map[enemy]].index(result_map[result])]
    total_points += result_map[result] + point_map[me]

print(total_points)

