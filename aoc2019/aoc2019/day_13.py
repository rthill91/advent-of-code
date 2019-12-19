import curses
from enum import IntEnum

from ._common import get_input
from .intcode import Intcode


def part1():
    instructions = get_input('input/day13', transform=int, delim=',')
    computer = Intcode('arcade', instructions)
    computer.compute()

    display = {}
    it = iter(computer.output_history)
    for x in it:
        y = next(it)
        obj = next(it)
        if obj == GameObject.EMPTY:
            display.pop((x, y), None)
        else:
            display[(x, y)] = obj

    num_of_blocks = len([o for o in display.values() if o == GameObject.BLOCK])
    print(num_of_blocks)
    return num_of_blocks


def part2():
    curses.wrapper(part2_runner)


def part2_runner(stdscr):
    stdscr.clear()

    objects = {
        GameObject.EMPTY: ' ',
        GameObject.WALL: '\u2588',
        GameObject.BLOCK: '\u2584',
        GameObject.PADDLE: '\u2594',
        GameObject.BALL: '*',
    }

    instructions = get_input('input/day13', transform=int, delim=',')
    instructions[0] = 2
    computer = Intcode('arcade', instructions)

    _auto_play(computer)
    while computer.is_running:
        computer.compute()

        it = iter(computer.output_history)
        for x in it:
            y = next(it)
            obj = next(it)
            if _is_score(x, y):
                stdscr.addstr(30, 30, f'SCORE: {obj}')
            else:
                stdscr.addstr(y, x, objects.get(obj))

        stdscr.refresh()
        key = stdscr.getkey()
        if key == 'KEY_LEFT':
            computer.add_inputs([-1])
        elif key == 'KEY_RIGHT':
            computer.add_inputs([1])
        else:
            computer.add_inputs([0])


def _auto_play(computer):
    # This is horrible...
    computer.add_inputs(
          [0]  * 3
        + [1]  * 18
        + [-1] * 7
        + [0] * 7
        + [1] * 4
        + [0] * 3
        + [-1] * 5
        + [0] * 52
        + [-1] * 1
        + [0] * 250
        + [-1] * 23
        + [0] * 100
        + [1] * 9
        + [0] * 40
        + [-1] * 13
        + [0] * 8
        + [1] * 6
        + [0] * 44
        + [-1] * 1
        + [0] * 30
        + [1] * 5
        + [0] * 50
        + [1] * 4
        + [0] * 10
        + [1] * 8
        + [0] * 10
        + [-1] * 2
        + [0] * 2
        + [-1] * 10
        + [0] * 75
        + [-1] * 8
        + [0] * 150
        + [1] * 4
        + [0] * 10
        + [-1] * 1
        + [0] * 250
        + [1] * 7
        + [0] * 40
        + [1] * 2
        + [0] * 170
        + [-1] * 4
        + [0] * 100
        + [1] * 16
        + [0] * 91
        + [1] * 10
        + [0] * 14
        + [-1] * 12
        + [0] * 60
        + [-1] * 14
        + [0] * 60
        + [1] * 14
        + [0] * 23
        + [1] * 7
        + [0] * 72
        + [-1] * 30
        + [0] * 60
        + [1] * 32
        + [-1] * 31
        + [0] * 40
        + [1] * 32
        + [0] * 16
        + [1] * 1
        + [0] * 71
        + [-1] * 35
        + [1] * 12
        + [0] * 175
        + [1] * 10
        + [0] * 50
        + [-1] * 10
        + [0] * 80
        + [1] * 10
        + [0] * 15
        + [1] * 14
        + [0] * 37
        + [-1] * 36
        + [0] * 1
        + [1] * 35
        + [0] * 3
        + [-1] * 35
        + [0] * 4
        + [1] * 36
        + [-1] * 37
        + [0] * 2
        + [1] * 37
        + [-1] * 36
        + [0] * 3
        + [1] * 34
        + [0] * 4
        + [-1] * 32
        + [0] * 6
        + [1] * 24
        + [-1] * 24
        + [1] * 28
        + [0] * 5
        + [1] * 4
        + [-1] * 33
        + [0] * 6
        + [1] * 32
        + [0] * 6
        + [-1] * 31
        + [0] * 71
        + [1] * 32
        + [-1] * 34
        + [0] * 4
        + [1] * 35
        + [0] * 3
        + [-1] * 36
        + [0] * 2
        + [1] * 36
        + [0] * 2
        + [-1] * 35
        + [0] * 3
        + [1] * 34
        + [0] * 4
        + [-1] * 32
        + [0] * 6
        + [1] * 30
        + [0] * 8
        + [-1] * 28
        + [0] * 10
        + [1] * 26
        + [0] * 28
        + [-1] * 26
        + [0] * 11
        + [1] * 26
        + [0] * 13
        + [-1] * 1
        + [0] * 81
        + [1] * 1
        + [0] * 13
        + [-1] * 25
        + [0] * 13
        + [1] * 25
        + [0] * 13
        + [-1] * 24
        + [0] * 14
        + [1] * 22
        + [0] * 27
        + [-1] * 1
        + [0] * 16
        + [-1] * 12
        + [0] * 106
        + [1] * 5
        + [0] * 32
        + [-1] * 6
        + [0] * 13
        + [1] * 1
        + [0] * 19
        + [1] * 3
        + [0] * 6
        + [1] * 5
        + [0] * 2
        + [-1] * 1
        + [0] * 1
        + [-1] * 10
        + [0] * 28
        + [1] * 13
        + [0] * 23
        + [-1] * 1
        + [0] * 2
        + [-1] * 15
        + [0] * 16
        + [1] * 1
        + [0] * 3
        + [1] * 1
        + [-1] * 1
        + [0] * 1
        + [1] * 16
        + [0] * 10
        + [1] * 2
        + [0] * 5
        + [-1] * 1
        + [0] * 1
        + [-1] * 1
        + [0] * 1
        + [-1] * 17
        + [0] * 18
        + [-1] * 1
        + [0] * 2
        + [1] * 1
        + [-1] * 1
        + [0] * 1
        + [-1] * 1
        + [1] * 1
        + [-1] * 1
        + [1] * 5
    )


def _is_score(x, y):
    return x == -1 and y == 0


class GameObject(IntEnum):
    EMPTY = 0
    WALL = 1
    BLOCK = 2
    PADDLE = 3
    BALL = 4
