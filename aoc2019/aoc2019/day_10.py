from dataclasses import dataclass
import math
from decimal import Decimal

from ._common import get_input


@dataclass
class Asteroid:
    x: int
    y: int
    detectable_count: int = 0


def part1():
    asteroid_map = get_input('input/day10')
    asteroids = []
    for y, line in enumerate(asteroid_map):
        for x, element in enumerate(line):
            if element == '#':
                asteroids.append(Asteroid(x, y))

    for station in asteroids:
        count = _calculate_visible_asteroids(station, asteroids)
        station.detectable_count = count

    best = max((a for a in asteroids), key=lambda a: a.detectable_count)
    print(best)
    return best



def part2():
    pass


def _calculate_visible_asteroids(station, asteroids):
    angles = []
    for asteroid in asteroids:
        if station is asteroid:
            continue
        angle = _calculate_angle(station, asteroid)
        angles.append(angle)
    return len(set(angles))


def _calculate_angle(p1, p2):
    return math.atan2(p2.y - p1.y, p2.x - p1.x) * 180


def _get_distance(p1, p2):
    return Decimal(math.sqrt((p2.x - p1.x)**2 + (p2.y - p1.y)**2))


def _get_angle(d1, d2, d3):
    cos_d1 = round((d2**2 + d3**2 - d1**2) / (2 * d2 * d3), 10)
    return math.acos(cos_d1)
