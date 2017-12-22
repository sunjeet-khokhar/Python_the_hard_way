#Build a string with the numbers from 0 to 100, "0123456789101112..."
def build_string(end_range):
    list_1 = [x for x in range(end_range)]
    # we have to convert the elements of the list to a string for the join method to work
    print(''.join(str(list_1)))

build_string(1000)

    