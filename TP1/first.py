import weka.core.jvm as jvm

from weka.core.converters import Loader
from weka.core.dataset import Instances
from weka.core.dataset import Instance
from weka.core.dataset import Attribute


jvm.start()
loader = Loader("weka.core.converters.ArffLoader")
dataset = loader.load_file("/Users/slash/weka-3-8-3/data/iris.arff")
print(dataset)
