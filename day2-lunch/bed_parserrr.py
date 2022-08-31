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
        
        assert fieldN > 3
        assert fieldN != 10 
        assert fieldN != 11
        assert fieldN < 12
             
        try:
            for j in range(min(len(field_types), len(fields))):
                fields[j] = field_types[j](fields[j])
                assert fields[j] == 8 and len(fields[8]) != 3

                    
                assert fields[j] == 12 and fields[9] != len(fields[10]) or fields[9] != len(fields[11])

                    
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
    