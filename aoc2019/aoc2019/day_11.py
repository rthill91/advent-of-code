from dataclasses import dataclass
from enum import IntEnum
import logging

from .intcode import Intcode
from ._common import get_input



def part1():
    paint = run_robot(Color.BLACK)

    print(len(paint))
    return len(paint)


def part2():
    paint = run_robot(Color.WHITE)

    for y in range(0, -6, -1):
        for x in range(0, 50):
            if (color := paint.get((x, y))) is not None:
                # print(color)
                if color == Color.WHITE:
                    print('\u2588', end='')
                else:
                    print(' ', end='')
            else:
                print(' ', end='')
        print()



def run_robot(starting_color):
    robot = Robot()
    instructions = get_input('input/day11', transform=int, delim=',')

    paint = {}
    computer = Intcode('main', instructions, [starting_color])
    while computer.is_running:
        computer.compute()
        color, direction = computer.output_history[-2:]

        paint[robot.coords] = color
        if direction == Turn.LEFT:
            robot.turn_left()
        elif direction == Turn.RIGHT:
            robot.turn_right()
        else:
            raise Exception(f'invalid turn {direction}')

        computer.add_inputs([paint.get(robot.coords, Color.BLACK)])

    return paint


class Turn(IntEnum):
    LEFT = 0
    RIGHT = 1


class Color(IntEnum):
    BLACK = 0
    WHITE = 1


@dataclass
class Robot:
    x: int = 0
    y: int = 0
    _direction: int = 0

    @property
    def coords(self):
        return (self.x, self.y)

    def turn_left(self):
        self._direction -= 1
        if self._direction < 0:
            self._direction = 3
        self._move()

    def turn_right(self):
        self._direction += 1
        if self._direction > 3:
            self._direction = 0
        self._move()

    def _move(self):
        if self._direction == 0:
            self.y += 1
        elif self._direction == 1:
            self.x += 1
        elif self._direction == 2:
            self.y -= 1
        elif self._direction == 3:
            self.x -= 1
