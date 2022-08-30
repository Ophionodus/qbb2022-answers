# QBB2022 - Day 1 - Lunch Exercises Submission

 1. I’m excited to learn how, in python, to make one boolean reverse another in response to a command in a state based way.
 
 
 
 
 
 The mean number of exons per gene was 63.
 
 I got this by first going into the day 1 lunch directory via the cd command, then used the wc command with the -l modifier to get a count of the number of lines.
 
 
 
 
 
 
 
 I would get the median by 
 
 1.  finding a way to get the program to check if the start and end chromosome positions of a given exon are within the bounds of a given gene
 
 2.  creating a set of exons for each gene
 
3.  converting the exons for each gene themselves, instead into numbers of exons

4.  sorting and finding the median of that data set







regions of the genome classified for each state:

(base) [~/qbb2022-answers/day1-lunch $]cut -f 4 chromHMM.E116_15_coreMarks_hg38lift_stateno.chr21.bed |  sort | uniq -c
 305 1
  17 10
  17 11
  30 12
  62 13
 228 14
 992 15
 678 2
  79 3
 377 4
 808 5
 148 6
1050 7
 156 8
 654 9
 
 
 
 
 I would determine which state comprises the largest fraction of the genome by 
 
 sorting the information by state number as before
 
 taking the difference between the starting and ending chromosome numbers (column 3 minus column 2)
 
 adding up these differences, separated by state number... this seems tricky
 
 the largest sum comprises the largest fraction by nucleotide.
 
 




