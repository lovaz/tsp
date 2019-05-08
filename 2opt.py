import numpy as np
import nearestneighbor_runnable as nna
import ingest_poczty as ing
import networkx as nx
import matplotlib.pyplot as plt


def cost_change(cost_mat, n1, n2, n3, n4):
    return cost_mat[n1][n3] + cost_mat[n2][n4] - cost_mat[n1][n2] - cost_mat[n3][n4]


def two_opt(route, cost_mat):
    iter = 0
    best = route
    improved = True
    while improved:
        improved = False
        for i in range(1, len(route) - 2):
            for j in range(i + 1, len(route)):
                if j - i == 1: continue
                diff= cost_change(cost_mat, best[i - 1][0], best[i][0], best[j - 1][0], best[j][0])
                if diff < -0.01:
                    best[i:j] = best[j - 1:i - 1:-1]
                    improved = True
        route = best
        iter = iter +1
        if iter%1000 ==0:
            print(iter, route_sum(route, cost_mat))
    return best

def route_sum(path, cost_matrix):
    sum = 0
    for j in list(zip(path,path[1:])):
        sum = sum + cost_matrix[j[0][0]][j[1][0]]
    return sum    

if __name__ == '__main__':
    data = ing.get_simple("poczty.txt")
    path, sum =  nna.nearestneighbor(data)
      
      
    
    path_ids = [p[0] for p in path]
    print("NNA path:", path_ids, "\nNNA sum", sum)
    cost_matrix =ing.get_dist_matrix("poczty.txt").tolist()
    best_route = two_opt(path, list(cost_matrix))
    best_sum = route_sum(best_route, cost_matrix)
    print("2-opt path:", best_route, "\n2-opt sum", best_sum)
    
    A = np.array([ [p[1],p[2]] for p in best_route])
    points_only = [ [p[1],p[2]] for p in data]
    PTS= np.array(points_only)
    
    plt.plot(*A.T)
    plt.scatter(*PTS.T,  s= 2, c ='m')

    plt.show()   
    
    