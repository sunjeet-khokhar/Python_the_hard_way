# make a list from a list by removing elements that occur more than once

def remove_non_dup_list(list_input):
    list_output = []
    output_dict = {x:list_input.count(x) for x in list_input}
    print(output_dict)
    for k,v in output_dict.items():
        if v == 1:
            list_output.append(k)
    print(list_output)

L = [1,1,3,4,4,4]

remove_non_dup_list(L)

