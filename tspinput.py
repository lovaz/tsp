"""Convert TSP input file to required format."""

def get(filename):
    with open(filename, "r") as f:
        f.readline()
        l = ([p.split() for p in f.read().strip().splitlines()])
        results = [[int(i[0]), int(i[1])] for i in l]
        return results
