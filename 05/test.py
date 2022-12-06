
from collections import deque
from collections import defaultdict
import re

with open('./05/test.txt') as input:
    stacks = defaultdict(deque)
    for line in input:
        if not line.startswith('['):
            next(input)
            break
        for n, i in enumerate(range(0, len(line)-2, 4)):
            content = line[i:i+3].strip()
            if content:
                stacks[n].appendleft(content[1])

    from copy import deepcopy
    stacks2 = deepcopy(stacks)

    for line in input:
        qty, from_, to = map(int, re.findall('\d+', line.strip('\n')))
        # part 1)
        for _ in range(qty):
            stacks[to-1].append(stacks[from_-1].pop())

        # part 2)
        tmp = deque()
        for _ in range(qty):
            tmp.appendleft(stacks2[from_-1].pop())
        stacks2[to-1].extend(tmp)
        
    print(''.join(stacks[i][-1] for i in range(len(stacks)))) # p1
    print(''.join(stacks2[i][-1] for i in range(len(stacks2)))) # p2