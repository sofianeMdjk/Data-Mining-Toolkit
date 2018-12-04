import csv
import random
def load_dataset(filename, split):
    training_set = []
    test_set = []
    with open(filename, "r") as csv_file:
        lines = csv.reader(csv_file)
        dataset = list(lines)
        tr_set = int(len(dataset)*split/100)
        for i in range(tr_set):
            training_set.append(dataset[i])
        for i in range(tr_set,len(dataset)-1):
            test_set.append(dataset[i])

    return training_set, test_set
