#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 21:16:06 2017

@author: miha
"""
import numpy as np
from random import randint

from util import files
from util import dataset

np.set_printoptions(threshold=np.nan)

def initialize_centroids(data, k):
    """returns k centroids from the initial points"""
    rows = data.shape[0]
    m = 0
    centroids = np.array([])
    while m < k:
        i = randint(0,rows-1)
        row = data[i,:]
        if np.isnan(row).any():
            continue
        elif centroids.size is 0:
            centroids = row
            m += 1
        else:
            centroids = np.vstack((centroids, row))
            m += 1
    return centroids


def closest_centroid(data, centroids):
    """return array with indexes of nearest centroid"""
    rows_count = len(data)
    centroids_count = len(centroids)
    all_distances = np.zeros((rows_count, centroids_count))
    i = 0;
    for instance_row in data:
        instance = np.array(instance_row)
        j = 0;
        for centroid_row in centroids:
            centroid = np.array(centroid_row)
            distance = calculate_distance(instance, centroid)
            all_distances[i,j] = distance
            j += 1
        i += 1
    return np.argmin(all_distances, axis = 1)
    
    
def calculate_distance(instance, centroid):
    """calculate distance between specific row/instance and centroid"""
    total_count = len(instance)
    nan_args = np.argwhere(np.isnan(instance))
    nan_count = len(nan_args)
    values_count = total_count - nan_count;
    instance[nan_args] = centroid[nan_args] 
    squared = (((instance - centroid) * (total_count/values_count))**2)
    squared_sum = np.sqrt(squared.sum()) 
    return squared_sum 


def update_centroids(data, centroids, closest_centroid):
    centroids_count = len(centroids)
    for i in range(0,centroids_count):
        cluster_args = np.argwhere(closest_centroid == i)
        cluster_members = data[cluster_args]
        new_centroid = np.nanmean(cluster_members, axis = 0)
        centroids[i,:] = new_centroid
    return centroids

def has_converged(old_centroids, new_centroids, itreations):
    MAX_ITERATIONS = 1000
    if (itreations > MAX_ITERATIONS):
        return True
    return np.array_equal(old_centroids,new_centroids)

def cluster(data, k):
    iterations = 1
    centroids = initialize_centroids(data, k)
    old_centroids = np.copy(centroids)
    closest = closest_centroid(data, centroids)
    new_centroids = update_centroids(data, centroids, closest)
    
    while not has_converged(old_centroids, new_centroids, iterations):
        old_centroids = np.copy(new_centroids)
        closest = closest_centroid(data, new_centroids)
        new_centroids = update_centroids(data, new_centroids, closest)
        iterations += 1
     
    print("Total iterations: "+str(iterations))
    print(new_centroids)
    return [new_centroids, closest]
    
        
        
    
"""   
niz = np.array([2,2])
args = np.argwhere(np.isnan(niz))
pun = np.array([1,4,1,2,3,4])

niz[args] = pun[args]

a = np.argwhere(pun == 1)
print(a)



data = files.read_numpy("data.csv")
dataset = dataset(data)
dataset.reduce(20)

cluster(dataset.reduced_data, 4)



print(len(data))

centroids = initialize_centroids(dataset.reduced_data, 4)
print(centroids)
closest = closest_centroid(dataset.reduced_data, centroids)
updated = update_centroids(dataset.reduced_data, centroids, closest)
print(updated)
print(has_converged(centroids, updated, 1))
print(np.array_equal(centroids,updated))
"""