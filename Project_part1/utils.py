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