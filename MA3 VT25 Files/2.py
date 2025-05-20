import random
import matplotlib.pyplot as plt
import math as m
import concurrent.futures as future
from statistics import mean 
from time import perf_counter as pc

def sphere_volume(n, d): #Ex2, approximation
    #n is the number of points
    # d is the number of dimensions of the sphere 
        
    N = [[random.uniform(-1, 1) for _ in range(d)] for _ in range(n)]
    Ns = list(filter(lambda coord: sum(x**2 for x in coord) <= 1, N))
    Vs = 2**d * len(Ns)/len(N)

    return Vs

#Ex3: parallel code - parallelize for loop
def sphere_volume_parallel1(n,d,np=10):
    #n is the number of points
    # d is the number of dimensions of the sphere
    #np is the number of processes

    with future.ProcessPoolExecutor() as ex:
        results = ex.map(sphere_volume, [n]*np, [d]*np)    
    return mean(results)

if __name__ == "__main__":
    n = 100000
    d = 11
    start = pc()
    for y in range (10):
        sphere_volume(n,d)
    stop = pc()

    print(f"Ex3: Sequential time of {d} and {n}: {stop-start}")
    print("What is parallel time?")
    start = pc()
    sphere_volume_parallel1(n, d)
    stop = pc()
    print(f'Paralell_1 time of {d} and {n}: {stop - start}')
