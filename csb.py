def add(a, b):
    return a+b
def sub(a, b):
    return a-b
def mul(a, b):
    return a*b
def div(a, b):
    return a//b
def mod(a, b):
    return a%b

instruction2 = {
    'ADD':add,
    'SUB':sub,
    'MUL':mul,
    'DIV':div,
    'MOD':mod,
}

def if_f(s):
    return pop(s) != 0
def pop(s):
    return s.pop()
def dup(s):
    s.append(s[-1])
def swp(s):
    s[-1],s[-2] = s[-2],s[-1]
def rot(s):
    s[-3],s[-2] = s[-2],s[-3]
    swp(s)
def ovr(s):
    s.append(s[-2])
def pos(s):
    s.append(pop(s) >= 0 and 1 or 0)
def not_f(s):
    s.append(pop(s) == 0 and 1 or 0)
def out(s):
    print(pop(s))
instruction1 = {
    'POP':pop,
    'DUP':dup,
    'SWP':swp,
    'ROT':rot,
    'OVR':ovr,
    'POS':pos,
    'NOT':not_f,
    'OUT':out,
}

functions = {}
def_func = ''
stack_data = []

def extract_if(i, instructions, data, is_if):
    l = len(instructions)
    if_count = 0 if is_if else 1
    while i < l:
        instruction = instructions[i]
        i += 1
        if instruction == 'IF':
            if_count += 1
        if instruction == 'FI':
            if_count -= 1
            if if_count <= 0:
                if is_if:
                    i -= 1
                break
        if instruction != 'ELS':
            data.append(instruction)
        else:
            if is_if:
                i -= 1
                break
    return i

def exec_if(s, i, instructions):
    f = if_f(s)
    if_l = []
    else_l = []
    l = len(instructions)

    j = extract_if(i+1, instructions, if_l, True)

    def had_els(k):
        # return False
        # if f: return False
        while k < l:
            if instructions[k] == 'ELS':
                return True
            k += 1
        return False

    if had_els(j):
        j = extract_if(j+1, instructions, else_l, False)
    exec_l = if_l if f else else_l
    process_nest(exec_l, s)
    return j

def process_nest(instructions, s):
    j = 0
    while j < len(instructions):
        ins = instructions[j]
        if ins == 'IF':
            j = exec_if(s, j, instructions)
        else:
            process(ins, s)
        j += 1

def process(instruction, s=[]):
    if instruction.lstrip('-').isdigit():
        s.append(int(instruction))
    elif instruction in instruction2.keys():
        a = s.pop()
        b = s.pop()
        s.append(instruction2[instruction](b, a))
    elif instruction in instruction1.keys():
        instruction1[instruction](s)
    elif instruction in functions:
        functions_ins = functions[instruction]
        process_nest(functions_ins, s)

with open('csb.txt') as file:
    lines = file.readlines()[1:]
    lines = [line.strip().split() for line in lines]

# n = int(input())
# lines = [input().split() for _ in range(n)]
# print(*lines)
instructions = []
for line in lines:
    instructions += line + ['\n']

print(instructions)

i = 0
instructions_len = len(instructions)
while i < instructions_len:
    instruction = instructions[i]
    if instruction == 'DEF':
        def_func = instructions[i+1]
        functions[def_func] = []
        i += 1
    elif instruction == 'END':
        def_func = ''
    elif def_func != '':
        functions[def_func].append(instruction)
    # elif instruction == '\n':
    #     stack_data = []
    elif def_func == '':
        if instruction == 'IF':
            i = exec_if(stack_data, i, instructions)
        else:
            process(instruction, stack_data)
    i += 1