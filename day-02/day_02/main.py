from .intcode import Intcode


def part1(instructions=None, noun=12, verb=2):
    part2 = True
    if not instructions:
        instructions = _get_input()
        part2 = False

    instructions[1] = noun
    instructions[2] = verb

    intcode = Intcode('main', instructions, [])
    intcode.compute()


    if part2:
        return intcode._instructions[0]
    assert intcode._instructions[0] == 11590668
    print(intcode._instructions[0])


def part2():
    instructions = _get_input()

    for noun in range(100):
        for verb in range(100):
            res = part1(instructions, noun, verb)
            if res == 19690720:
                answer = 100 * noun + verb
                assert answer == 2254
                print(answer)
                return


def _get_input():
    with open('input') as fh:
        return [int(inst) for inst in fh.readline().split(',')]
