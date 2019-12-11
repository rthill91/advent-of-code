def part1():
    image = _get_input()
    layer_index = _get_layer_index_with_fewest_zeros(image)
    layer = image[layer_index]
    ones = sum(line.count('1') for line in layer)
    twos = sum(line.count('2') for line in layer)
    answer = ones * twos

    assert answer == 1965
    print(answer)


def part2():
    image = []
    image_layers = _get_input()
    for i in range(len(image_layers[0])): # rows
        line = []
        for j in range(len(image_layers[0][0])): #columns
            pixels = [layer[i][j] for layer in image_layers]
            value = next(pixel for pixel in pixels if pixel != '2')
            line.append(value)
        image.append(tuple(line))

    for line in image:
        l = ''.join(line)
        l = l.replace('1', '\u2587')
        l = l.replace('0', ' ')
        print(l)


def _get_layer_index_with_fewest_zeros(image):
    fewest_zeros = (9999, -1)
    for index, layer in enumerate(image):
        zeros = sum(line.count('0') for line in layer)
        if zeros < fewest_zeros[0]:
            fewest_zeros = (zeros, index)
    return fewest_zeros[1]


def _get_input():
    with open('input') as fh:
        image = []
        layer = []
        line = []
        for char in fh.read():
            line.append(char)
            if len(line) == 25:
                layer.append(tuple(line))
                line = []
            if len(layer) == 6:
                image.append(tuple(layer))
                layer = []

        return image
