def crossing_point(interval: tuple=(-4,4), N: int=400, f = lambda x : x, g = lambda x : x * x, epsilon : float = 0.01):
    assert(len(interval) == 2)
    beg, end = interval
    assert(end > beg)
    dx = (end - beg) / N
    curr = beg - dx
    while((curr := curr + dx) < end):
        if abs(f(curr) - g(curr)) < epsilon:
            return curr

if __name__ == "__main__":
    print(crossing_point())
    for i in range(2,10):
        print(crossing_point(N=400*i))