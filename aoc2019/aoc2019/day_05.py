from .intcode import Intcode
from ._common import get_input


def part1():
    instructions = get_input('input/day5', transform=int, delim=',')
    intcode = Intcode('main', instructions, [1])
    intcode.compute()

    print(intcode.result)
    return intcode.result


def part2():
    instructions = get_input('input/day5', transform=int, delim=',')
    intcode = Intcode('main', instructions, [5])
    intcode.compute()

    print(intcode.result)
    return intcode.result
