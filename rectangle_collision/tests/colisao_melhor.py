def colisao(x1, y1, x2, y2, x3, y3, x4, y4):
    if (x1 > x4 or x3 > x2) or (y1 > y4 or y3 > y2):
        return 0
    return 1
