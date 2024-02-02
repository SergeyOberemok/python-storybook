def getPlotBoundaries(top: int, right: int, bottom: int = None, left: int = None, margin: int = 0) -> list:
    if bottom is None:
        bottom = -top

    if left is None:
        left = -right

    return [
        getPlotBound(left, margin),
        getPlotBound(right, margin),
        getPlotBound(bottom, margin),
        getPlotBound(top, margin)
    ]


def getPlotBound(bound: int, margin: int) -> int:
    sign = int(abs(bound) / bound)

    return sign * (abs(bound) + margin)
