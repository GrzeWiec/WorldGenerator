from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import numpy as np
from perlin import generate_perlin_noise_2d
from BlocksGenerator import Block, BlockGrid
from TextureMap import IDtoTexture
import sys

app = Ursina()
player = FirstPersonController(y=10)
Sky()

position_text = Text(text='', position=(-0.9, 0.4), scale=2, origin=(-1, 0))
boxes = []

def update():
    position_text.text = f'Pozycja gracza: ({int(player.position.x)}, {int(player.position.y)}, {int(player.position.z)})'

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

def add_block_to_grid(block_grid, x, y, z, block_id):
    block_grid.add_block(x, y, z, block_id)

def remove_block(position):
    for box in boxes:
        if box.position == position:
            destroy(box)
            boxes.remove(box)
            break

block_grid = BlockGrid()
for x in range (0,50):
    for z in range (0, 50):
        add_block_to_grid(block_grid, x, 1, z, 1)

app.run()
