import argparse
from itertools import chain, combinations
from utils import clean_list

class Apriori():
    def __init__(self,file_path):
        self.data = self.data_from_csv(file_path)

    def joinset(self,itemset, k):
        return set([i.union(j) for i in itemset for j in itemset if len(i.union(j)) == k])

    def subsets(self,itemset):
        return chain(*[combinations(itemset, i + 1) for i, a in enumerate(itemset)])

    def itemset_support(self,transaction_list, itemset, min_support=0):
        len_transaction_list = len(transaction_list)
        l = [
            (item, float(sum(1 for row in transaction_list if item.issubset(row))) / len_transaction_list)
            for item in itemset
        ]
        return dict([(item, support) for item, support in l if support >= min_support])

    def freq_itemset(self, transaction_list, c_itemset, min_support):
        f_itemset = dict()
        k = 1
        while True:
            if k > 1:
                c_itemset = self.joinset(l_itemset, k)
            l_itemset = self.itemset_support(transaction_list, c_itemset, min_support)
            if not l_itemset:
                break
            f_itemset.update(l_itemset)
            k += 1

        return f_itemset

    def apriori(self, min_support, min_confidence):
        # Get first itemset and transactions
        itemset, transaction_list = self.itemset_from_data()


        # Get the frequent itemset
        f_itemset = self.freq_itemset(transaction_list, itemset, min_support)

        # Association rules
        rules = list()
        for item, support in f_itemset.items():
             if len(item) > 1:
                for A in self.subsets(item):
                    B = item.difference(A)
                    if B:
                        A = frozenset(A)
                        AB = A | B
                        confidence = float(f_itemset[AB]) / f_itemset[A]
                        if confidence >= min_confidence:
                            rules.append((A, B, confidence))
        return rules, f_itemset

    def itemset_from_data(self):
        itemset = set()
        transaction_list = list()
        for row in self.data:
            transaction_list.append(frozenset(row))
            for item in row:
                if item:
                    itemset.add(frozenset([item]))
        return itemset, transaction_list

    def data_from_csv(self,filename):
        f = open(filename, 'rU')
        rows = []
        for line in f:
            row = line.split(',')
            row = clean_list(row)
            rows.append(row)
        return rows

    def apriori_results(self,min_support=0.40,min_confidence=0.6):
        rules, itemset = self.apriori(min_support, min_confidence)
        return rules,itemset



