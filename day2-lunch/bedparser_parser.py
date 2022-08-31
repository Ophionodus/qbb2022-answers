import sys

#imports bed parser
import bed_parser
bed_parser.bed_parser()

#opens a bed file
try:
        fs = open(fname, 'r')
    except:
        raise FileNotFoundError("That file doesn’t appear to exist")





#had previously been used to run my bed_parser.py
python bed_parser.py hg38_gencodev41_chr21.bed