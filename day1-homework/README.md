# QBB2022 - Day 1 - Homework Exercises Submission


#1.





#USAGE: bash exercise1.sh input_VCF

for nuc in A C G T
do
  echo "Considering " $"nuc"
  awk '/^#/{next} {if ($4 == $nuc) {print $5}}' $1 | sort | uniq -c
done
exercise1.sh (END)



#bash exercise1.sh ~/data/vcf_files/random_snippet.vcf



#THE ERROR MESSAGE SAYS:
#Considering  A
#awk: illegal field $(), name "nuc"
#input record number 21, file /Users/cmdb/data/vcf_files/random_snippet.vcf
#source line number 1
 
 
 
 
#google: "Unix awk illegal field $()"

#makes sense biolog



#2. 


#selected the region of interest on chromosome 21, identified a gene as Adenosine Deaminase RNA Specific B1

#There are promoter-like regions (promoter-like because there are active transcription sites, enhancers, and transcription start sites nearby), and some of these regions have reasonable consensus across cell types. (some such regions can be found at approximately Human chr21: 46572213, 46590404, and 46648529)

#Though there is some consensus on the promoter regions, there is also considerable variation across cell types- the regions are not clearly and objectively defined, and the start sites of transcription are sometimes ranges.


# awk example for my reference:
#awk '{if ($1 == "chr21") {print}}' input_file


#I'm unsure of how to access the bed files version of the data from the linked resource.


cut -f 2 random_snippet.vcf     
returns chromosome positions of variant SNPs

|

bedtools intersect stdin -a -b chromHMM.E116_15_coreMarks_hg38lift_stateno.chr21.bed
pipes result as "A" into bedtools intersect; "B" contains the promoter ranges

#it says: Error: Unable to open file -b. Exiting.

#google: bedtools intersect unable to open file

cut -f 2 random_snippet.vcf | bedtools intersect -abam stdin -b chromHMM.E116_15_coreMarks_hg38lift_stateno.chr21.bed 

#it says: libc++abi: terminating with uncaught exception of type std::length_error: basic_string
#Abort trap: 6

#google: perhaps vector is not large enough to handle data? Unsure.










#3. 
#exercise3.sh:
#!/bin/bash

#USAGE: bash exercise3.sh input_VCF

awk '/^#/{next} {print $1,$2-1, $2}' $1 > variants.bed
#go to the next line? then print first column(chromosome number), (position - chromosome number?) 
#how does that make sense??), then print second column(chromosome position)... save column 1 to the file variants.bed
sort -k1,1 -k2,2n ~/data/bed_files/genes.bed > genes.sorted.bed
#sort fields 1 and 2 from genes.bed... save to genes.sorted.bed
bedtools closest -a variants.bed -b genes.sorted.bed
#run bedtools closest on the results of the first and second lines of code

#it says:
#Error: unable to open file or unable to determine types for file variants.bed

- Please ensure that your file is TAB delimited (e.g., cat -t FILE).
- Also ensure that your file has integer chromosome coordinates in the 
  expected columns (e.g., cols 2 and 3 for BED).
  
  
#I tried just this part: awk '/^#/{next} {print $1,$2-1, $2}' random_snippet.vcf

#and the result had "chr21" as the first column... I think I need to save all three columns rather than specifying just the first.

#I removed $1 from the first line of code
awk '/^#/{next} {print $1,$2-1, $2}'  > variants.bed

#result: No error message or anything... terminal simply did not respond. It's as if it froze or something. 
#I restarted terminal and tried again. It seems this operation might just take a really long time.