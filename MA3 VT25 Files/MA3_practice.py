import random
import matplotlib.pyplot as plt
import math as m
import concurrent.futures as future
from statistics import mean 
from time import perf_counter as pc
from time import sleep as pause
# import multiprocessing as mp
import concurrent.futures as future

def approximate_pi(n): # Ex1
    #n is the number of points
    # Write your code here
    N = [(random.uniform(-1, 1), random.uniform(-1, 1)) for _ in range(n)]
    Nc = [(i, j) for i, j in N if (i**2 + j**2) < 1]
    Ns = [(i, j) for i, j in N if ((i**2 + j**2)) > 1]
    pi = 4*len(Nc)/len(N)

    x_Nc = [k[0] for k in Nc]
    y_Nc = [k[1] for k in Nc]
    x_Ns = [k[0] for k in Ns]
    y_Ns = [k[1] for k in Ns]

    plt.scatter(x_Nc, y_Nc, color = 'red', s = 1)
    plt.scatter(x_Ns, y_Ns, color = 'blue', s = 1)
    plt.title('Plot of coordinates in N')
    plt.show()

    return pi

# approximate_pi(100000)

def sphere_volume(n, d): #Ex2, approximation
    #n is the number of points
    # d is the number of dimensions of the sphere 
    def in_sphere(coord):
        sum_ = sum(i**2 for i in coord)
        if sum_ < 1:
            return True
        else:
            return False
        
    N = [[random.uniform(-1, 1) for _ in range(d)] for _ in range(n)]
    Ns = list(filter(in_sphere, N))
    Vs = 2**d * len(Ns)/len(N)

    return Vs

# print(sphere_volume(10, 3))


def runner(n):
    print(f'Performing a costly function {n}')
    pause(n)
    print(f'Function {n} Completed')

"""
if __name__ == '__main__':
    start = pc()
    for _ in range(10):
        runner()
    end = pc()
    print(f'Process took {round(end - start, 2)} seconds')
"""

"""
if __name__ == '__main__':
    start = pc()
    p1 = mp.Process(target = runner)
    p2 = mp.Process(target = runner)
    

    p1.start()
    p2.start()
    p1.join()
    p2.join()

    end = pc()
    print(f'Process took {round(end - start, 2)} seconds')
"""

if __name__ == "__main__":
    start = pc()

    with future.ThreadPoolExecutor() as ex:
        p = [5, 4, 3, 2, 1]
        results = ex.map(runner, p)

        for r in results:
            print(r)

    end = pc()
    print(f"Process took {round(end-start, 2)} seconds")






