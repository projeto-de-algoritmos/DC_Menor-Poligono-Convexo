from functools import reduce
import operator
import math

hull = set()

def clockwiseSort():
    center = tuple(map(operator.truediv, reduce(lambda x, y: map(operator.add, x, y), hull), [len(hull)] * 2))
    a = (sorted(hull, key=lambda coord: (-135 - math.degrees(math.atan2(*tuple(map(operator.sub, coord, center))[::-1]))) % 360))
    return a


def findSide(p1, p2, p):
    val = (p[1] - p1[1]) * (p2[0] - p1[0]) - (p2[1] - p1[1]) * (p[0] - p1[0])

    if val > 0:
        return 1
    if val < 0:
        return -1
    return 0

def lineDist(p1, p2, p):
    return abs((p[1] - p1[1]) * (p2[0] - p1[0]) - (p2[1] - p1[1]) * (p[0] - p1[0]))


def quickHull(points, n, p1, p2, side):
    ind = -1
    max_dist = 0

    for i, p in enumerate(points):
        temp = lineDist(p1, p2, p)
        if findSide(p1, p2, p) == side and temp > max_dist:
            ind = i
            max_dist = temp

    if ind == -1:
        hull.add(p1)
        hull.add(p2)
        return;

    quickHull(points, n, points[ind], p1, -findSide(points[ind], p1, p2))
    quickHull(points, n, points[ind], p2, -findSide(points[ind], p2, p1))

def printHull(points, n):

    min_x = 0
    max_x = 0
    for i, p in enumerate(points):
        if p[0] < points[min_x][0]:
            min_x = i

        if p[0] > points[max_x][0]:
            max_x = i


    quickHull(points, n, points[min_x], points[max_x], 1)

    quickHull(points, n, points[min_x], points[max_x], -1)


def makeHull(points):
    import sys
    # points = [(0,300), (100,100), (200,200), (400, 400), (0, 0), (100, 200), (300, 100), (300, 300)]
    # points = [(123, 139), (124, 275), (331, 278), (270, 204), (332, 121), (303, 218)]
    print('entrada ', points)
    if len(points) >= 3:
        printHull(points, len(points))
        pointsSorted = clockwiseSort()
        print('exit ', pointsSorted)
        return pointsSorted
    else:
        return []
