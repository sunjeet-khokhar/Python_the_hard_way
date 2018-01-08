def panildrome(s):
    string_to_check = str(s)
    if (string_to_check == ''.join(reversed(string_to_check))):
        print("the given string is a panildrome")
    else:
        print("the given string is not a panildrome")
    print(''.join(reversed(string_to_check)))
        
panildrome("arora")
panildrome(11112)

