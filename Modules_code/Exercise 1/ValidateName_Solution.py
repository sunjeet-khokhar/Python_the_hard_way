# Your client has sent you a long list of names for use in your performance test scripts, the test engineer started writing a script 
# to validate the format of the names but had to leave and has asked you to finish it.
# Your task is to complete the validate_name function to complete the script.

import re

def validate_name(name):
    '''
    Returns True if the name is valid, False if not based off the following rules
    - the name has a max character length of 20
    - the name consists of only alpha characters (ie a-zA-Z) and space characters
    '''
    out = True
    if len(name) > 20:
        out = False
    elif not all(c.isalpha() or c.isspace() for c in name):
        out = False
    return out

def validate_name2(name):
    '''
    Returns True if the name is valid, False if not based off the following rules
    - max character length = 20
    - must be two alpha only words seperated by a non alpha character

    '''
    name = name
    out = True
    if len(name) > 20:
        out = False
    elif not re.match(r'^[a-z]*[^a-z][a-z]*$', name, re.I):
        out = False
    return out


def main():
    with open('names.txt') as f:
        lines = f.readlines()
    f.closed
    
    valid_names = []
    invalid_names = []
    
    for line in lines:
        name = line.rstrip()
        valid = validate_name(name)
        if valid:
            valid_names.append(name)
        else:
            invalid_names.append(name)
    
    print("Total count of records imported: " + str((len(valid_names) + len(invalid_names))))
    print("Count of imported records that meet the selected criteria: " + str(len(valid_names)))
    print("list of invalid names")
    print("---------------------")
    for name in invalid_names:
        print(name)


if __name__ == "__main__":
    main()

# Extension exercises
# - Complete the validate_name2 function
# - Save the list of valid names to a file
# - 




# Future topics
# ----------------------
# Test framework
# Regex
# Objects
# Dictionary / Set / Tuples
# Recursion
# Library
# - Intenet access
# - Timing
# - JSON
# Lambda
# Iterators / Generators
# Exceptions