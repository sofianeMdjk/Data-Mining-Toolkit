
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
        self.vlayout1.addWidget(self.instances_table)

        #Vertical layout 2

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

        self.attributes_box = QComboBox()
        attributes = self.weka_instance.get_attributes()
        attributes.remove("class")
        self.attributes_box.addItems(attributes)
        self.attributes_box.currentIndexChanged.connect(self.attribute_clicked)
        self.vlayout2.addWidget(self.attributes_box)

        self.missing_values_button = QPushButton("Replace Missing values")
        self.missing_values_button.clicked.connect(self.replace_missing_values)
        self.vlayout2.addWidget(self.missing_values_button)

        self.hist_button = QPushButton("Draw histogram")
        self.hist_button.clicked.connect(self.hist_plot)
        self.vlayout2.addWidget(self.hist_button)

        self.box_button = QPushButton("Draw box plot")
        self.box_button.clicked.connect(self.box_plot)
        self.vlayout2.addWidget(self.box_button)

        #Horizental layout

        self.hlayout.addLayout(self.vlayout1)
        self.hlayout.addLayout(self.vlayout2)

        self.setLayout(self.hlayout)

        self.fill_table(self.weka_instance.get_instances())

    def update_table(self):
        self.instances_table.setRowCount(0);
        self.instances_table.setRowCount(self.dataset.num_instances)
        i=0
        for key in list(self.weka_instance.df.head(0)):
            j=0
            for item in self.weka_instance.df[key]:
                self.instances_table.setItem(j, i, QTableWidgetItem(str(item)))
                j+=1
            i+=1

    def fill_table(self,instances):
        i=0
        for key in instances.keys():
            j=0
            for item in instances[key]:
               self.instances_table.setItem(i,j,QTableWidgetItem(item))
               j+=1
            i+=1

    def attribute_clicked(self,attribute_id):
        if not self.weka_instance.is_nominal(self.weka_instance.get_attributes()[attribute_id]):
            min = str(self.weka_instance.attribute_min(attribute_id))
            max = str(self.weka_instance.attribute_max(attribute_id))
            median = str(self.weka_instance.attribute_median(attribute_id))
            mean = str(self.weka_instance.attribute_mean(attribute_id))
            q3 = str(self.weka_instance.attribute_q3(attribute_id))
            mode = str(self.weka_instance.attribute_mode(attribute_id))
            message_content = "Minimum value is : "+min+"\nMaximum value is : "+max+"\nMedian is : "\
                              +median+"\nMean value is : "+mean+"\nQ3 Value is : "+q3+"\nMode is : "+mode
            buttonReply = QMessageBox.information(self, 'Attribute details', message_content, QMessageBox.Cancel)
        else :
            mode = str(self.weka_instance.attribute_mode(attribute_id))
            message_content = "Mode is : "+mode+"\nPick a numerical attribite for more statistical details"
            buttonReply = QMessageBox.information(self, 'Attribute details', message_content, QMessageBox.Cancel)

    def hist_plot(self):
        self.weka_instance.hist_plot()

    def box_plot(self):
        self.weka_instance.box_plot()

    def replace_missing_values(self):
        self.weka_instance.fill_missing_values()
        self.update_table()


