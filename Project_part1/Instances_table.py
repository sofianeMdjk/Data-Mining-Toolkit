
from PyQt5.QtWidgets import QTableView,QWidget,QTableWidget,QTableWidgetItem,QVBoxLayout,QHBoxLayout,QPushButton,QComboBox, QMessageBox
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
        self.attributes_box.addItems(self.weka_instance.get_attributes())
        self.attributes_box.currentIndexChanged.connect(self.attribute_clicked)
        self.vlayout2.addWidget(self.attributes_box)

        self.button = QPushButton("this is a button")
        self.button.resize(140,140)
        self.vlayout2.addWidget(self.button)

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
        message_content = "Minimum value is : "+min+"\nMaximum value is : "+max+"\nMedian is : "+median
        buttonReply = QMessageBox.information(self, 'PyQt5 message', message_content, QMessageBox.Cancel)
        print(int(buttonReply))
        print("attribute changed")
        print(self.weka_instance.attribute_min(i))

    def cellClick(self):
        print("Cell click in here")

