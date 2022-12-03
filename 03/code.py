

# read './03/input.txt' file line by line into a list
with open('./03/input.txt', 'r') as f:
    backpacks = f.readlines()

# give lower case letters a prio from 1 to 26 and upper case letters a prio from 27 to 52
def get_prio(char):
    if char.islower():
        return ord(char) - 96
    elif char.isupper():
        return ord(char) - 38
    
    
total = 0
for backpack in backpacks:
    
    # split in two halves
    half1, half2 = backpack[:len(backpack)//2], backpack[len(backpack)//2:]
    
    for item in half1:
        if item in half2:
            print(f"{item} {get_prio(item)}")
            total += get_prio(item)
            break
        
# print(total)

total = 0
i = 0
while i < len(backpacks) - 1:
    
    for item in backpacks[i]:
        if item in backpacks[i+1] and item in backpacks[i+2]:
            print(f"{item} {get_prio(item)}")
            total += get_prio(item)
            break
    
    i += 3

print(total)