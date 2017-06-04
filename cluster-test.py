#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 01:16:48 2017

@author: miha
"""

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns; sns.set()
import kmeans
from util import dataset

points = np.vstack(((np.random.randn(150, 2) * 0.75 + np.array([1, 0])),
                  (np.random.randn(50, 2) * 0.25 + np.array([-0.5, 0.5])),
                  (np.random.randn(50, 2) * 0.5 + np.array([-0.5, -0.5]))))


dataset = dataset(points)
dataset.reduce(5)


plt.scatter(points[:, 0], points[:, 1])
#ax = plt.gca()
#ax.add_artist(plt.Circle(np.array([1, 0]), 0.75/2, fill=False, lw=3))
#ax.add_artist(plt.Circle(np.array([-0.5, 0.5]), 0.25/2, fill=False, lw=3))
#ax.add_artist(plt.Circle(np.array([-0.5, -0.5]), 0.5/2, fill=False, lw=3))


#centroids = kmeans.cluster(points, 3)
centroids, closest = kmeans.cluster(dataset.reduced_data, 3)

arg1 = np.argwhere(closest == 0)
cluster1 = np.array(points[arg1])
print(cluster1)
plt.scatter(cluster1[:, 0], cluster1[:, 1], c='g')

whole = np.insert(points, 2, closest, axis=1)
print(whole)

print(centroids[:,0])
plt.scatter(centroids[:, 0], centroids[:, 1], c='r', s=100)

