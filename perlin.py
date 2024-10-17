import numpy as np

def fade(t):
    return t * t * t * (t * (t * 6 - 15) + 10)

def lerp(a, b, t):
    return a + t * (b - a)

def grad(hash, x, y):
    h = hash & 3 
    u = x if h < 2 else -x
    v = y if h < 1 or h == 2 else -y
    return u + v

def perlin(x, y, perm):
    X = int(np.floor(x)) & 255
    Y = int(np.floor(y)) & 255

    x -= np.floor(x)
    y -= np.floor(y)

    u = fade(x)
    v = fade(y)

    a = perm[X] + Y
    aa = perm[a]
    ab = perm[a + 1]
    b = perm[X + 1] + Y
    ba = perm[b]
    bb = perm[b + 1]

    res = lerp(lerp(grad(perm[aa], x, y),
                     grad(perm[ba], x - 1, y),
                     u),
               lerp(grad(perm[ab], x, y - 1),
                    grad(perm[bb], x - 1, y - 1),
                    u),
               v)

    return (res + 1) / 2 

def generate_perlin_noise_2d(shape = (10,10), scale=1.0, cliping = 1):
    height, width = shape
    noise = np.zeros((height, width))

    perm = np.random.permutation(256)
    perm = np.stack([perm, perm]).flatten() 

    for y in range(height):
        for x in range(width):
            noise[y][x] = perlin(x / scale, y / scale, perm)

    noise = np.clip(np.round(noise * cliping), 0, cliping).astype(int)
    return noise
