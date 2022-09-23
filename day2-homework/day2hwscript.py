#Create an analysis script that will import your VCF parser, load both the 1KGP genomes (random_snippet.vcf) and dbSNP (dbSNP_snippet.vcf) VCF files, and then annotate the 1KGP variants with the IDs from the dbSNP file, when appropriate. Your script should include the following features:

# Fully commented
# Loads the records from dbSNP_snippet.vcf and random_snippet.vcf
# Creates a dictionary of positions and IDs from the dbSNP file
# Replaces the ID in each record from random_snippet.vcf with the correct label, if it exists, from your dbSNP dictionary
# Finds and reports the number of random_snippet.vcf records that do not have a corresponding ID in your dbSNP ID dictionary
#

#!/usr/bin/env python3
import sys

from vcfParser.py import parse_vcf
parse_vcf()

def relabeler(fname1, fname2):
    #create a dictionary of positions and IDs from the dbSNP file
    