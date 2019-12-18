from ._common import get_input
from dataclasses import dataclass
import itertools
import copy
import math


def part1():
    raw_input = get_input('input/day12')
    moons = sanitize_input(raw_input)
    for i in range(1000):
        moons = time_step(moons)

    energy = sum(m.total_energy for m in moons)
    print(energy)
    return energy


def part2():
    raw_input = get_input('input/day12')
    moons = sanitize_input(raw_input)

    x_steps = steps_to_original_position(copy.deepcopy(moons), 'x', 0)
    y_steps = steps_to_original_position(copy.deepcopy(moons), 'y', 1)
    z_steps = steps_to_original_position(copy.deepcopy(moons), 'z', 2)

    lowest = lcm(x_steps, y_steps, z_steps)
    print(lowest)


def time_step(moons, updates=None):
    for moon_pair in itertools.combinations(moons, r=2):
        if not updates:
            _update_velocity_x(*moon_pair)
            _update_velocity_y(*moon_pair)
            _update_velocity_z(*moon_pair)
        elif updates[0]:
            _update_velocity_x(*moon_pair)
        elif updates[1]:
            _update_velocity_y(*moon_pair)
        elif updates[2]:
            _update_velocity_z(*moon_pair)

    _apply_velocity(moons)
    return moons


def steps_to_original_position(moons, attr, index):
    updates = [False, False, False]
    updates[index] = True
    steps = 0
    original_moons = copy.deepcopy(moons)
    while True:
        steps += 1
        time_step(moons, updates)
        if check_moons(original_moons, moons, attr, index):
            break
    return steps


def check_moons(originals, moons, attr, index):
    for ind, moon in enumerate(moons):
        if moon != originals[ind]:
            return False
    return True


def _update_velocities(moon1, moon2):
    _update_velocity_x(moon1, moon2)
    _update_velocity_y(moon1, moon2)
    _update_velocity_z(moon1, moon2)


def _update_velocity_x(moon1, moon2):
    vel_change = 0
    if moon1.x > moon2.x:
        vel_change = -1
    elif moon1.x < moon2.x:
        vel_change = 1

    moon1.change_velocity(vel_change, 0, 0)
    moon2.change_velocity(-vel_change, 0, 0)


def _update_velocity_y(moon1, moon2):
    vel_change = 0
    if moon1.y > moon2.y:
        vel_change = -1
    elif moon1.y < moon2.y:
        vel_change = 1

    moon1.change_velocity(0, vel_change, 0)
    moon2.change_velocity(0, -vel_change, 0)


def _update_velocity_z(moon1, moon2):
    vel_change = 0
    if moon1.z > moon2.z:
        vel_change = -1
    elif moon1.z < moon2.z:
        vel_change = 1

    moon1.change_velocity(0, 0, vel_change)
    moon2.change_velocity(0, 0, -vel_change)


def _apply_velocity(moons):
    for moon in moons:
        moon.apply_velocity()


def sanitize_input(raw):
    moons = []
    for coord_string in raw:
        if coord_string:
            coords = coord_string[1:-1].split(', ')
            moons.append(Moon(int(coords[0][2:]), int(coords[1][2:]), int(coords[2][2:])))
    return moons


@dataclass
class Moon:
    x: int
    y: int
    z: int
    velocity: tuple = (0, 0, 0)

    @property
    def potential_energy(self):
        return abs(self.x) + abs(self.y) + abs(self.z)

    @property
    def kinetic_energy(self):
        return abs(self.velocity[0]) + abs(self.velocity[1]) + abs(self.velocity[2])

    @property
    def total_energy(self):
        return self.potential_energy * self.kinetic_energy

    def change_velocity(self, x, y, z):
        vel = self.velocity
        self.velocity = (vel[0] + x, vel[1] + y, vel[2] + z)

    def apply_velocity(self):
        self.x += self.velocity[0]
        self.y += self.velocity[1]
        self.z += self.velocity[2]

    def __hash__(self):
        pos = (self.x, self.y, self.z)
        return hash((pos, self.velocity))

def lcm(*args):
    res = args[0]
    for i in args[1:]:
        res = (res * i) // math.gcd(res, i)
    return res
