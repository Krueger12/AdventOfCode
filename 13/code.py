from functools import cmp_to_key

def parse_input(path: str):
    with open(path) as f:
        content = f.read()
        text_pairs = [pair.split('\n') for pair in content.split('\n\n')]
        pairs = [[eval(item) for item in pair] for pair in text_pairs]
        return pairs
            



def compare(left: list, right: list):
    
    for i in range(max(len(left), len(right))):
        
        if i == len(left) and i < len(right):
            return True
        if i < len(left) and i == len(right):
            return False
        
        l, r = left[i], right[i]
        lt, rt = type(l), type(r)
        
        if lt == int and rt == int:
            if l < r:
                return True
            if l > r:
                return False
        
        elif lt == list and rt == list:
            sub_result = compare(l, r)
            if sub_result is not None:
                return sub_result
        
        else:
            if lt == int:
                l = [l]
                lt == list
            
            if rt == int:
                r = [r]
                rt == list

            sub_result = compare(l, r)
            if sub_result is not None:
                return sub_result
    
    return None
    









def part1(pairs):
    
    result = [int(compare(*pair)) for pair in pairs]
    return sum(i+1 for i, val in enumerate(result) if val)       
        
def part2(pairs):
    
    pairs = [item for pair in pairs for item in pair]
    pairs.extend([[[2]], [[6]]])
    pairs = sorted(pairs, key=cmp_to_key(lambda l, r: -1 if compare(l, r) else 1))
    index1, index2 = pairs.index([[2]]), pairs.index([[6]])
    return (index1+1) * (index2+1)






def solve():
    test_path = '13/test.txt'
    input_path = '13/input.txt'
    print("Part 1:")
    print(f"test: {part1(parse_input(test_path))}")
    print(f"result: {part1(parse_input(input_path))}")
    
    print("Part 2:")
    print(f"test: {part2(parse_input(test_path))}")
    print(f"result: {part2(parse_input(input_path))}")

if __name__ == '__main__':
    solve()