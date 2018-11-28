from PyQt5.QtWidgets import QWidget,\
    QVBoxLayout,QHBoxLayout,QPushButton,QComboBox, QMessageBox, QLabel, QLineEdit, QPlainTextEdit
import utils

class Apriori_Interface(QWidget):
    def __init__(self,prepared_ds):
        super(Apriori_Interface, self).__init__()
        self.hlayout = QHBoxLayout(self)
        self.vlayout1 = QVBoxLayout(self)
        self.vlayout2 = QVBoxLayout(self)
        self.dataset = prepared_ds

        #1st Vertical layout contains support and confidence settings
        self.support_layout = QHBoxLayout(self)
        self.confidence_layout = QHBoxLayout(self)
        values = utils.get_box_numerical_values()

        #Support items
        self.support_label = QLabel("Select the support percentage %")
        self.support_layout.addWidget(self.support_label)

        self.support_box = QComboBox()
        self.support_box.addItems(values)
        self.support_layout.addWidget(self.support_box)

        self.support_edit = QLineEdit()
        self.support_layout.addWidget(self.support_edit)

        #Confidence items
        self.confidence_label = QLabel("Select the confidence percentage %")
        self.confidence_layout.addWidget(self.confidence_label)

        self.confidence_box = QComboBox()
        self.confidence_box.addItems(values)
        self.confidence_layout.addWidget(self.confidence_box)

        self.confidence_edit = QLineEdit()
        self.confidence_layout.addWidget(self.confidence_edit)

        self.support_confidence_layout = QVBoxLayout()
        self.support_confidence_layout.addLayout(self.support_layout)
        self.support_confidence_layout.addLayout(self.confidence_layout)

        self.launch_button = QPushButton("Launch Apriori Algorithm")
        self.launch_button.clicked.connect(self.launch_apriori)

        self.vlayout1.addLayout(self.support_confidence_layout)
        self.vlayout1.addLayout(self.launch_button)

        #2nd vertical layout contains 2 text areas to represent the results of the algorithm
        self.itemset_layout = QVBoxLayout()
        self.rules_layout = QVBoxLayout()

        #Itemset layout
        self.itemset_label = QLabel("List of Itemsets")
        self.itemset_layout.addWidget(self.itemset_label)

        self.itemset_area = QPlainTextEdit()
        self.itemset_layout.addWidget(self.itemset_area)

        #rules_layout
        self.rules_label = QLabel("List of Rules")
        self.rules_layout.addWidget(self.rules_label)

        self.rules_area = QPlainTextEdit()
        self.rules_layout.addWidget(self.rules_area)

        self.vlayout2.addLayout(self.itemset_layout)
        self.vlayout2.addLayout(self.rules_layout)

        self.hlayout.addLayout(self.vlayout1)
        self.hlayout.addLayout(self.vlayout2)


    def launch_apriori(self):
        pass

