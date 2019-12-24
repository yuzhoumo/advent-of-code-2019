import sys


class Image:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.raw_data, self.layers = [], []

    def add_layer(self, layer):
        assert layer.x == self.x and layer.y == self.y, 'Layer size does not match image size'
        self.layers.append(layer)

    def set_data(self, data):
        assert len(data) % (self.x * self.y) == 0, 'Data length does not match img size'
        self.raw_data = [int(n) for n in data]
        data = list(self.raw_data)

        while data:
            layer = Layer(self.x, self.y)
            layer.set_data(data[:self.x * self.y])
            data = data[self.x * self.y:]
            self.add_layer(layer)


class Layer:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.raw_data, self.rows = [], []

    def add_row(self, row):
        assert len(row) == self.x, 'Row length does not match x dimension'
        self.rows.append(row)

    def set_data(self, data):
        assert len(data) == self.x * self.y, 'Data length does not match layer size'
        self.raw_data = [int(n) for n in data]
        data = list(self.raw_data)

        for _ in range(self.y):
            row, data = data[:self.x], data[self.x:]
            self.add_row(row)

    def count_digit(self, d):
        cnt = 0
        for n in self.raw_data:
            if n == d:
                cnt += 1
        return cnt


def corruption_check(img):
    fewest_zeros_layer = min(img.layers, key=lambda x: Layer.count_digit(x, 0))
    return fewest_zeros_layer.count_digit(1) * fewest_zeros_layer.count_digit(2)


assert len(sys.argv) > 1, 'Missing argument: path to input file'
assert len(sys.argv) > 2, 'Missing argument: x dimension of image'
assert len(sys.argv) > 3, 'Missing argument: y dimension of image'
assert len(sys.argv) < 5, 'Too many arguments'

with open(sys.argv[1], 'r') as f:
    x_dim, y_dim = int(sys.argv[2]), int(sys.argv[3])
    image = Image(x_dim, y_dim)
    image.set_data(f.read().strip())

print(corruption_check(image))