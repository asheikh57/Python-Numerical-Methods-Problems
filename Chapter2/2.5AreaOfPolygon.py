
def polyarea(x,y):
    assert(len(x) == len(y))
    off = 1
    length = len(x)
    agg1, agg2 = 0, 0
    for i in range(length):
        agg1 += x[i]*y[(i+off) % length]
        agg2 += y[i]*x[(i+off) % length]
    area = 0.5*(agg1 - agg2) if agg1 - agg2 > 0 else 0.5*(agg2 - agg1)
    return area

if __name__ == "__main__":
    x = [0,0,1,1]
    y = [0,1,1,0]
    print(polyarea(x,y))