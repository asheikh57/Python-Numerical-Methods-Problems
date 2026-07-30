from math import pi
from matplotlib import pyplot as plt

def euler(N : int = 100):
    out = [0 for _ in range(N)]
    curr_sum, exp_pi = 0, 0
    for i in range(0,N):
        k = i+1
        curr_sum += 6 / (k * k)
        exp_pi = curr_sum ** 0.5
        out[i] = exp_pi - pi

    return out

def liebniz(N : int = 100):
    out = [0 for _ in range(N)]
    curr_sum, exp_pi = 0, 0
    for i in range(0,N):
        curr_sum += 8 * 1/((4*i+1)*(4*i+3))
        exp_pi = curr_sum
        
        out[i] = exp_pi - pi
    
    return out

if __name__ == "__main__":
    print(liebniz())
    print(euler())
    plt.plot(liebniz())
    plt.plot(euler())
    plt.show()