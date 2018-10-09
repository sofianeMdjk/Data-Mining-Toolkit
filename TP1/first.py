import weka.core.jvm as jvm
from weka.core.converters import Loader


jvm.start()
l = Loader("weka.core.converters.ArffLoader")
d = l.load_file("/Users/slash/weka-3-8-3/data/iris.arff")
print(d)
print(d.summary(d))
print("Dataset summary")
print("\t \t name   type")

for i in range(d.num_attributes):
	print(d.attribute(i))
print("the number of attributes :"+str(d.num_attributes))
print("the number of instances :"+str(d.num_instances))
