import weka.core.jvm as jvm
from weka.core.converters import Loader, Saver
import matplotlib.pyplot as plt
import pandas as pd
from scipy.io.arff import loadarff
import numpy as np

class weka_handler:

    def __init__(self):
        pass

    def load_dataset(self,file_path):
        jvm.start()
        l = Loader("weka.core.converters.ArffLoader")
        self.dataset = l.load_file(file_path)
        self.dataset_line_plot(file_path)

    def save_dataset(self,filepath):
        saver = Saver(classname="weka.core.converters.CSVSaver")
        saver.save_file(self.dataset, filepath)

    def dataset_line_plot(self,file_path):
        raw_data = loadarff(file_path)
        df_data = pd.DataFrame(raw_data[0])
        #for att in list(df_data):
            #boxplot=df_data.boxplot(column=[att])



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

    def attribute_q3(self,attribute_id):
        return np.quantile(self.get_attribute_values(attribute_id),0.5)

    def attribute_mode(self,attribute_id):
        pass

    def attribute_mean(self,attribute_id):
        return np.mean(self.get_attribute_values(attribute_id))