from pico2d import *

objects = []

def World_Init(layerIndex):
    for i in range(layerIndex):
        objects.append([])

def Add_Object(obj, depth):
    if len(objects) < depth:
        for i in range(depth - len(objects)):
            objects.append([])

    objects[depth].append(obj)
    pass

def Add_Objcets(objs, depth):
    if len(objects) < depth:
        for i in range(depth - len(objects)):
            objects.append([])

    objects[depth] += objs
    pass

def Remove_Object(obj):
    for layer in objects:
        if obj in layer:
            layer.remove(obj)
            del obj
            return
    raise ValueError('not find remove object')
    pass

def All_Objcet():
    for layer in objects:
        for obj in layer:
            yield obj
    pass

def clear():
    for obj in All_Objcet():
        del obj
    for layer in objects:
        layer.remove()

