#!/usr/bin/env python

import numpy
from scipy.stats import binomtest
import matplotlib.pyplot as plt
import seaborn
from statsmodels.stats.multitest import multipletests

arr = numpy.array([[0,1], [2,3]])

row_indeces = []
col_indeces = []
values = []
for row_index, row in enumerate(arr):
    for col_index, number in enumerate(row):
        row_indeces.append(row_index)
        col_indeces.append(col_index)
        values.append(number)
        
for i in range(len(values)):
    print(row_indeces[i], col_indeces[i], values[i])
        
        
        