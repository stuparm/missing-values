#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 23:06:10 2017

@author: miha
"""

from util import files
#from util import kmeans
import kmeans
from util import dataset
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans



data = files.read_numpy("data.csv")

dataset = dataset(data)
dataset.reduce(10)



row_count = dataset.row_count()
column_count = dataset.column_count()

populated = np.array((row_count,column_count))


for col in range(0,column_count):
    removed = dataset.remove_column(col)
    y = removed[0]
    X = removed[1]
    k = kmeans.get_centroid_count(y)
    centroids, closest = kmeans.cluster(dataset.reduced_data, k)
    
    
    
    
    
    
x = dataset.remove_column(2)
print(x[0].shape)
print(x[1].shape)

#kmeans = kmeans(data)
#a = kmeans.select_row_index(2)
