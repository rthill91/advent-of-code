_HASHES = {}

def part1():
    orbit_input = _get_input()
    orbits = _get_orbits(orbit_input)
    checksum = 0
    for satellite in orbits:
        checksum += _calculate_hash(satellite, orbits)

    print(checksum)


def part2():
    orbit_input = _get_input()
    orbits = _get_orbits(orbit_input)
    you_path = _get_path('YOU', orbits)
    san_path = _get_path('SAN', orbits)

    while you_path.pop() == san_path.pop():
        pass

    print(len(you_path) + len(san_path) + 2)


def _get_orbits(orbit_input):
    orbits = dict()
    for entry in orbit_input:
        center, satellite = _get_orbit(entry)
        orbits[satellite] = center
    return orbits


def _get_orbit(entry):
    center, satellite = entry.split(')')
    return center, satellite


def _calculate_hash(satellite, orbits, end=None):
    if not satellite:
        return -1
    if satellite == end:
        return 0
    return 1 + _calculate_hash(orbits.get(satellite), orbits)


def _get_path(satellite, orbits):
    path = []
    while satellite := orbits.get(satellite):
        path.append(satellite)
    return path


def _get_input():
    with open('input') as fh:
        return [line.strip() for line in fh.readlines()]
