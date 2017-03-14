""" Numerical approximation to pi using Monte Carlo approx """
import random as rand
import sys
import time

def monte_carlo_approximation(n, step):
    """ Approximates pi using n samples. """
    n_in = 0
    for i in range(0, n):
        x, y = rand.random(), rand.random()
        if (x**2 + y**2 <= 1):
            n_in  += 1
        if ((i+1) % step == 0):
            p = n_in / i
            approx = p * 4.0
            print("Number of samples: {}\t\tPI: {}".format(i, approx) , end="\r", flush=True)
    p = n_in / n
    approx = p * 4.0
    print("Number of samples: {}\t\tPI: {}".format(n, approx))


if __name__ == "__main__":
    if (len(sys.argv) == 3):
        n = int(sys.argv[1])
        step  = int(sys.argv[2])    
    else:
        n    = 9000000
        step = 100000
    monte_carlo_approximation(n, step)

