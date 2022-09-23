# QBB2022 - Day 3 - Homework Exercises Submission


#1
VCF=~/qbb2022-answers/day3-homework/ALL.chr21.shapeit2_integrated_v1a.GRCh38.20181129.phased.vcf.gz



plink --vcf $VCF --allow-extra-chr --set-missing-var-ids @:# \
 \
--make-bed --pca 3 --out moccassinsomniferance


#2 unfinished:
#!/usr/bin/env python
import sys
import numpy as np
import matplotlib.pyplot as plt

fname = sys.argv[1]
thedata = np.genfromtxt(fname, dtype = None, encoding = None, names = ["ID", "ID2", "eigenvector1", "eigenvector2", "eigenvector3"]) 

try:
    np.save("numpysaveoutput1", thedata)
except:
    print("didntsave")
    
print(thedata[3])
print(thedata[4])
print(thedata[5])

x = thedata["eigenvector1"]
y = thedata["eigenvector2"]
z = thedata["eigenvector3"]           
                      
fig, ax = plt.subplots() # create a figure and axes
ax.scatter(x, y, z)
ax.set_xlabel("firsteigenvector")
ax.set_ylabel("secondeigenvector") 
ax.set_zlabel("thirdeigenvector")   
plt.scatter(x, y, z)
plt.show()
