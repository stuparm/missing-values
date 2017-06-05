#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 22:44:39 2017

@author: miha
"""
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from random import randint

class files:
    
    def read(file_name):
        data = []
        with open(file_name) as file:
            for line in file:
                data.append(line.strip().split(','))
        return data
    
    def write(file_name, data):
        np.savetxt(file_name,data,delimiter=",",fmt="%s")
        
    def read_numpy(file_name):
        data = files.read(file_name)
        return np.array(data)
    
    def read_pandas(fine_name):
        return pd.read_csv(fine_name, header=None)
    
    
    
#class kmeans:
#    
#    def __init__(self, data):
#        self.data = data
#        self.k = data.shape[1]
#        self.kmeans = KMeans(n_clusters=self.k)
#        self.kmeans.fit(data)
#    
#    def select_row_index(self, cluster_index):
#        y = self.kmeans.predict(self.data)
#        bools = y[:] == cluster_index
#        row_index = np.where(bools == True)
#        return np.array(row_index)
#    
#    def select_row(self, cluster_index):
#        row_index = self.select_row_index(cluster_index)
#        return self.data[row_index,:]
#    
#    def cluster_count(self):
#        return self.k
    
    

class dataset:
     
    def __init__(self, data):
        self.data = data
    
    def reduce(self, percentage):
        rows = self.data.shape[0]
        cols = self.data.shape[1]
        total_count = rows * cols
        percentage_decimal = percentage / 100
        reduced_count = total_count * percentage_decimal
        reduced_data = self.data.copy().astype(np.float)
        while(reduced_count > 0):
            row = randint(0,rows-1)
            col = randint(0,cols-1)
            if ~np.isnan(reduced_data[row,col]):
                reduced_data[row,col] = np.NaN
                reduced_count -= 1
        self.reduced_data = reduced_data 
    
    def column_count(self):
        return self.reduced_data.shape[1]
    
    def row_count(self):
        return self.reduced_data.shape[0]

    def remove_column(self, col_num):
        col = self.reduced_data[:,col_num]
        other = np.delete(self.reduced_data, [col_num], axis=1)
        return col,other
    
    def reduced_data(self):
        return self.reduced_data