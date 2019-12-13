import aoc2019


def test_day01_get_fuel():
    assert aoc2019.day_01._get_fuel(12, False) == 2
    assert aoc2019.day_01._get_fuel(14, False) == 2
    assert aoc2019.day_01._get_fuel(1969, False) == 654
    assert aoc2019.day_01._get_fuel(100756, False) == 33583

def test_day01_part1():
    assert aoc2019.day_01.part1() == 3372463


def test_day01_part2():
    assert aoc2019.day_01.part2() == 5055835


def test_day02_part1():
    assert aoc2019.day_02.part1() == 11590668


def test_day02_part2():
    assert aoc2019.day_02.part2() == 2254


def test_day03_part1():
    assert aoc2019.day_03.part1() == 2180


def test_day03_part2():
    assert aoc2019.day_03.part2() == 112316


def test_day04_part1():
    assert aoc2019.day_04.part1() == 1729


def test_day04_part2():
    assert aoc2019.day_04.part2() == 1172


def test_day05_part1():
    assert aoc2019.day_05.part1() == 5821753


def test_day05_part2():
    assert aoc2019.day_05.part2() == 11956381


def test_day06_part1():
    assert aoc2019.day_06.part1() == 292387


def test_day06_part2():
    assert aoc2019.day_06.part2() == 433


def test_day07_part1():
    assert aoc2019.day_07.part1() == 92663


def test_day07_part2():
    assert aoc2019.day_07.part2() == 14365052


def test_day08_part1():
    assert aoc2019.day_08.part1() == 1965


def test_day09_part1():
    assert aoc2019.day_09.part1() == 2789104029


def test_day09_part2():
    assert aoc2019.day_09.part2() == 32869
