from PyQt5.QtWidgets import QWidget, \
    QVBoxLayout, QHBoxLayout, QPushButton, QComboBox, QMessageBox, QLabel, QLineEdit, QPlainTextEdit, QFileDialog
from classification_algorithms.knn_algorithm import run_knn

class Classification_interface(QWidget):
    def __init__(self):
        super(Classification_interface,self).__init__()
        self.hlayout = QHBoxLayout(self)
        self.vlayout1 = QVBoxLayout(self)
        self.vlayout2 = QVBoxLayout(self)
        self.ds_path = None
        #first vertical layout contains parameters and launch button
        self.param_layout = QVBoxLayout(self)

        self.split_layout = QHBoxLayout(self)
        #label
        self.split_label = QLabel("split parameter training/test")
        self.split_layout.addWidget(self.split_label)
        #line edit
        self.split_edit = QLineEdit()
        self.split_layout.addWidget(self.split_edit)

        self.k_layout = QHBoxLayout(self)
        #label
        self.k_label = QLabel("Set the number of neighbors")
        self.k_layout.addWidget(self.k_label)
        #line edit
        self.k_edit = QLineEdit()
        self.k_layout.addWidget(self.k_edit)

        self.param_layout.addLayout(self.split_layout)
        self.param_layout.addLayout(self.k_layout)

        self.buttons_layout = QHBoxLayout()
        #load button
        self.load_button = QPushButton("Load dataset")
        self.load_button.clicked.connect(self.handle_ds_load)
        self.buttons_layout.addWidget(self.load_button)
        #launch knn button
        self.launch_knn = QPushButton("Launch KNN classification")
        self.launch_knn.clicked.connect(self.handle_knn)
        self.buttons_layout.addWidget(self.launch_knn)

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


    def handle_ds_load(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                  "All Files (*);;Python Files (*.py)", options=options)
        self.ds_path = fileName

    def handle_knn(self):
        if self.ds_path == None :
            message_content = "Make sure to load your dataset first"
            buttonReply = QMessageBox.information(self, 'Attribute details', message_content, QMessageBox.Cancel)
        else :
            split_param = self.split_edit.text()
            k_neighbors = self.k_edit.text()

            if split_param == "" or k_neighbors == "":
                message_content = "Fill both split and k neighbors with a number"
                buttonReply = QMessageBox.information(self, 'Attribute details', message_content, QMessageBox.Cancel)
            else:
                split_param = int(split_param)
                k_neighbors = int(k_neighbors)
                accuracy = run_knn(self.ds_path, split_param, k_neighbors)

