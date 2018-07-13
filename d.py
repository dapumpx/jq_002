import argparse

import numpy as np
from scipy import special, optimize, signal 
import matplotlib.pyplot as plt

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(usage=__doc__)
    parser.add_argument("--order", type=int, default=3, help="order of Bessel function")
    parser.add_argument("--output", default="plot.png", help="output image file")
    args = parser.parse_args()

    # Compute maximum
    f = lambda x: -special.jv(args.order, x)
    sol = optimize.minimize(f, 1.0)

    # Plot
    x = np.linspace(0, 10, 5000)
    plt.plot(x, special.jv(args.order, x), '-', sol.x, -sol.fun, 'o')

    # Produce output
    plt.savefig(args.output, dpi=96)

def play_matplotlib():
    # x = np.linspace(-1, 1, 50)
    # y = 2*x + 1

    # print(x)
    # print(y)
    v = np.array([ 0.56660112,  0.76309473,  0.69597908,  0.38260156,  0.24346445, 0.56021785,  0.24109326,  0.41884061,  0.35461957,  0.54398472, 0.59572658,  0.92377974])
    plt.figure()
    plt.plot([0, 1,2,3,4,5,6,7,8,9,10,11], v)
    
    a = signal.argrelextrema(v, np.greater)
    b = signal.argrelextrema(v, np.less)

    # print(a)

    for aa in a:
        plt.plot(aa, v[aa], 'ro')

    for bb in b:
        plt.plot(bb, v[bb], "go")
        
    plt.show()


if __name__ == "__main__":
    play_matplotlib()