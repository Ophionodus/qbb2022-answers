#!/usr/bin/env python3

import sys

#defines parse_vcf as a function with a string value equal to the filename     fname is the argument.  (a piece of info being passed intio a function)       parse_vcf is a function, much like print or open.
def parse_vcf(fname):
    #makes an empty list called vcf
    vcf = []
    #makes an empty set called info_description
    info_description = {}
    #makes an empty set called info_type
    info_type = {}
    #makes an empty dictionary called format_description
    format_description = {}
    #makes a eponymous dictionary of functions used to convert data to a given type
    type_map = {
        "Float": float,
        "Integer": int,
        "String": str
        }
    #starts the count for error lines at zero
    malformed = 0
    #attempts to open the file of interest, reports any failure to do so
    try:
        fs = open(fname)
    except:
        raise FileNotFoundError(f"{fname} does not appear to exist", file=sys.stderr)
    
    #starts a for loop
    for h, line in enumerate(fs):
        #if the line the for loop is currently on starts with #,
        if line.startswith("#"):
            #start the process of trying to make the header; if things go awry, say "Malformed header"
            try:
                #if the line starts with the text "##format", do this... if the line starts with "##INFO", do the other... if the line starts with "#CHROM", do the third.
                if line.startswith("##FORMAT"):
                    #formats the fields; strips characters from the end of the string, specifically ">/r/n"
                    fields = line.split("=<")[1].rstrip(">\r\n") + ","
                    #creates a variable
                    i = 0
                    #creates a variable
                    start = 0
                    #creates a boolean and sets it to False
                    in_string = False
                    #so long as the variable i has a value less than that of the number of fields,  ...
                    while i < len(fields):
                        #if the current field of interest is a comma and is not in string, ...
                        if fields[i] == "," and not in_string:
                            #I do not fully understand this line, I WILL ASK QUESTIONS ABOUT IT.                          !
                            name, value = fields[start:i].split('=')
                            #if the name is "ID", make that the value
                            if name == "ID":
                                ID = value
                            #if the name is instead "Description", make "desc" the value
                            elif name == "Description":
                                desc = value
                            #sets the integer value of the start variable to: one greater than the i variable
                            start = i + 1
                        # if instead the current field of interest is a double-quote delimiter, ...
                        elif fields[i] == '"':
                            #reverse the boolean status of in_string
                            in_string = not in_string
                        #increases the value of the i variable by 1
                        i += 1
                    #summons forth "ID" as one of the items in the set known as format_description. I am unsure as to how the strip command is functioning here.
                    format_description[ID] = desc.strip('"')
                #option number two of the for loop; if instead the line starts with "##INFO", ...
                elif line.startswith("##INFO"):
                    #formats the fields; strips characters from the end of the string
                    fields = line.split("=<")[1].rstrip(">\r\n") + ","
                    #sets the variable i at an integer value of zero
                    i = 0
                    #sets the variable start at an integer value of zero
                    start = 0
                    #sets the boolean in_string to False
                    in_string = False
                    #so long as the variable i has a value less than that of the number of fields, ...
                    while i < len(fields):
                        #if the field is a comma and the boolean in_string is currently False, ...
                        if fields[i] == "," and not in_string:
                            #set the name and value... I do not fully understand this syntax.                      !
                            name, value = fields[start:i].split('=')
                            #if the name reads "ID", set the ID variable equal to value
                            if name == "ID":
                                ID = value
                            #if instead the name reads "Description", set the desc variable equal to value
                            elif name == "Description":
                                desc = value
                            #if instead the name reads "Type", set the Type variable equal to value
                            elif name == "Type":
                                Type = value
                            #sets the start variable to an integer value one greater than the integer value of the i variable
                            start = i + 1
                        #if the field of index-number i is a double-quote delimiter, reverse the boolean value of in_string
                        elif fields[i] == '"':
                            in_string = not in_string
                        #increase the integer value of the variable i by one
                        i += 1
                    #adds to the empty dictionary in such a way as to pair IDs and descriptions                   !
                    info_description[ID] = desc.strip('"')
                    #sets an item in the set info_type as the variable Type
                    info_type[ID] = Type
                #option number three of the for loop; if instead the line starts with "#CHROM", ...
                elif line.startswith('#CHROM'):
                    #formats the fields; strips "#" characters from the end of the string
                    fields = line.lstrip("#").rstrip().split("\t")
                    
                    vcf.append(fields)
            #if the header is not clearly defined, say malformed header.
            except:
                raise RuntimeError("Malformed header")
        #if the line DOESN't start with #, it's not part of the header; enter this try loop that adds one to the counter of malformed lines should something go awry
        else:
            try:
                #formats fields
                fields = line.rstrip().split("\t")
                fields[1] = int(fields[1])
                #if field 5 does not contain a "."
                if fields[5] != ".":
                    #convert it to a float
                    fields[5] = float(fields[5])
                #makes an empty set known as info
                info = {}
                #formats field 7 with a split at the ;
                for entry in fields[7].split(";"):
                    #Unsure about this line. Review.                             !
                    temp = entry.split("=")
                    #if the length of the variable temp is equal to 1
                    if len(temp) == 1:
                        #set the zeroth item in temp to None
                        info[temp[0]] = None
                    #if the length of the variable
                    else:
                        name, value = temp
                        Type = info_type[name]
                        info[name] = type_map[Type](value)
                fields[7] = info
                if len(fields) > 8:
                    fields[8] = fields[8].split(":")
                    if len(fields[8]) > 1:
                        for i in range(9, len(fields)):
                            fields[i] = fields[i].split(':')
                    else:
                        fields[8] = fields[8][0]
                vcf.append(fields)
            #adds one to the malformed lines counter (variable "malformed") if something goes awry in the above try loop
            except:
                malformed += 1
    #changes item seven of the zeroth item of the list known as vcf equal to the variable item_description
    vcf[0][7] = info_description
    #if the length of the first position in the list known as vcf is greater than 8 items, ...
    if len(vcf[0]) > 8:
        #change item eight of the zeroth item of the list known as vcf equal to the variable format_description
        vcf[0][8] = format_description
    # if the variable malformed has a positive integer value, ...
    if malformed > 0:
        #report the number of malformed entries as an error message
        print(f"There were {malformed} malformed entries", file=sys.stderr)
    #spit out the list known as vcf
    return vcf
#prints vcf at the variable i, conditionally based on filename
if __name__ == "__main__":
    fname = sys.argv[1]
    vcf = parse_vcf(fname)
    for i in range(10):
        print(vcf[i])
