

#VCF = ~/qbb2022-answers/day3-homework/ALL.chr21.shapeit2_integrated_v1a.GRCh38.20181129.phased.vcf.gz

#     --vcf                      specified location of our VCF file                                         --double-id      told plink to duplicate the id of the samples    
#     --allow-extra-chr          allows additional chromosomes beyond the human chromosome set             
#     --indep-pairwise           first argument, 50, denotes a window of 50 Kb      second argument, 10, is the window step size in bp     third argument, 0.1, is the r^2 threshold
#     --out                      produces the prefix for the output data
#
#




#plink --vcf $VCF --double-id --allow-extra-chr \
#--set-missing-var-ids @:# \
#--indep-pairwise 50 10 0.1 --out bootcamp






#plink --vcf $VCF --double-id --allow-extra-chr --set-missing-var-ids @:# \
#--extract bootcamp.prune.in \
#--make-bed --pca --out shoesleep






#plink --vcf $VCF --allow-extra-chr --set-missing-var-ids @:# \
 #\
#--make-bed --pca 3 --out moccassinsomniferance






#--pca [count] [{approx | meanimpute}] ['scols='<col set descrip.>]
#--pca [{allele-wts | biallelic-var-wts}] [count] [{approx | meanimpute}]
#      ['vzs'] ['scols='<col set descrip.>] ['vcols='<col set descrip.>]

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