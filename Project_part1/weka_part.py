import weka.core.jvm as jvm
from weka.core.converters import Loader, Saver
import matplotlib.pyplot as plt
import pandas as pd
from scipy.io.arff import loadarff
import numpy as np
from scipy import stats
from sklearn import preprocessing
from utils import unique

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

    def save_dataset(self,filepath):
        saver = Saver(classname="weka.core.converters.CSVSaver")
        saver.save_file(self.dataset, filepath)

    def hist_plot(self):
          for att in self.df :
              if not self.is_nominal(att):
                plt.hist(self.df[att], bins= 20, rwidth=0.50, label=att)
          plt.legend()
          plt.show()

    def box_plot(self):
         data_list = [self.df[att] for att in self.df if not self.is_nominal(att)]
         plt.boxplot(data_list,meanline=True,vert=False)
         plt.legend()
         plt.show()

    def get_instance_list(self,index):
        return str(self.dataset.get_instance(index)).split(",")

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

    def get_classes(self):
        if self.dataset_labelized():
            return unique(self.df['class'])
        else :
            return []

    def get_attributes(self):
        attributes = []
        for i in range(self.dataset.num_attributes):
            attributes.append(self.dataset.attribute(i).name)
        return attributes

    def get_attribute_values(self, attribite_id):
        return self.df[self.get_attributes()[attribite_id]]

    def attribute_min(self, attribute_id):
        return np.min(self.get_attribute_values(attribute_id))

    def attribute_max(self, attribute_id):
        return np.max(self.get_attribute_values(attribute_id))

    def attribute_median(self, attribute_id):
        return np.median(self.get_attribute_values(attribute_id))

    def attribute_q3(self, attribute_id):
        return np.quantile(self.get_attribute_values(attribute_id),0.5)

    def attribute_mode(self, attribute_id):
        return stats.mode(self.get_attribute_values(attribute_id))[0][0]

    def attribute_mean(self, attribute_id):
        return np.mean(self.get_attribute_values(attribute_id))


    def normalize_dataset(self):
        attributes = self.get_attributes()
        for att in attributes :
            if not self.is_nominal(att):
                x = pd.DataFrame({att : self.df[att]})
                min_max_scalar = preprocessing.MinMaxScaler()
                scaled = min_max_scalar.fit_transform(x)
                self.df[att] = pd.DataFrame(scaled)

    def attribute_is_semetrical(self,attribute_id):
        if not self.is_nominal(self.get_attributes()[attribute_id]):
            mean,mode,median = self.attribute_mean(attribute_id), \
                               self.attribute_mode(attribute_id), self.attribute_median(attribute_id)
            if mean == mode == median:
                return True
            else :
                return False

    def attribute_is_neg_skewed(self, attribute_id):
        if not self.is_nominal(self.get_attributes()[attribute_id]):
            mean, mode, median = self.attribute_mean(attribute_id), \
                                 self.attribute_mode(attribute_id), self.attribute_median(attribute_id)

            if (median < mode) and (mode < mean):
                return True
            else :
                return False

    def attribute_is_pos_skewed(self, attribute_id):
        if not self.is_nominal(self.get_attributes()[attribute_id]):
            mean, mode, median = self.attribute_mean(attribute_id), \
                                 self.attribute_mode(attribute_id), self.attribute_median(attribute_id)

            if (median > mode) and (mode > mean):
                return True
            else :
                return False

    def decode_data(self):
        attributes = self.get_attributes()
        for att in attributes :
            if self.df[att].dtypes == "object":
                self.df[att] = self.df[att].str.decode("utf-8")

    def mean_calcul_missing(self,attribute,item_class):
        values = self.get_attribute_value_by_class(attribute,item_class)
        return np.mean(values)

    def mode_calcul_missing(self,attribute,item_class):
        values = self.get_attribute_value_by_class(attribute, item_class)
        return values.mode()[0]

    def get_attribute_value_by_class(self, att, item_class):
        temp = self.df.loc[self.df["class"] == item_class, att]
        return temp

    def is_nominal(self,attribite):
        if self.df[attribite].dtypes == "object":
            return True

    def contains_missing_valeus(self,attribute):
        if not self.df[attribute].isnull().empty:
            return True
        else:
            return False

    def fill_missing_values_class_dependant(self):
        attributes = self.get_attributes()
        classes = self.get_classes()
        for att in attributes:
            if self.contains_missing_valeus(att) is True:
                for class_item in classes:
                    if self.is_nominal(att):
                        mode_value = self.mode_calcul_missing(att,class_item)
                        self.df.loc[self.df["class"] == class_item, att] = self.df.loc[self.df["class"]== class_item,att].fillna(value=str(mode_value))
                    else :
                        avg_value = self.mean_calcul_missing(att,class_item)
                        self.df.loc[self.df["class"] == class_item,att] = self.df.loc[self.df["class"]== class_item,att].fillna(value=str(avg_value)).values.astype(float)


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
