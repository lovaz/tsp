from ast import literal_eval as make_tuple
import pandas as pd
from scipy.spatial import distance_matrix
from dis import dis


def get(filename):
    with open(filename, "r") as f:
        l = [make_tuple(p) for p in f.read().strip().splitlines()]
        #results = [[int(i[0]), int(i[1])] for i in l]
        return l
    
  
def get_dist_matrix(filename):
      
    poczty = get("poczty.txt")
    poczty_coords = [ [round(float(p[2]),6), round(float(p[3]),6)] for p in poczty]
    indices = list(map(lambda x: x[0], poczty))
    df = pd.DataFrame(poczty_coords, columns=['lat', 'lon'], index=indices)
    dist_matrix = pd.DataFrame(distance_matrix(df.values, df.values), index=df.index, columns=df.index).to_numpy()
    return dist_matrix
