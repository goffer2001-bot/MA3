""" MA3.py

Student:
Mail:
Reviewed by:
Date reviewed:

"""
import random
import matplotlib.pyplot as plt
import math as m
import concurrent.futures as future
from statistics import mean 
from time import perf_counter as pc

def approximate_pi(n): # Ex1
    #n is the number of points
    # Write your code here
    N = [(random.uniform(-1, 1), random.uniform(-1, 1)) for _ in range(n)]
    Nc = [(i, j) for i, j in N if (i**2 + j**2) < 1]
    Ns = [(i, j) for i, j in N if ((i**2 + j**2)) > 1]
    pi = 4*len(Nc)/n

    x_Nc = [k[0] for k in Nc]
    y_Nc = [k[1] for k in Nc]
    x_Ns = [k[0] for k in Ns]
    y_Ns = [k[1] for k in Ns]

    plt.scatter(x_Nc, y_Nc, color = 'red', s = 1)
    plt.scatter(x_Ns, y_Ns, color = 'blue', s = 1)
    plt.title('Plot of coordinates with Monte-Carlo simulations')
    plt.show()

    return pi

def sphere_volume(n, d): #Ex2, approximation
    #n is the number of points
    # d is the number of dimensions of the sphere 
        
    N = [[random.uniform(-1, 1) for _ in range(d)] for _ in range(n)]
    Ns = list(filter(lambda coord: sum(x**2 for x in coord) <= 1, N))
    Vs = 2**d * len(Ns)/len(N)

    return Vs

def hypersphere_exact(d): #Ex2, real value
    # d is the number of dimensions of the sphere 
    V = (m.pi**(d/2))/(m.gamma(1 + d/2))
    return V

#Ex3: parallel code - parallelize for loop
def sphere_volume_parallel1(n,d,np):
    #n is the number of points
    # d is the number of dimensions of the sphere
    #np is the number of processes

    with future.ProcessPoolExecutor() as ex:
        results = list(ex.map(sphere_volume, [n]*np, [d]*np))    
    return mean(results)

# Ex4: parallel code - parallelize actual computations by splitting data

def sphere_volume_parallel2(n,d,np=10):
    #n is the number of points
    # d is the number of dimensions of the sphere
    #np is the number of processes
    parts = n // np
    with future.ProcessPoolExecutor() as ex:
        results = ex.map(sphere_volume, [parts]*np, [d]*np)

    return mean(results)
    
    
def main():
    """
    #Ex1
    dots = [1000, 10000, 100000]
    for n in dots:
        approximate_pi(n)
    #Ex2
    n = 100000
    d = 2
    sphere_volume(n,d)
    print(f"Actual volume of {d} dimentional sphere = {hypersphere_exact(d)}")

    n = 100000
    d = 11
    sphere_volume(n,d)
    print(f"Actual volume of {d} dimentional sphere = {hypersphere_exact(d)}")

    #Ex3
    n = 100000
    d = 11
    np = 10
    start = pc()
    for y in range (10):
        sphere_volume(n,d)
    stop = pc()

    print(f"Ex3: Sequential time of {d} and {n}: {stop-start}")
    print("What is parallel time?")
    start = pc()
    sphere_volume_parallel1(n, d, np)
    stop = pc()
    print(f'Paralell_1 time of {d} and {n}: {stop - start}')
    """
    
    #Ex4
    n = 1000000
    d = 11
    start = pc()
    result_1 = sphere_volume(n,d)
    stop = pc()
    print(f"Ex4: Sequential time of d = {d} and n = {n}: {round(stop-start, 2)} s")
    print(f'Calculated Volume: {round(result_1, 5)}')

    start = pc()
    result_2 = sphere_volume_parallel2(n,d)
    stop = pc()
    print(f'Paralell time of d = {d} and n = {n}: {round(stop-start, 2)} s')
    print(f'Calculated Volume: {round(result_2, 5)}')

    print(f'True Sphere Volume: {round(hypersphere_exact(d), 5)}')

    


if __name__ == '__main__':
	main()
    
