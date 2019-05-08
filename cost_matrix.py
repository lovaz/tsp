import sys
import timeit
import math
import itertools

import tspinput as tspinput
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
from scipy.spatial import distance_matrix

coords = tspinput.get("tsp9.txt")

ctys = ['A', 
        'B',
        'C', 
        'D', 
        'E', 
        'F', 
        'G', 
        'H', 
        'I'
        
        ]


df = pd.DataFrame(coords, columns=['xcord', 'ycord'], index=ctys)
df1 = pd.DataFrame(distance_matrix(df.values, df.values), index=df.index, columns=df.index)
print(df1)