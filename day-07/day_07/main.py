import itertools
import logging

from .intcode import Intcode


logging.basicConfig(level=logging.CRITICAL)
LOGGER = logging.getLogger(__name__)


def part1():
    instructions = _get_input()

    highest = 0
    for phase in itertools.permutations(list("01234")):
        computer = Intcode('computer', instructions, [])
        for i in [int(i) for i in phase]:
            computer.reset_state([i, computer.result])
            computer.compute()

        highest = max(computer.result, highest)

    print(highest)
    assert highest == 92663


def part2():
    instructions = _get_input()

    highest = 0
    for phase in itertools.permutations(list("56789")):
        phase_list = [int(i) for i in phase]

        computer_a = Intcode("A", instructions, [phase_list[0]])
        computer_b = Intcode("B", instructions, [phase_list[1]])
        computer_c = Intcode("C", instructions, [phase_list[2]])
        computer_d = Intcode("D", instructions, [phase_list[3]])
        computer_e = Intcode("E", instructions, [phase_list[4]])
        computers = [computer_a, computer_b, computer_c, computer_d, computer_e]
        for _ in itertools.cycle(range(5)):
            computer = computers.pop(0)
            LOGGER.debug(f'{computer._phase_signal_pair=}')
            computer.add_inputs([computers[-1].result])
            LOGGER.debug(f'{computer._phase_signal_pair=}')
            is_done = computer.compute()
            if computer.name == 'E' and is_done:
                highest = max(highest, computer.result)
                break
            computers.append(computer)
            LOGGER.debug(f'{computer.result=}')

    print(highest)
    assert highest == 14365052


def _get_input():
    with open('input') as fh:
        return [int(inst) for inst in fh.readline().split(',')]
