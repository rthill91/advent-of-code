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
    asteroids = _get_asteroids('input/day10')

    for station in asteroids:
        count = _calculate_visible_asteroids(station, asteroids)
        station.detectable_count = count

    best = max((a for a in asteroids), key=lambda a: a.detectable_count)
    print(best)
    return best



def part2(station_x=8, station_y=16):
    """
    find all asteroids on a given angle and sort them by distance
    starting at -90 and rotating clockwise what is the 200th asteroid hit
    """
    asteroids = _get_asteroids('input/day10')
    station = next(ast for ast in asteroids if ast.x == station_x and ast.y == station_y)

    angles = _get_visible_angles(station, asteroids)
    for angle in angles:
        angles[angle].sort(key=lambda ast: _get_distance(station, ast))

    angles = _convert_to_list(angles)
    count = 0
    while count < 200:
        angle = angles.pop(0)
        ast = angle[1].pop(0)
        count += 1
        if angle[1]:
            angles.append(angle)

    print(ast)
    result = 100 * ast.x + ast.y
    print(result)
    return result



def _get_asteroids(input_file):
    asteroid_map = get_input(input_file)
    asteroids = []
    for y, line in enumerate(asteroid_map):
        for x, element in enumerate(line):
            if element == '#':
                asteroids.append(Asteroid(x, y))
    return asteroids


def _calculate_visible_asteroids(station, asteroids):
    angles = _get_visible_angles(station, asteroids)
    return len(set(angles))


def _get_visible_angles(station, asteroids):
    angles = {}
    for asteroid in asteroids:
        if station is asteroid:
            continue
        angle = _calculate_angle(station, asteroid)
        if angles.get(angle):
            angles[angle].append(asteroid)
        else:
            angles[angle] = [asteroid]
    return angles


def _calculate_angle(p1, p2):
    return math.atan2(p2.y - p1.y, p2.x - p1.x) * 180 / math.pi


def _get_distance(p1, p2):
    return Decimal(math.sqrt((p2.x - p1.x)**2 + (p2.y - p1.y)**2))


def _convert_to_list(angles):
    ret_val = []
    angle_list = sorted(angles)
    angle = angle_list[0]
    while angle < -90.0:
        angle_list.append(angle_list.pop(0))
        angle = angle_list[0]

    for angle in angle_list:
        ret_val.append((angle, angles[angle]))

    return ret_val


def _get_angle(d1, d2, d3):
    cos_d1 = round((d2**2 + d3**2 - d1**2) / (2 * d2 * d3), 10)
    return math.acos(cos_d1)
