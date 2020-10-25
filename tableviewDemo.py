from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys,math


class tabelviewDemo(QWidget):
    def __init__(self):
        super(tabelviewDemo, self).__init__()
        self.InitUI()
        self.setWindowTitle('创建二维表Demo')
        self.resize(500,500)


    def InitUI(self):
        self.tabel=QTableView()
        self.model=QStandardItemModel(4,3,self)
        self.model.setHorizontalHeaderLabels(['ID','姓名','年龄'])
        self.tabel.setModel(self.model)
        layout=QVBoxLayout()
        layout.addWidget(self.tabel)
        self.setLayout(layout)

        self.model.setItem(0,0,QStandardItem('1'))
        self.model.setItem(0, 1, QStandardItem('aotem'))
        self.model.setItem(0, 2, QStandardItem('100000'))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = tabelviewDemo()
    main.show()
    sys.exit(app.exec_())
