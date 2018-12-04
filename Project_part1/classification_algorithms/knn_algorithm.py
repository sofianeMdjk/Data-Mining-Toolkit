from classification_algorithms.dataset_split import load_dataset
import math
import operator
import nltk

def calculate_euclidian_distance(instance1, instance2):
    instance_length = len(instance1)-1 #No need to take in consideration the class attribute
    distance = 0

    for i in range(instance_length):
        distance += pow((float(instance1[i]) - float(instance2[i])), 2)
    eucl_distance = math.sqrt(distance)
    return eucl_distance


def get_k_neighbors(k,training_set, test_instance):
    distances = []
    k_neighbors = []
    for instance in training_set:
        #Calculating distance between an instance of training set and our test instance
        euc_distance = calculate_euclidian_distance(instance, test_instance)
        distances.append((instance,euc_distance))

    #sorting the disntances list depending on the
    distances.sort(key=operator.itemgetter(1))
    for i in range(k):
        k_neighbors.append(distances[i][0])

    return k_neighbors


def class_chooser(neighbors_list):
    classes_occurances = {}
    for neighbor in neighbors_list:
        class_name = neighbor[-1]
        if class_name in classes_occurances:
            classes_occurances[class_name] += 1
        else:
            classes_occurances[class_name] = 1

    #returning the class that appears the most
    return sorted(classes_occurances.items(), key=operator.itemgetter(1),reverse=True)[0][0]


def get_accuracy(test_set, predicitons):
    accurate_classifications = 0
    for i in range(len(test_set)):
        if test_set[i][-1] == predicitons[i]:
            accurate_classifications +=1

    return float(accurate_classifications/len(test_set))


def run_knn(dataset_path, training_percentage, k):
    training_set, test_set = load_dataset(dataset_path,training_percentage)
    predictions = []
    for instance in test_set:
        neighbors = get_k_neighbors(k, training_set, instance)
        classification_result = class_chooser(neighbors)
        print(classification_result)
        predictions.append(classification_result)
    classification_accuracy = get_accuracy(test_set, predictions)

    return classification_accuracy

accuracy = run_knn("../classification_datasets/iris.data", 83, 7)
print(accuracy)