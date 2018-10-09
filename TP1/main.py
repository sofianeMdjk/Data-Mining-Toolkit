import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFileDialog, QTableWidget,QTableWidgetItem
import weka_part


class Interface(QWidget):

    def __init__(self):
        super().__init__()
        self.init_interface()

    def init_interface(self):
        #main interface
        self.setGeometry(500, 175, 800, 600)

        #Data_set_path
        load_btn = QPushButton('Read dataset', self)
        load_btn.resize(200,100)
        load_btn.move(50, 250)
        load_btn.clicked.connect(self.handle_load_btn)

        #Display dataset informations
        display_btn = QPushButton('Display dataset attributes', self)
        display_btn.resize(200,100)
        display_btn.move(300, 250)
        display_btn.clicked.connect(self.handle_att_display)

        #display benchmarks
        benchmark_btn = QPushButton("Display Benchmarks",self)
        benchmark_btn.resize(200, 100)
        benchmark_btn.move(550, 250)
        benchmark_btn.clicked.connect(self.handle_bench_display)


        self.show()


    def handle_load_btn(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                  "All Files (*);;Python Files (*.py)", options=options)
        self.file_path=fileName
        #Here's the part where you just call the load funciton
        weka_part.load_dataset(self.file_path)

    def handle_att_display(self):
        weka_part.att_display()

    def handle_bench_display(self):
        weka_part.display_benchmarks()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    ex = Interface()

    sys.exit(app.exec_())
