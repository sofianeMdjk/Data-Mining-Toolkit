
import pandas as pd

def load_data(path):
    df = pd.read_csv(path)
    return df

def train_test_split(data,training):
    df_size = len(data.index)
    training_set_num_rows = int(df_size*training/100)
    #test_set_num_rows = df_size-training_set_num_rows
    training_set = data[0:training_set_num_rows]
    test_set = data[training_set_num_rows:df_size]
    return training_set,test_set

def load_split_data(dataset_path, training):
    df = load_data(dataset_path)
    training_set, test_set = train_test_split(df, training)

    return training_set, test_set
