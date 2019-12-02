def part1():
    opcodes = {
        1: _add,
        2: _multiply,
    }

    with open('input') as fh:
        instructions = [int(inst) for inst in fh.readline().split(',')]

    instructions[1] = 12
    instructions[2] = 2
    index = 0
    while index < len(instructions):
        inst = instructions[index]
        if inst == 99:
            break
        op = opcodes.get(inst, None)
        op(index, instructions)
        index += 4
    print(instructions)



def part2():
    raise NotImplementedError


def _add(index, instructions):
    oper1 = instructions[index+1]
    oper2 = instructions[index+2]
    dest = instructions[index+3]
    instructions[dest] = instructions[oper1] + instructions[oper2]


def _multiply(index, instructions):
    oper1 = instructions[index+1]
    oper2 = instructions[index+2]
    dest = instructions[index+3]
    instructions[dest] = instructions[oper1] * instructions[oper2]
