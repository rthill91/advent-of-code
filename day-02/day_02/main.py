import copy


def part1(instructions=None, noun=12, verb=2):
    opcodes = {
        1: _add,
        2: _multiply,
    }

    part2 = True
    if not instructions:
        part2 = False
        instructions = _get_input()

    instructions[1] = noun
    instructions[2] = verb
    index = 0
    while index < len(instructions):
        inst = instructions[index]
        if inst == 99:
            break
        op = opcodes.get(inst, None)
        op(index, instructions)
        index += 4


    if not part2:
        assert instructions[0] == 11590668
        print(instructions[0])
    return instructions[0]



def part2():
    instructions = _get_input()

    for noun in range(100):
        for verb in range(100):
            res = part1(copy.copy(instructions), noun, verb)
            if res == 19690720:
                answer = 100 * noun + verb
                assert answer == 2254
                print(answer)
                return


def _add(index, instructions):
    noun = instructions[index+1]
    verb = instructions[index+2]
    dest = instructions[index+3]
    instructions[dest] = instructions[noun] + instructions[verb]


def _multiply(index, instructions):
    noun = instructions[index+1]
    verb = instructions[index+2]
    dest = instructions[index+3]
    instructions[dest] = instructions[noun] * instructions[verb]


def _get_input():
    with open('input') as fh:
        return [int(inst) for inst in fh.readline().split(',')]
