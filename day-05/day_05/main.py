from .intcode import Intcode


def part1():
    instructions = _get_input()
    intcode = Intcode('main', instructions, [1])
    intcode.compute()

    assert intcode.result == 5821753
    print(intcode.result)


def part2():
    instructions = _get_input()
    intcode = Intcode('main', instructions, [5])
    intcode.compute()

    assert intcode.result == 11956381
    print(intcode.result)


def _get_input():
    with open('input') as fh:
        return [int(inst) for inst in fh.readline().split(',')]
