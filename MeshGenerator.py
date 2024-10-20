from ursina import *

vertices = [
    Vec3(-1, -1, -1),  # 0
    Vec3(1, -1, -1),   # 1
    Vec3(1, 1, -1),    # 2
    Vec3(-1, 1, -1),   # 3
    Vec3(-1, -1, 1),   # 4
    Vec3(1, -1, 1),    # 5
    Vec3(1, 1, 1),     # 6
    Vec3(-1, 1, 1),    # 7
]

uvs = (1, 1), (0, 1), (0, 0), (1, 0), (1, 1), (0, 0)

def mesh_create(block):
    tmp_mesh = []
    
    if "FRONT" not in block.properties["neighbors"]:
        tmp_mesh.extend([(0, 1, 2), (0, 2, 3)])  # BACK
    if "BACK" not in block.properties["neighbors"]:
        tmp_mesh.extend([(6, 5, 4), (7, 6, 4)])  # FRONT
    if "RIGHT" not in block.properties["neighbors"]:
        tmp_mesh.extend([(7, 4, 0), (3, 7, 0)])  # LEFT
    if "LEFT" not in block.properties["neighbors"]:
        tmp_mesh.extend([(1, 5, 6), (1, 6, 2)])  # RIGHT
    if "TOP" not in block.properties["neighbors"]:
        tmp_mesh.extend([(3, 2, 6), (3, 6, 7)])  # TOP
    if "BOTTOM" not in block.properties["neighbors"]:
        tmp_mesh.extend([(5, 1, 0), (4, 5, 0)])  # BOTTOM

    if tmp_mesh:
        block.model = Mesh(vertices=vertices, triangles=tmp_mesh)
    else:
        block.enabled = False
