from classification_algorithms.dataset_split import train_test_split

df = load_data("../classification_datasets/iris.data.txt")
train_test_split(df,75)