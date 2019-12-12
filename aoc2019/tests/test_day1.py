from aoc2019 import day_01


def test_get_fuel():
    assert day_01._get_fuel(12, False) == 2
    assert day_01._get_fuel(14, False) == 2
    assert day_01._get_fuel(1969, False) == 654
    assert day_01._get_fuel(100756, False) == 33583


def test_part1():
    assert day_01.part1() == 3372463


def test_part2():
    assert day_01.part2() == 5055835
