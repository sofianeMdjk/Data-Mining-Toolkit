import math

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
        values.append(str(5*i))
    return values


def clean_list(l):
    l[-1] = (l[-1].split("\n"))[0]
    return l

def frozenset2list(fs):
    elemnts = []
    for elt in fs:
        elemnts.append(elt)
    return elemnts

def frozenset2str(fs):
    output = ""
    for elt in fs:
        output = output+elt+"-"
    return output

def formalize_rule(r):
    rule = (list(r))
    premisses = []
    rule_confidence = rule[-1]
    for i in range(len(rule)-2):
        fs = rule[i]
        print(fs)
        elt = "-".join(frozenset2list(fs))
        premisses.append(elt)

    return premisses, rule_confidence

def calculate_euclidian_distance(instance1, instance2):
    instance_length = len(instance1)-1 #No need to take in consideration the class attribute
    distance = 0
    for i in range(instance_length):
        if isinstance(instance1[i], float):
            distance += pow((float(instance1[i]) - float(instance2[i])), 2)
        else:
            if instance1[i] != instance2[i]:
                distance += 1
    eucl_distance = math.sqrt(distance)
    return eucl_distance


def append_unique(list_, elt):
    if elt not in list_:
        list_.append(elt)
    return list_


def extend_unique(list1, list2):
    for elt in list2:
        if elt not in list1:
            list1.append(elt)
    return list1


def distinct_elements_of_list(list_):
    distinct = []
    for elt in list_:
        if elt not in distinct:
            distinct.append(elt)
    return distinct


def distinct_postive_elements_of_list(list_):
    distinct = []
    for elt in list_:
        if elt not in distinct and elt > 0:
            distinct.append(elt)
    return distinct
