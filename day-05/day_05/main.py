import copy


def part1(additional_opcodes=None):
    opcodes = {
        '01': (_add, 4),
        '02': (_multiply, 4),
        '03': (_input, 2),
        '04': (_output, 2),
    }
    if additional_opcodes:
        opcodes.update(additional_opcodes)

    instructions = _get_input()

    index = 0
    while index < len(instructions):
        inst = instructions[index]
        inst = str(inst).zfill(4)
        operation = inst[-2:]
        modes = inst[:-2]
        if operation == '99':
            break
        op, inst_length = opcodes.get(operation, None)
        modes = modes.zfill(inst_length)
        new_index = op(index, instructions, modes)
        if new_index > 0:
            index = new_index
        else:
            index += inst_length


def part2():
    opcodes = {
        '05': (_jump_if_true, 3),
        '06': (_jump_if_false, 3),
        '07': (_less_than, 4),
        '08': (_equals, 4),
    }
    part1(additional_opcodes=opcodes)


def _add(index, instructions, modes):
    noun = _get_value(instructions[index+1], instructions, modes[-1])
    verb = _get_value(instructions[index+2], instructions, modes[-2])
    dest = instructions[index+3]
    instructions[dest] = noun + verb
    return 0


def _multiply(index, instructions, modes):
    noun = _get_value(instructions[index+1], instructions, modes[-1])
    verb = _get_value(instructions[index+2], instructions, modes[-2])
    dest = instructions[index+3]
    instructions[dest] = noun * verb
    return 0


def _input(index, instructions, modes):
    number = input("Input: ")
    dest = instructions[index+1]
    instructions[dest] = int(number)
    return 0


def _output(index, instructions, modes):
    output_location = instructions[index+1]
    print(instructions[output_location])
    return 0


def _jump_if_true(index, instructions, modes):
    noun = _get_value(instructions[index+1], instructions, modes[-1])
    verb = _get_value(instructions[index+2], instructions, modes[-2])
    if noun != 0:
        return verb
    return 0


def _jump_if_false(index, instructions, modes):
    noun = _get_value(instructions[index+1], instructions, modes[-1])
    verb = _get_value(instructions[index+2], instructions, modes[-2])
    if noun == 0:
        return verb
    return 0


def _less_than(index, instructions, modes):
    noun = _get_value(instructions[index+1], instructions, modes[-1])
    verb = _get_value(instructions[index+2], instructions, modes[-2])
    dest = instructions[index+3]
    if noun < verb:
        instructions[dest] = 1
    else:
        instructions[dest] = 0
    return 0


def _equals(index, instructions, modes):
    noun = _get_value(instructions[index+1], instructions, modes[-1])
    verb = _get_value(instructions[index+2], instructions, modes[-2])
    dest = instructions[index+3]
    if noun == verb:
        instructions[dest] = 1
    else:
        instructions[dest] = 0
    return 0


def _get_value(value, instructions, mode):
    if mode == "0":
        return instructions[value]
    return value


def _get_input():
    with open('input') as fh:
        return [int(inst) for inst in fh.readline().split(',')]
