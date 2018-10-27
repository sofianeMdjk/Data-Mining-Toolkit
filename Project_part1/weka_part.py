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
        self.df = pd.DataFrame(raw_data[0])
        self.decode_data()
        self.df = self.df.replace('?',np.nan)
        #gp = self.df[self.df["class"] ==b"'goo'"] d
        self.fill_missing_values()
        #print(self.df[self.df["class"].isnull()])


    def save_dataset(self,filepath):
        saver = Saver(classname="weka.core.converters.CSVSaver")
        saver.save_file(self.dataset, filepath)

    def hist_plot(self):
          for att in self.df :
            if att != "class":
                plt.hist(self.df[att], bins= 20, rwidth=0.50, label=att)
          plt.legend()
          plt.show()

    def box_plot(self):
         data_list = [self.df[att] for att in self.df if att!="class"]
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

    def get_attribute_type(self, attribute):

        val = type(self.df[attribute][0])
        print(val)

    def get_attribute_values(self, attribute_id):
        values = []
        return

    def select_missing_values(self,attribute_id):
        values = self.get_attribute_values(attribute_id)
        missing_values_indexes = []
        for i,elt in enumerate(values) :
            if elt == "?":
                missing_values_indexes.append(i)

        return missing_values_indexes

    def attribute_min(self, attribute_id):
        return np.min(self.get_attribute_values(attribute_id))

    def attribute_max(self, attribute_id):
        return np.max(self.get_attribute_values(attribute_id))

    def attribute_median(self, attribute_id):
        return np.median(self.get_attribute_values(attribute_id))

    def attribute_q3(self, attribute_id):
        return np.quantile(self.get_attribute_values(attribute_id),0.5)

    def attribute_mode(self, attribute_id):
        pass

    def attribute_mean(self, attribute_id):
        return np.mean(self.get_attribute_values(attribute_id))

    def decode_data(self):
        attributes = self.get_attributes()
        for att in attributes :
            if self.df[att].dtypes == "object":
                self.df[att] = self.df[att].str.decode("utf-8")



    def normalize_data(self):
        print("Data normalize")

    def is_nominal(self,attribite):
        if self.df[attribite].dtypes == "object" :
            return True

    def contains_missing_valeus(self,attribute):
        if not self.df[attribute].isnull().empty:
            #print(attribute+"-------------------------------------y")
            #print(self.df[self.df[atribute].isnull()])
            return True
        else:
            return False



    def fill_missing_values(self):
        attributes = self.get_attributes()
        for att in attributes :
            if self.contains_missing_valeus(att) is True:
                if self.is_nominal(att):
                    mode_value = self.df[att].mode()[0]
                    self.df[att] = self.df[att].fillna(value=str(mode_value))
                else :
                    avg_value = self.df[att].mean()
                    self.df[att] = self.df[att].fillna(value=avg_value)

