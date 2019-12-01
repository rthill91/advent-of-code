def part1():
    fuel = 0
    with open('input') as fh:
        line = fh.readline()
        while (line != '') and (mass := int(line)):
            line = fh.readline()
            fuel += _get_fuel(mass)

    assert fuel == 3372463
    print(fuel)


def part2():
    fuel = 0
    with open('input') as fh:
        line = fh.readline()
        while (line != '') and (mass := int(line)):
            line = fh.readline()
            fuel += _get_fuel(mass, True)

    print(fuel)


def _get_fuel(mass, account_for_fuel_mass=False):
    fuel = (mass // 3) - 2

    if not account_for_fuel_mass:
        return fuel

    if fuel <= 0:
        return 0

    fuel += _get_fuel(fuel, True)

    return fuel
