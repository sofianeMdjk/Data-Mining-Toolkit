from PyQt5.QtWidgets import QWidget, \
    QVBoxLayout, QHBoxLayout, QPushButton, QComboBox, QMessageBox, QLabel, QLineEdit, QPlainTextEdit, QFileDialog
from classification_algorithms.dbscan_algorithm import run_dbscan
from utils import *

class Dbscan_interface(QWidget):
    def __init__(self):
        super(Dbscan_interface,self).__init__()
        self.hlayout = QHBoxLayout(self)
        self.vlayout1 = QVBoxLayout(self)
        self.vlayout2 = QVBoxLayout(self)
        self.ds_path = "tmp/temp.csv"
        #first vertical layout contains parameters and launch button
        self.param_layout = QVBoxLayout(self)

        self.eps_layout = QHBoxLayout(self)
        #label
        self.eps_label = QLabel("EPS Parameter")
        self.eps_layout.addWidget(self.eps_label)
        #line edit
        self.eps_edit = QLineEdit()
        self.eps_layout.addWidget(self.eps_edit)

        self.k_layout = QHBoxLayout(self)
        #label
        self.k_label = QLabel("Set the min number of points in cluster")
        self.k_layout.addWidget(self.k_label)
        #line edit
        self.k_edit = QLineEdit()
        self.k_layout.addWidget(self.k_edit)

        self.param_layout.addLayout(self.eps_layout)
        self.param_layout.addLayout(self.k_layout)

        self.buttons_layout = QHBoxLayout()
        #launch knn button
        self.launch_dbscan = QPushButton("Launch DBScan classification")
        self.launch_dbscan.clicked.connect(self.handle_DBSCAN)
        self.buttons_layout.addWidget(self.launch_dbscan)

        self.vlayout1.addLayout(self.param_layout)
        self.vlayout1.addLayout(self.buttons_layout)

        #KNN results
        self.results_layout = QVBoxLayout(self)
        #label
        self.result_label = QLabel("Results for KNN classification ")
        self.results_layout.addWidget(self.result_label)
        #text area
        self.algo_results = QPlainTextEdit()
        self.algo_results.setReadOnly(True)
        self.results_layout.addWidget(self.algo_results)

        self.vlayout2.addLayout(self.results_layout)

        self.hlayout.addLayout(self.vlayout1)
        self.hlayout.addLayout(self.vlayout2)


    def handle_DBSCAN(self):
        eps_param = self.eps_edit.text()
        min_points = self.k_edit.text()
        if eps_param == "" or min_points == "":
            message_content = "Fill both eps and k neighbors with a number"
            buttonReply = QMessageBox.information(self, 'Attribute details', message_content, QMessageBox.Cancel)
        else:
            eps_param = float(eps_param)
            min_points = float(min_points)
            db_scan_results = run_dbscan(self.ds_path, eps_param, min_points)
            num_clusters = distinct_postive_elements_of_list(db_scan_results)

            toprint ="Number of clusters is : \n"+str(num_clusters)+"\n\npoints id clustering is : \n"
            self.algo_results.insertPlainText(toprint)
            for elt in db_scan_results :
                self.algo_results.insertPlainText(str(elt)+"\n")

