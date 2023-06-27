from ..base.vector import Vector

def normalize(v):
    return Vector(v.x/v.mag, v.y/v.mag)