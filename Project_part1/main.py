import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog, QComboBox, QAction, qApp, QHBoxLayout, \
    QVBoxLayout
from weka_part import weka_handler
from Instances_table import Instances_table


class Interface(QMainWindow):

    def __init__(self):
        super().__init__()
        self.init_interface()


    def init_interface(self):
        #main interface
        self.setGeometry(500, 175, 800, 800)
        self.setWindowTitle("My Weka")


        #Menubar
        #file actions
        load_ds_action = QAction("Load dataset", self)
        load_ds_action.setShortcut('Ctrl+l')
        load_ds_action.triggered.connect(self.handle_load_dataset)
        save_ds_action= QAction("Save dataset informations",self)
        save_ds_action.setShortcut('Ctrl+s')
        save_ds_action.triggered.connect(self.handle_load_dataset)
        exit_action = QAction('Exit',self)
        exit_action.triggered.connect(qApp.quit)


        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('&File')
        fileMenu.addAction(load_ds_action)
        fileMenu.addAction(save_ds_action)
        fileMenu.addAction(exit_action)

        self.show()


    def handle_load_dataset(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                  "All Files (*);;Python Files (*.py)", options=options)
        file_path=fileName
        #Here's the part where you just call the load funciton
        self.weka = weka_handler()
        self.weka.load_dataset(file_path)
        self.table_load()
        #Instances_table(self)

    def table_load(self):
        self.table_widget = Instances_table(self.weka)
        self.setCentralWidget (self.table_widget)
        self.table_widget.fill_table(self.weka.get_instances())

    def handle_ds_save(self):
        self.weka.save_dataset("iris.csv")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Interface()
    sys.exit(app.exec_())
