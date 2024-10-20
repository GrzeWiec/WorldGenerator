import json
import TextureMap
from ursina import *

class Block(Entity):
    def __init__(self, x, y, z, block_id):
        super().__init__(
        origin_y=-0.5,
        position = (x, y, z),
        scale = 1,
        collider="box",
        model = "cube",
        parent = scene,
        texture = load_texture("Textures\dirt.png")
        )
        self.coordinates = (x, y, z)
        self.block_id = block_id
        self.uid = f"{x}x{y}y{z}z"
        self.state = "None"

    def __repr__(self):
        return f"block(id={self.block_id}, coordinates={self.coordinates}, state={self.state}, uid={self.uid})"
    
    
class BlockGrid:
    def __init__(self):
        self.blocks = []

    def add_block(self, x, y, z, block_id):
        # if block_id in self.blocks:
        #     raise ValueError("block with this ID already exists.")
        self.blocks.append(Block(x, y, z, block_id))

    def remove_block(self, block_id):
        if block_id in self.blocks:
            del self.blocks[block_id]
        else:
            raise KeyError("block with this ID does not exist.")
    
    def save_to_file(self, filename):
        with open(filename, 'w') as f:
            json.dump([block.to_dict() for block in self.blocks.values()], f)

    @classmethod
    def load_from_file(cls, filename):
        grid = cls()
        with open(filename, 'r') as f:
            blocks_data = json.load(f)
            for block_data in blocks_data:
                block = block.from_dict(block_data)
                grid.blocks[block.block_id] = block
        return grid

    def __repr__(self):
        return f"blockGrid(blocks={list(self.blocks)})"