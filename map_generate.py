import numpy as np


def generate_perlin_noise(width, height, scale, octaves, persistence, lacunarity, seed):
    perlin_noise_array = np.zeros((height, width))
    for y in range(height):
        for x in range(width):
            perlin_noise_array[y][x] = generate_perlin_value(
                x, y, scale, octaves, persistence, lacunarity, seed)
    return perlin_noise_array


def generate_perlin_value(x, y, scale, octaves, persistence, lacunarity, seed):
    value = 0
    for i in range(octaves):
        freq = scale * (2 ** i)
        amp = persistence ** i
        value += interp_noise(x * freq, y * freq, seed) * amp
    return int(value)


def interp_noise(x, y, seed):
    x_int = int(x)
    y_int = int(y)
    fractional_x = x - x_int
    fractional_y = y - y_int

    top_left = random_noise(x_int, y_int, seed)
    top_right = random_noise(x_int + 1, y_int, seed)
    bottom_left = random_noise(x_int, y_int + 1, seed)
    bottom_right = random_noise(x_int + 1, y_int + 1, seed)

    top = interpolate(top_left, top_right, fractional_x)
    bottom = interpolate(bottom_left, bottom_right, fractional_x)

    return interpolate(top, bottom, fractional_y)


def random_noise(x, y, seed):
    np.random.seed(seed)
    return np.random.random()


def interpolate(a, b, x):
    ft = x * np.pi
    f = (1 - np.cos(ft)) * 0.5
    return a * (1 - f) + b * f


# Tham số cho việc tạo Perlin noise
width = 10
height = 10
scale = 1
octaves = 3
persistence = 4
lacunarity = 2.0
seed = np.random.randint(0, 100)

# Tạo mảng Perlin noise
perlin_noise_array = generate_perlin_noise(
    width, height, scale, octaves, persistence, lacunarity, seed)

# Lưu mảng Perlin noise thành một file ma trận
np.savetxt('perlin_noise_matrix.map', perlin_noise_array, fmt='%d')
