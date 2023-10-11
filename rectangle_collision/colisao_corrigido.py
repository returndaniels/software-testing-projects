def colisao(x1, y1, x2, y2, x3, y3, x4, y4):
    minxr1 = min(x1, x2)
    maxxr1 = max(x1, x2)
    minxr2 = min(x3, x4)
    maxxr2 = max(x3, x4)
    minyr1 = min(y1, y2)
    maxyr1 = max(y1, y2)
    minyr2 = min(y3, y4)
    maxyr2 = max(y3, y4)

    if (minxr2 >= minxr1 and minxr2 <= maxxr1) or (
        maxxr2 >= minxr1 and maxxr2 <= maxxr1
    ):
        if (minyr2 >= minyr1 and minyr2 <= maxyr1) or (
            maxyr2 >= minyr1 and maxyr2 <= maxyr1
        ):
            return 1
        if (minyr1 >= minyr2 and minyr1 <= maxyr2) or (
            maxyr1 >= minyr2 and maxyr1 <= maxyr2
        ):
            return 1

    if (minxr1 >= minxr2 and minxr1 <= maxxr2) or (
        maxxr1 >= minxr2 and maxxr1 <= maxxr2
    ):
        if (minyr2 >= minyr1 and minyr2 <= maxyr1) or (
            maxyr2 >= minyr1 and maxyr2 <= maxyr1
        ):
            return 1
        if (minyr1 >= minyr2 and minyr1 <= maxyr2) or (
            maxyr1 >= minyr2 and maxyr1 <= maxyr2
        ):
            return 1

    return 0
