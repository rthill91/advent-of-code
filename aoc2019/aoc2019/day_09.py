from ._common import get_input
from .intcode import Intcode

import logging

# logging.basicConfig(level=logging.DEBUG)


def part1():
    instructions = get_input('input/day9', transform=int, delim=',')
    computer = Intcode('main', instructions, [1])
    computer.compute()
    print(computer.result)
    return computer.result


def part2():
    instructions = get_input('input/day9', transform=int, delim=',')
