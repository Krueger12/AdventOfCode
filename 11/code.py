from dataclasses import dataclass


@dataclass
class Item():
    worry_level: int    

@dataclass
class Monkey():
    
    items: list[Item]
    operation: list[str]
    divisor: int
    t_target: int
    f_target: int
    inspection_count: int = 0
    global monkeys
    
    def inspect(self):
        
        self.inspection_count += 1
        item = self.items[0]
        first_val, operation_type, second_val = self.operation
        
        if first_val == 'old':
            first_val = item.worry_level
        if second_val == 'old':
            second_val = item.worry_level
        
        first_val, second_val = int(first_val), int(second_val)
        
        if operation_type == "+":
            item.worry_level = first_val + second_val
        elif operation_type == "*":
            item.worry_level = first_val * second_val
            
    def get_bored(self):
        
        self.items[0].worry_level = self.items[0].worry_level // 3
        
    def throw(self):
        
        if self.items[0].worry_level % self.divisor == 0:
            monkeys[self.t_target].items.append(self.items[0])
        else:
            monkeys[self.f_target].items.append(self.items[0])
        
        self.items.pop(0)
        
    def play_turn(self, part_nr: int = 1):
        
        while len(self.items) > 0:
            self.inspect()
            if part_nr == 1:
                self.get_bored()
            self.throw()

monkeys: list[Monkey] = []

# parse input
with open('11/test.txt') as f:
    lines = f.read()
    
blocks = lines.split('\n\n')

for block in blocks:
    lines = block.split('\n')
    items = [Item(int(level)) for level in lines[1].split(': ')[1].split(', ')]
    operation = lines[2].split(': ')[1].split('= ')[1].split(' ')
    divisor = int(lines[3].split(' ')[-1])
    t_target = int(lines[4].split(' ')[-1])
    f_target = int(lines[5].split(' ')[-1])
    
    monkeys.append(Monkey(items, operation, divisor, t_target, f_target))
    
# part 1

# # play game
# for round in range(20):
#     for monkey in monkeys:
#         monkey.play_turn()
        
# part 2

# play game
for round in range(20):
    for monkey in monkeys:
        monkey.play_turn(2)
        
# print results
for monkey in monkeys:
    print(f"Monkey {monkeys.index(monkey)} inspected {monkey.inspection_count} items")
inspections = [monkey.inspection_count for monkey in monkeys]
inspections.sort(reverse=True)
print(inspections[0] * inspections[1])



    