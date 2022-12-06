import textwrap
import re

def parse_stacks(stacks_string):
    stacks_string = stacks_string.split('\n')[::-1]
    stacks_string = [textwrap.wrap(row, width=4, drop_whitespace=False) for row in stacks_string[1:]]
    
    stacks = [[] for _ in range(len(stacks_string[0]))]

    for row in stacks_string:
        for idx, crate in enumerate(row):
            crate = crate.strip(' []')
            if crate:
                stacks[idx].append(crate)
    
    return stacks

PROCEDURE_PATTERN = r"move (\d*) from (\d*) to (\d*)"
def parse_procedure(procedure_string):
    procedure = []

    for line in procedure_string.strip().split('\n'):
        m = re.match(PROCEDURE_PATTERN, line)
        procedure.append(tuple(map(int, m.groups())))

    return procedure

def execute_procedure(stacks, procedure):
    for order in procedure:
        reps, src, dest = order
        # print("--- order ---")
        # print(order)
        # print("--- before ---")
        # print(stacks[src-1])
        # print(stacks[dest-1])

        grabbed = []
        for _ in range(reps):
            grabbed.append(stacks[src-1].pop())
        stacks[dest-1].extend(grabbed[::-1])

        # print("--- after ---")
        # print(stacks[src-1])
        # print(stacks[dest-1])
        # print("--- ---")
        
    return stacks

with open("input.txt", 'r') as file:
    content = file.read()
    stacks, procedure = content.split('\n\n')

    stacks = parse_stacks(stacks)
    procedure = parse_procedure(procedure)

    stacks = execute_procedure(stacks, procedure)
    res = [stack[-1] for stack in stacks]
    print(''.join(res))