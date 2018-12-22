import csv
import pandas as pd


def load_dataset_split(filename, split):
    training_set = []
    test_set = []
    with open(filename, "r") as csv_file:
        lines = csv.reader(csv_file)
        dataset = list(lines)
        tr_set = int(len(dataset)*split/100)
        for i in range(1,tr_set):
            training_set.append(dataset[i])
        for i in range(tr_set,len(dataset)-1):
            test_set.append(dataset[i])
        csv_file.close()
    return training_set, test_set


def load_dataset(filename):
    return pd.read_csv(filename)


