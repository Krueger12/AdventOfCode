import json

def get_folder(my_dict: dict, path: list):
    for folder in path:
        if folder not in my_dict:
            my_dict[folder] = {}
        my_dict = my_dict[folder]
    return my_dict

def find_smaller_limit(my_dict: dict, output: list = [], limit: int = 100000):
    for key, value in my_dict.items():
        if key == 'size' and value <= limit:
            output.append(value)
            
        if isinstance(value, dict):
            output = find_smaller_limit(value, output, limit)
        
    return output

def find_delete_folder(my_dict: dict, limit: int, current: int = 10000000000):
    for key, value in my_dict.items():
        if key == 'size' and value >= limit and value < current:
            current = value

        if isinstance(value, dict):
            current = find_delete_folder(value, limit, current)
            
    return current
    

# read input from '07/input.txt' to list 'commands'
with open('07/input.txt', 'r') as f:
    commands = f.read().splitlines()
    
folders = {}
current_folder = None
folder_path = []

# loop through commands
for i, command_str in enumerate(commands):
    
    # split command_str into its 'args'
    command = command_str.split(' ')
    
    # 'executing' commands start with $
    if command[0] == '$':
        
        # get the action
        if command[1] == 'cd':
            
            # get the folder name
            folder_name = command[2]
            
            # move up a folder if folder is '..' and store the size of the folder in the parent folder
            if folder_name == '..':
                sub_folder_size = current_folder['size']
                folder_path.pop()
                get_folder(folders, folder_path)['size'] += sub_folder_size
                
            else:
                # add the folder to path
                folder_path.append(folder_name)
                
            # get the folder
            current_folder = get_folder(folders, folder_path)
            
            # create size key if not existing
            if 'size' not in current_folder:
                current_folder['size'] = 0
                
            continue
        
    elif command[0] == 'dir':
        continue
    
    else:
        # left over are files, adding their size to the current folder           
        current_folder['size'] += int(command[0])
    
# in the end we need to add up to the root folder from the current folder
while len(folder_path) > 1:
    sub_folder_size = get_folder(folders, folder_path)['size']
    folder_path.pop()
    get_folder(folders, folder_path)['size'] += sub_folder_size
        

# get folders smaller 100000
small_folders_sizes = find_smaller_limit(folders)
print(sum(small_folders_sizes))

# get missing space
used_space = folders['/']['size']
total_space = 70000000
needed_space = 30000000
free_space = total_space - used_space
to_delete_space = needed_space - free_space

smallest_to_delete = find_delete_folder(folders, to_delete_space)
print(f"missing: {to_delete_space}, smallest: {smallest_to_delete}")        
            
with open('07/output.json', 'w') as f:
    f.write(json.dumps(folders, indent=4))        
    
                
            
            
    