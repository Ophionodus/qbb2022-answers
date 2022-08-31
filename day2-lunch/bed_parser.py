#!/usr/bin/env python3

import sys

def parse_bed(fname):
    try:
        fs = open(fname, 'r')
    except:
        raise FileNotFoundError("That file doesn’t appear to exist")
    bed = []
    field_types = [str, int, int, str, float, str, int, int, list, int, list, list]
    for i, line in enumerate(fs):
        if line.startswith("#"):
            continue
        fields = line.rstrip().split()
        fieldN = len(fields)
        if fieldN < 3 or fieldN == 10 or fieldN == 11 or fieldN > 12:
            print(f"Line {i} appears malformed", file=sys.stderr)
            continue
             
        try:
            for j in range(min(len(field_types), len(fields))):
                fields[j] = field_types[j](fields[j])
                if fields[j] == 8 and len(fields[8]) != 3:
                    print (fields[0],fields [1], fields[2])
                    print ("wrong number of integers in RBG", file=sys.stderr)
                    
                if fields[j] == 12 and fields[9] != len(fields[10]) or fields[9] != len(fields[11]):
                    print (fields[0],fields [1], fields[2])
                    print (f" in line {i} bed12 error, number of blockstarts or blocksizes integers mismatches blockcount", file=sys.stderr)
                    
                if len[fields] == 12:
                    fields[11].rstrip(",").split()
                    fields[10].rstrip(",").split()
                    
            bed.append(fields)
            
        except:
            print(f"Line {i} appears malformed", file=sys.stderr)
    fs.close()
    return bed

if __name__ == "__main__":
    fname = sys.argv[1]
    bed = parse_bed(fname)
    