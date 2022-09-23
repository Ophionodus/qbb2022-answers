#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np

x = [1, 2, 3]

y = [10, 25, 30]
genes_per_chrom = np.genfromtxt("genes_per_chrom.txt",
                                dtype = None,
                                encoding =None,
                                names = ["gene_count", "chrom_name"])
fig, ax = plt.subplots() 
ax.plot(x, y)
                               
print(genes_per_chrom["gene_count"])
plt.show()  