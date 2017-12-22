# merge two sorted lists into 1 sorted list

def combine_sorted_lists(list_1,list_2):
    list_3 = []
    for x in list_1:
        list_3.append(x)   
    for x in list_2:
        list_3.append(x)
    list_3.sort
    print(list_3)

a = [3, 4, 6, 10, 11, 18]
b = [1, 5, 7, 12, 13, 19, 21]

combine_sorted_lists(a,b)
    