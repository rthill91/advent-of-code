import aoc2019
import pytest


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


def test_day10_part1():
    assert aoc2019.day_10.part1() == 214


def test_day10_part2():
    assert aoc2019.day_10.part2() == 502


def test_day11_part1():
    assert aoc2019.day_11.part1() == 2276


def test_day12_part1():
    assert aoc2019.day_12.part1() == 7202


def test_day12_part2():
    assert aoc2019.day_12.part2() == 537881600740876


def test_day13_part1():
    assert aoc2019.day_13.part1() == 233


@pytest.mark.skip
def test_day14_part1():
    assert aoc2019.day_14.part1() == None


@pytest.mark.skip
def test_day14_part2():
    assert aoc2019.day_14.part2() == None


@pytest.mark.skip
def test_day15_part1():
    assert aoc2019.day_15.part1() == None


@pytest.mark.skip
def test_day15_part2():
    assert aoc2019.day_15.part2() == None


@pytest.mark.skip
def test_day16_part1():
    assert aoc2019.day_16.part1() == None


@pytest.mark.skip
def test_day16_part2():
    assert aoc2019.day_16.part2() == None


@pytest.mark.skip
def test_day17_part1():
    assert aoc2019.day_17.part1() == None


@pytest.mark.skip
def test_day17_part2():
    assert aoc2019.day_17.part2() == None


@pytest.mark.skip
def test_day18_part1():
    assert aoc2019.day_18.part1() == None


@pytest.mark.skip
def test_day18_part2():
    assert aoc2019.day_18.part2() == None


@pytest.mark.skip
def test_day19_part1():
    assert aoc2019.day_19.part1() == None


@pytest.mark.skip
def test_day19_part2():
    assert aoc2019.day_19.part2() == None


@pytest.mark.skip
def test_day20_part1():
    assert aoc2019.day_20.part1() == None


@pytest.mark.skip
def test_day20_part2():
    assert aoc2019.day_20.part2() == None


@pytest.mark.skip
def test_day21_part1():
    assert aoc2019.day_21.part1() == None


@pytest.mark.skip
def test_day21_part2():
    assert aoc2019.day_21.part2() == None


@pytest.mark.skip
def test_day22_part1():
    assert aoc2019.day_22.part1() == None


@pytest.mark.skip
def test_day22_part2():
    assert aoc2019.day_22.part2() == None


@pytest.mark.skip
def test_day23_part1():
    assert aoc2019.day_23.part1() == None


@pytest.mark.skip
def test_day23_part2():
    assert aoc2019.day_23.part2() == None


@pytest.mark.skip
def test_day24_part1():
    assert aoc2019.day_24.part1() == None


@pytest.mark.skip
def test_day24_part2():
    assert aoc2019.day_24.part2() == None


@pytest.mark.skip
def test_day25_part1():
    assert aoc2019.day_25.part1() == None


@pytest.mark.skip
def test_day25_part2():
    assert aoc2019.day_25.part2() == None
