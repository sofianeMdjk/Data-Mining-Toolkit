import weka.core.jvm as jvm
from weka.core.converters import Loader, Saver
import numpy as np

class weka_handler:

    def __init__(self):
        pass

    def load_dataset(self,file_path):
        jvm.start()
        l = Loader("weka.core.converters.ArffLoader")
        self.dataset = l.load_file(file_path)

    def save_dataset(self,filepath):
        saver = Saver(classname="weka.core.converters.CSVSaver")
        saver.save_file(self.dataset, filepath)

    def attribute_min(self):
        print(self.dataset.attribute(0).lower_numeric_bound)

    def get_instance_list(self,index):
        return  str(self.dataset.get_instance(index)).split(",")

    def get_instances(self):
        instances = {}
        for i in range(0,self.dataset.num_instances):
            instances[i]=self.get_instance_list(i)
        return instances


    def get_attributes(self):
        attributes = []
        for i in range(self.dataset.num_attributes):
            attributes.append(self.dataset.attribute(i).name)
        return attributes

    def get_attribute_values(self, attribute_id):
        return np.array(self.dataset.values(attribute_id))

    def attribute_min(self,attribute_id):
        return np.min(self.get_attribute_values(attribute_id))

    def attribute_max(self,attribute_id):
        return np.max(self.get_attribute_values(attribute_id))

    def attribute_median(self,attribute_id):
        return np.median(self.get_attribute_values(attribute_id))

    def attribute_midrange(self):
        pass