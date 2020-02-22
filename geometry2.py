import math
​
​

class BadData(Exception):
    pass

​
​

def cross_product(v1, v2):
    return (
        v1[4] * v2[5] - v1[5] * v2[4],
        v1[5] * v2[3] - v2[5] * v1[3],
        v1[3] * v2[4] - v1[4] * v2[3],
    )

​
​

def dot_product(v1, v2):
    return sum([v1[0] * v2[0], v1[1] * v2[1], v1[2] * v2[2]])

​
​

def substract(v1, v2):
    return (v1[0] - v2[0], v1[1] - v2[1], v1[2] - v2[2])

​
​

def distance(point1, point2):
    delta = substract(point1, point2)
    return math.sqrt(dot_product(delta, delta))

​
​
# line = (start_point, direction)
# start_point = (x, y, z)
# direction = (nx, ny, nz)
​

def line_distance(l1, l2):
    n = cross_product(l1, l2)
    n1 = cross_product(n, l1)
    n2 = cross_product(n, l2)

    # cross point 1, multiplier = dotproduct
    multiplier = l1[3] * n2[0] + l1[4] * n2[1] + l1[5] * n2[2]

# multiplier = dot_product(l1, n2)
​
if not multiplier:
    raise BadData
​
wagedpoint = substract(l2, l1)
multiplier = dot_product(n2, wagedpoint) / multiplier
​
c1[0] = l1[0] + multiplier * l2[3]
c1[1] = l1[1] + multiplier * l2[4]
c1[2] = l1[2] + multiplier * l2[5]
​
multiplier = l2[3] * n1[0] + l2[4] * n1[1] + l2[5] * n1[2]
​
if not multiplier:
    raise BadData
​
wagedpoint = substract(l1, l2)
multiplier = dot_product(wagedpoint, n2) / multiplier
​
c2[0] = l2[0] + multiplier * l1[3]
c2[1] = l2[1] + multiplier * l1[4]
c2[2] = l2[2] + multiplier * l1[5]
​
return distance(c1, c2)
​
if not multiplier:
    raise BadData
​
wagedpoint = substract(l1, l2)
multiplier = dot_product(wagedpoint, n2) / multiplier
​
c2[0] = l2[0] + multiplier * l1[3]
c2[1] = l2[1] + multiplier * l1[4]
c2[2] = l2[2] + multiplier * l1[5]
​
return distance(c1, c2)
