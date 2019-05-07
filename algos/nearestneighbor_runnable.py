#!/usr/bin/env python3
"""Run and time a nearest neighbor TSP solution."""

import sys
import timeit
import math

import tspinput
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


data = tspinput.get(sys.argv[1])

def closestpoint(point, route):
    dmin = float("inf")
    for p in route:
        d = math.sqrt((int(point[0]) - int(p[0]))**2 + (int(point[1]) - int(p[1]))**2)
        if d < dmin:
            dmin = d
            closest = p
    return closest, dmin

point, *route = data
path = [point]
sum = 0
while len(route) >= 1:
    closest, dist = closestpoint(path[-1], route)
    path.append(closest)
    route.remove(closest)
    sum += dist
# Go back the the beginning when done.
closest, dist = closestpoint(path[-1], [point])
path.append(closest)
sum += dist

print("Optimal route:", path)
print("Length:", sum)

A = np.array(path)
PTS= np.array(data)

plt.plot(*A.T)
plt.scatter(*PTS.T,  s= 2, c ='m')
# plt.plot(data[0], data[1])
plt.show()

















