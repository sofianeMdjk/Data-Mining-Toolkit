def unique(list1):
    # intilize a null list
    unique_list = []

    # traverse for all elements
    for x in list1:
        # check if exists in unique_list or not
        if x not in unique_list:
            unique_list.append(x)
            # print list
    return unique_list

def get_box_numerical_values():
    values = []
    for i in range(20):
        values.append(5*i)
    return values

