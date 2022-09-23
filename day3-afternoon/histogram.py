import matplotlib.pyplot as plt
import numpy as np

snp_af = np.genfromtxt("chr21_af.txt")
plt.hist(snp_af, bins=50)

plt.show()  