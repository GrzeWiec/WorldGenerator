from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import numpy as np
from perlin import generate_perlin_noise_2d
import sys

app = Ursina()
player = FirstPersonController(y=10)
Sky()

position_text = Text(text='', position=(-0.9, 0.4), scale=2, origin=(-1, 0))

boxes = []

def update():
    position_text.text = f'Pozycja gracza: ({int(player.position.x)}, {int(player.position.y)}, {int(player.position.z)})'

def gen_terrain(poz, texture):
    for i in poz:
        remove_block(i)
        box = Button(color=color.white, model='cube', position=i,
                     texture=texture, parent=scene, origin_y=0.5)
        boxes.append(box)

def remove_block(position):
    for box in boxes:
        if box.position == position:
            destroy(box)
            boxes.remove(box)
            break

def input(key):
    if key == 'x':
        sys.exit()
    
    for box in boxes:
        if box.hovered:
            if key == 'left mouse down':
                new_box = Button(color=color.white, model='cube', position=box.position + mouse.normal,
                                 texture='grass.png', parent=scene, origin_y=0.5)
                boxes.append(new_box)
            elif key == 'right mouse down':
                destroy(box)
                boxes.remove(box)
            break 

def matrix_to_poz(matrix):
    tmp_list = []
    for cor_x in range(len(matrix)):
        for cor_y in range(len(matrix[0])):
            for cor_z in range(matrix[cor_x][cor_y]):
                tmp_list.append((cor_x, cor_z, cor_y))
        
    return tmp_list

x = 30
shape = (x, x)
terrain = []
dirt = generate_perlin_noise_2d(shape, scale=8, cliping=7)
print(f"dirt matrix\n{dirt}\n")
grass = generate_perlin_noise_2d(shape, scale=12, cliping=2)
print(f"grass matrix\n{grass}\n")
stone = generate_perlin_noise_2d(shape, scale=2, cliping=1)
print(f"stone matrix\n{stone}\n")
grass = dirt + grass

gen_terrain(matrix_to_poz(grass), "grass.png")
terrain.extend(grass)

gen_terrain(matrix_to_poz(dirt), "dirt.png")
terrain.extend(dirt)

stone+=2
# print(stone)
# gen_terrain(matrix_to_poz(stone), "stone.png")

terrain.extend(dirt)

app.run()
