
with open('06/input.txt', 'r') as f:
        data = f.read()

last4found = False
index = 3
while index <= len(data) - 1:
    
    if not last4found:
        # get the last 4 characters
        last4 = data[index-3:index+1]
        
        # check if the last 4 characters are unique
        if len(set(last4)) == 4:
            print(f"last4: {last4}")
            print(f"last4 index: {index+1}")
            
            
    # get the last 14 characters
    if index >= 13:
        last14 = data[index-13:index+1]
    
        if len(set(last14)) == 14:
            print(f"last14: {last14}")
            print(f"last14 index: {index+1}")
            break
    
    index += 1