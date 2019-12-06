def part1():
    orbit_input = _get_input()
    orbits = _get_orbits(orbit_input)
    checksum = 0
    for satellite in orbits:
        checksum += _calculate_hash(satellite, orbits)

    print(checksum)


def part2():
    pass


def _get_orbits(orbit_input):
    orbits = dict()
    for entry in orbit_input:
        center, satellite = _get_orbit(entry)
        orbits[satellite] = center
    return orbits


def _get_orbit(entry):
    center, satellite = entry.split(')')
    return center, satellite


def _calculate_hash(satellite, orbits):
    if not satellite:
        return -1
    return 1 + _calculate_hash(orbits.get(satellite), orbits)


def _get_input():
    with open('input') as fh:
        return [line.strip() for line in fh.readlines()]
    # return ['B)C', 'C)D', 'D)E', 'E)F', 'B)G', 'G)H', 'D)I', 'E)J', 'J)K', 'K)L', 'COM)B']
    # return ['COM)B', 'B)C', 'C)D', 'D)E', 'E)F', 'B)G', 'G)H', 'D)I', 'E)J', 'J)K', 'K)L']
