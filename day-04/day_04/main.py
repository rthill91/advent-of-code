def part1(lower='153517', upper='630395'):
    i = 0
    for num in _generator(lower, upper):
        if len(set(num)) < 6 and int(num) <= int(upper) and int(num) >= int(lower):
            i += 1

    assert i == 1729
    print(i)


def part2(lower='153517', upper='630395'):
    i = 0
    for num in _generator(lower, upper):
        num_set = set(num)
        exactly_two_digits = False
        for item in num_set:
            if num.count(item) == 2:
                exactly_two_digits = True


        if len(num_set) < 6 and int(num) <= int(upper) and int(num) >= int(lower) and exactly_two_digits:
            i += 1

    assert i == 1172
    print(i)


def _generator(lower, upper):
    for i0 in range(int(lower[0]), int(upper[0])+1):
        for i1 in range(i0, 10):
            for i2 in range(i1, 10):
                for i3 in range(i2, 10):
                    for i4 in range(i3, 10):
                        for i5 in range(i4, 10):
                            yield f'{i0}{i1}{i2}{i3}{i4}{i5}'
