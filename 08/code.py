

def get_col(matrix, col):
    return [row[col] for row in matrix]

# read input from '08/input.txt' to list 'input'
with open('08/input.txt', 'r') as f:
    input = f.read().splitlines()
    
# transform into multidimensional array
trees = [[int(height) for height in line] for line in input]

# get maxes of row/col
max_col = len(trees)
max_row = len(trees[0])

visible_trees = 0
scenic_scores = []

# loop through trees
for row in range(len(trees)):
    for col in range(len(trees[0])):
        
        height = trees[row][col]
        
        # part 1
        
        # # get outermost trees | scenic score will be zero so continue
        # if col == 0 or row == 0 or col == max_col-1 or row == max_row-1:
        #     visible_trees += 1
        #     continue
        
        # get trees in row/col
        cur_col = get_col(trees, col)
        top_trees = cur_col[:row]
        bottom_trees = cur_col[row+1:]
        right_trees = trees[row][col+1:]
        left_trees = trees[row][:col]
        
        # # if max(top_trees) < height or max(right_trees) < height or max(bottom_trees) < height or max(left_trees) < height:
        #     visible_trees += 1
        #     continue
        
        
        # part 2
        

        # move in each direction until >= height or end of map
        temp_score = 1
        
        temp=0
        for lt in left_trees[::-1]:
            temp += 1
            if lt >= height:
                break
        temp_score *= temp
        
        temp=0
        for lt in right_trees:
            temp += 1
            if lt >= height:
                break
        temp_score *= temp
            
        temp=0
        for lt in top_trees[::-1]:
            temp += 1
            if lt >= height:
                break
        temp_score *= temp
            
        temp=0
        for lt in bottom_trees:
            temp += 1
            if lt >= height:
                break
        temp_score *= temp
        
        scenic_scores.append(temp_score)    
        
        
print(visible_trees)
print(max(scenic_scores))
