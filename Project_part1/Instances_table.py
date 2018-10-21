
from PyQt5.QtWidgets import QTableView,QWidget,QTableWidget,QTableWidgetItem,\
    QVBoxLayout,QHBoxLayout,QPushButton,QComboBox, QMessageBox, QLabel
import matplotlib.pyplot as plt
class Instances_table(QWidget):
    def __init__(self,wk):
        super(Instances_table, self).__init__()
        self.hlayout = QHBoxLayout(self)
        self.vlayout1 = QVBoxLayout(self)
        self.vlayout2= QVBoxLayout(self)
        self.weka_instance=wk
        self.dataset=self.weka_instance.dataset

        #Vertical layout 1
        self.instances_table = QTableWidget()
        self.instances_table.setRowCount(self.dataset.num_instances)
        self.instances_table.setColumnCount(self.dataset.num_attributes)
        self.instances_table.setHorizontalHeaderLabels(self.weka_instance.get_attributes())
        self.instances_table.setSelectionBehavior(QTableView.SelectRows)
        self.instances_table.clicked.connect(self.cellClick)
        self.vlayout1.addWidget(self.instances_table)

        #Vertical layout 2
        self.attributes_box = QComboBox()
        attributes = self.weka_instance.get_attributes()
        attributes.remove("class")

        self.attributes_label = QLabel()
        text = "Number of attributes is : "
        if self.weka_instance.dataset_labelized():
            text += str(self.weka_instance.dataset.num_attributes)
        self.attributes_label.setText(text)
        self.vlayout2.addWidget(self.attributes_label)

        self.instances_label = QLabel()
        text = "Number of instances is : "+str(self.weka_instance.dataset.num_instances)
        self.instances_label.setText(text)
        self.vlayout2.addWidget(self.instances_label)

        self.attributes_box.addItems(attributes)
        self.attributes_box.currentIndexChanged.connect(self.attribute_clicked)
        self.vlayout2.addWidget(self.attributes_box)

        self.hist_button = QPushButton("Draw histogram")
        self.hist_button.clicked.connect(self.hist_plot)
        self.vlayout2.addWidget(self.hist_button)

        self.box_button = QPushButton("Draw box plot")
        self.box_button.clicked.connect(self.box_plot)
        self.vlayout2.addWidget(self.box_button)

        self.normalize_button = QPushButton("Normalize dataset")
        self.normalize_button.clicked.connect(self.normalize_data)
        self.vlayout2.addWidget(self.normalize_button)
        #Horizental layout

        self.hlayout.addLayout(self.vlayout1)
        self.hlayout.addLayout(self.vlayout2)

        self.setLayout(self.hlayout)

    def fill_table(self,instances):
        i=0
        for key in instances.keys():
            j=0
            for item in instances[key]:
               self.instances_table.setItem(i,j,QTableWidgetItem(item))
               j+=1
            i+=1

    def attribute_clicked(self,i):
        min= str(self.weka_instance.attribute_min(i))
        max=str(self.weka_instance.attribute_max(i))
        median=str(self.weka_instance.attribute_median(i))
        mean=str(self.weka_instance.attribute_mean(i))
        q3=str(self.weka_instance.attribute_q3(i))
        message_content = "Minimum value is : "+min+"\nMaximum value is : "+max+"\nMedian is : "+median+"\nMean value is : "+mean+"\nQ3 Value is : "+q3
        buttonReply = QMessageBox.information(self, 'PyQt5 message', message_content, QMessageBox.Cancel)
        print(int(buttonReply))
        print("attribute changed")
        print(self.weka_instance.attribute_min(i))

    def hist_plot(self):
        self.weka_instance.hist_plot()

    def box_plot(self):
        self.weka_instance.box_plot()

    def normalize_data(self):
        self.weka_instance.normalize_data()

    def cellClick(self):
        print("Cell click in here")

