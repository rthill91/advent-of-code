from ._common import get_input
from .intcode import Intcode


def part1(instructions=None, noun=12, verb=2):
    part2 = True
    if not instructions:
        instructions = get_input('input/day2', transform=int, delim=',')
        part2 = False

    instructions[1] = noun
    instructions[2] = verb

    intcode = Intcode('main', instructions, [])
    intcode.compute()


    if not part2:
        print(intcode._memory[0])
    return intcode._memory[0]


def part2():
    instructions = get_input('input/day2', transform=int, delim=',')

    for noun in range(100):
        for verb in range(100):
            res = part1(instructions, noun, verb)
            if res == 19690720:
                answer = 100 * noun + verb
                print(answer)
                return answer
