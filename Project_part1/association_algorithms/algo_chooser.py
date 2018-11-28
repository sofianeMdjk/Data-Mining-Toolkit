
from association_algorithms.apriori_algo import Apriori


apriori_algorithm = Apriori("breast-cancer.arff")

rules, itemset = apriori_algorithm.apriori_results(0.23)

print("------------------------ITEMSETS----------------------------")
for item in itemset:
    print(item)

print("----------------------LIST OF RULES--------------------------")
for rule in rules:
    print(rule)

print(len(itemset))