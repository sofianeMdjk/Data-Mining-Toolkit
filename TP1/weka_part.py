import weka.core.jvm as jvm
from weka.core.converters import Loader



def load_dataset(file_path):
    global dataset
    jvm.start()
    l = Loader("weka.core.converters.ArffLoader")
    dataset = l.load_file(file_path)

def att_display():
    print("the data set instance is : ",dataset)
    print(dataset)
    print(dataset.summary(dataset))
    print("Dataset summary")
    print("\t \t name   type")

    for i in range(dataset.num_attributes):
        print(dataset.attribute(i))
        print("the number of attributes :" + str(dataset.num_attributes))
        print("the number of instances :" + str(dataset.num_instances))


def display_benchmarks():
    print("waiting for benchmarks")


