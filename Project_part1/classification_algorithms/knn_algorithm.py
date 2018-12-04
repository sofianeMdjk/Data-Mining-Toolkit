from classification_algorithms.dataset_split import load_split_data
import math

def calculate_euclidian_distance(instance1, instance2):
    instance_length = len(instance1)-1 #No need to take in consideration the class attribute
    distance = 0
    for i in range(instance_length):
        distance += pow((instance1[i]-instance2[i]),2)
    eucl_distance = math.sqrt(distance)
    return eucl_distance


training_set, test_set = load_split_data("../classification_datasets/iris.data.txt",70)
