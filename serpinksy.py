import MaxPlus
import random
import math


def LerpColour(a, b, t):
    return a[0]*(1 - t) + b[0]*t, a[1]*(1 - t) + b[1]*t, a[2]*(1 - t) + b[2]*t


def height(x, y, d):
    b = abs(d/2 - x)
    print b
    return 1.25 + math.sin((x+y)/float(d/4)) + 0.15 * random.uniform(-1.0, 1.0)


def draw_boxes():
    # initial variables
    dimension = 30
    maxHeight = 50
    space = 10.0
    # red, white
    colx1, colx2 = [random.randrange(0, 255) for c in range(3)], [random.randrange(0, 255) for c in range(3)]
    #yellow, cyan
    coly1, coly2 = [random.randrange(0, 255) for c in range(3)], [random.randrange(0, 255) for c in range(3)]

    MaxPlus.FileManager.Reset(True)

    for x in range(dimension):
        for y in range(dimension):
            obj = MaxPlus.Factory.CreateGeomObject(MaxPlus.ClassIds.Box)
            obj.ParameterBlock.Height.Value = maxHeight * height(x, y, dimension)

            colorx = LerpColour(colx1, colx2, float(x)/(dimension-1))
            colory = LerpColour(coly1, coly2, float(x)/(dimension-1))

            colorxy = LerpColour(colorx, colory, float(y)/(dimension-1))
            intcolor = [c/255 for c in colorxy]

            name = "x={}, y={}".format(x, y)
            if x % 5 == 0 and y % 5 == 0:
                print name
            node = MaxPlus.Factory.CreateNode(obj, name)
            node.Position = (MaxPlus.Point3(25.0*float(x), 25.0*float(y)+space, 0))
            node.WireColor = MaxPlus.Color(intcolor[0], intcolor[1], intcolor[2])


if __name__ == "__main__":
    draw_boxes()