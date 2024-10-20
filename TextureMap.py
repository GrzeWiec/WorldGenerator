import json

def IDtoTexture(id):
    return(ID_TO_TEXTURE.get(id, None))
    

ID_TO_TEXTURE = {
    1: "stone.png",
    2: "dirt.png",
    3: "grass.png",
    4: "sand.png",
}