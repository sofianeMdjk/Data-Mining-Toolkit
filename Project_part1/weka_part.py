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
        raw_data = loadarff(file_path)
        self.df_data = pd.DataFrame(raw_data[0])

    def save_dataset(self,filepath):
        saver = Saver(classname="weka.core.converters.CSVSaver")
        saver.save_file(self.dataset, filepath)

    def hist_plot(self):
          for att in self.df_data :
            if att != "class":
                plt.hist(self.df_data[att], bins= 20, rwidth=0.50, label=att)
          plt.legend()
          plt.show()

    def box_plot(self):
         data_list = [self.df_data[att] for att in self.df_data if att!="class"]
         print(data_list)
         plt.boxplot(data_list,meanline=True,vert=False)
         plt.legend()
         plt.show()

    def attribute_min(self):
        print(self.dataset.attribute(0).lower_numeric_bound)


    def get_instance_list(self,index):
        return  str(self.dataset.get_instance(index)).split(",")

    def get_instances(self):
        instances = {}
        for i in range(0,self.dataset.num_instances):
            instances[i]=self.get_instance_list(i)
        return instances

    def dataset_labelized(self):
        list = self.get_attributes()
        if "class" in list:
            return True
        else:
            return False

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

    def normalize_data(self):
        print("Data normalize")