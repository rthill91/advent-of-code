from ._common import get_input


def part1():
    fuel = 0
    masses = list(filter(None, get_input('input/day1')))
    for mass in masses:
        fuel += _get_fuel(int(mass))

    print(fuel)
    return fuel


def part2():
    fuel = 0
    masses = list(filter(None, get_input('input/day1')))
    for mass in masses:
        fuel += _get_fuel(int(mass), True)

    print(fuel)
    return fuel


def _get_fuel(mass, account_for_fuel_mass=False):
    fuel = (mass // 3) - 2

    if not account_for_fuel_mass:
        return fuel

    if fuel <= 0:
        return 0

    return fuel + _get_fuel(fuel, True)
