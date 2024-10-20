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
        self.uid = f"{x};{y};{z}"
        self.state = "None"
        self.properties = {"ID"          : block_id, 
                           "state"       : self.state,
                           "mesh"        : None,
                           "coordinates" : (x, y, z),
                           "neighbors"   : []}

    def __repr__(self):
        return f"block(id={self.block_id}, coordinates={self.coordinates}, state={self.state}, uid={self.uid})"
     
class BlockGrid:
    def __init__(self):
        self.blocks = {}

    def add_block(self, x, y, z, block_id):
        # if block_id in self.blocks:
        #     raise ValueError("block with this ID already exists.")
        new_block = Block(x, y, z, block_id)
        self.blocks[new_block.uid]=new_block.properties

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
    
    def check_neighbors(self):
        for key in self.blocks:
            uid = key.split(";")
            if f"{int(uid[0])+1};{uid[1]};{uid[2]}" in self.blocks: #LEFT
                self.blocks[key]["neighbors"].append("LEFT")
            if f"{int(uid[0])-1};{uid[1]};{uid[2]}" in self.blocks: #RIGHT
                self.blocks[key]["neighbors"].append("RIGHT")
            if f"{uid[0]};{int(uid[1])+1};{uid[2]}" in self.blocks: #TOP
                self.blocks[key]["neighbors"].append("TOP")
            if f"{uid[0]};{int(uid[1])-1};{uid[2]}" in self.blocks: #BOTTOM
                self.blocks[key]["neighbors"].append("BOTTOM")
            if f"{uid[0]};{uid[1]};{int(uid[2])+1}" in self.blocks: #BACK
                self.blocks[key]["neighbors"].append("BACK")
            if f"{uid[0]};{uid[1]};{int(uid[2])-1}" in self.blocks: #FRONT
                self.blocks[key]["neighbors"].append("FRONT")

    def __repr__(self):
        return f"blockGrid={self.blocks})"
    

