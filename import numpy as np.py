import numpy as np
import random
import math

def fade(t):
    return t * t * t * (t * (t * 6 - 15) + 10)

def lerp(a, b, t):
    return a + t * (b - a)

def grad(hash, x, y):
    h = hash & 3
    u = x if h == 0 or h == 2 else -x
    v = y if h == 0 or h == 1 else -y
    return u + v

def perlin(x, y, perm):
    X = int(np.floor(x)) & 255
    Y = int(np.floor(y)) & 255
    x -= np.floor(x)
    y -= np.floor(y)
    u = fade(x)
    v = fade(y)
    
    aa = perm[perm[X] + Y]
    ab = perm[perm[X] + Y + 1]
    ba = perm[perm[X + 1] + Y]
    bb = perm[perm[X + 1] + Y + 1]
    
    res = lerp(lerp(grad(aa, x, y), grad(ba, x - 1, y), u),
               lerp(grad(ab, x, y - 1), grad(bb, x - 1, y - 1), u), v)

    return (res + 1) / 2

def generate_perlin_noise_2d(shape, scale, value_range, octaves=1, persistence=0.5):
    noise_array = np.zeros(shape)
    perm = list(range(256))
    random.shuffle(perm)
    perm += perm
    
    for y in range(shape[0]):
        for x in range(shape[1]):
            amplitude = 1
            frequency = 1
            total = 0
            max_value = 0
            
            for _ in range(octaves):
                noise_value = perlin(x * frequency / scale, y * frequency / scale, perm)
                total += noise_value * amplitude
                
                max_value += amplitude
                amplitude *= persistence
                frequency *= 2
            
            # Normalizacja
            mapped_value = math.floor(value_range[0] + (total / max_value) * (value_range[1] - value_range[0]))
            noise_array[y, x] = mapped_value

    return noise_array

# Ustawienia dla różnych poziomów zmienności
shape = (20, 20)  # Rozmiar macierzy
value_range = (1, 10)  # Zakres wartości

# 1. Mała zmienność
scale_small = 20.0
octaves_small = 1
persistence_small = 0.5
perlin_noise_small = generate_perlin_noise_2d(shape, scale_small, value_range, octaves_small, persistence_small)

# 2. Średnia zmienność
scale_medium = 10.0
octaves_medium = 3
persistence_medium = 0.5
perlin_noise_medium = generate_perlin_noise_2d(shape, scale_medium, value_range, octaves_medium, persistence_medium)

# 3. Duża zmienność
scale_large = 5.0
octaves_large = 4
persistence_large = 0.6
perlin_noise_large = generate_perlin_noise_2d(shape, scale_large, value_range, octaves_large, persistence_large)

# Wyświetlenie wyników
print("Mała zmienność:\n", perlin_noise_small)
print("Średnia zmienność:\n", perlin_noise_medium)
print("Duża zmienność:\n", perlin_noise_large)
