#!/usr/bin/env python3
"""Run and time a nearest neighbor TSP solution."""

import sys
import timeit
import math

import ingest_poczty as ing

import numpy as np
import networkx as nx
import matplotlib.pyplot as plt



def closestpoint(point, route):
    dmin = float("inf")
    for p in route:
        d = math.sqrt((int(point[1]) - int(p[1]))**2 + (int(point[2]) - int(p[2]))**2)
        if d < dmin:
            dmin = d
            closest = p
    return closest, dmin

def nearestneighbor(data):
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
    return path, sum



    

if __name__ == "__main__":
    data = ing.get_simple("poczty.txt")

    path, sum =  nearestneighbor(data)
    
    print("Optimal route:", path)
    print("Length:", sum)
    
    A = np.array([ [p[1],p[2]] for p in path])
    points_only = [ [p[1],p[2]] for p in data]
    PTS= np.array(points_only)
    
    plt.plot(*A.T)
    plt.scatter(*PTS.T,  s= 2, c ='m')

    plt.show()   
    

















