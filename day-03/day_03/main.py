from dataclasses import dataclass
import math

@dataclass(frozen=True)
class Point:
    x: int
    y: int
    i: int = 0

    def up(self):
        return Point(self.x + 1, self.y, self.i + 1)

    def down(self):
        return Point(self.x - 1, self.y, self.i + 1)

    def left(self):
        return Point(self.x, self.y - 1, self.i + 1)

    def right(self):
        return Point(self.x, self.y + 1, self.i + 1)

    def get_distance(self, point):
        return abs(self.x - point.x) + abs(self.y - point.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))


def part1():
    origin = Point(0,0)
    wire1_moves, wire2_moves = _get_input()

    wire1 = _get_wire(origin, wire1_moves)
    wire2 = _get_wire(origin, wire2_moves)

    shortest_dist = math.inf
    for p in wire1.intersection(wire2):
        dist = origin.get_distance(p)
        if dist < shortest_dist:
            shortest_dist = dist

    assert shortest_dist == 2180
    print(shortest_dist)


def part2():
    origin = Point(0,0)
    wire1_moves, wire2_moves = _get_input()

    wire1 = _get_wire(origin, wire1_moves)
    wire2 = _get_wire(origin, wire2_moves)

    shortest_dist = math.inf
    for p in wire1.intersection(wire2):
        p1 = next(p1 for p1 in list(wire1) if p1 == p)
        p2 = next(p2 for p2 in list(wire2) if p2 == p)
        sum_dist = p1.i + p2.i
        if sum_dist < shortest_dist:
            shortest_dist = sum_dist

    assert shortest_dist == 112316
    print(shortest_dist)


def _get_input():
    wires = []
    with open('input') as fh:
        return (fh.readline().split(','), fh.readline().split(','))


def _get_wire(origin, moves):
    cur_point = origin
    wire = set()

    for move in moves:
        direction, distance = _parse_move(move)
        for _ in range(distance):
            if direction == 'U':
                cur_point = cur_point.up()
            elif direction == 'D':
                cur_point = cur_point.down()
            elif direction == 'L':
                cur_point = cur_point.left()
            elif direction == 'R':
                cur_point = cur_point.right()
            wire.add(cur_point)

    return wire


def _parse_move(move):
    direction = move[0]
    distance = int(move[1:])
    return (direction, distance)
