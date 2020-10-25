from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys,math


class TableWidgetDemo(QWidget):
    def __init__(self):
        super(TableWidgetDemo, self).__init__()
        self.InitUI()
        self.setWindowTitle('创建TableWidget二维表Demo')
        self.resize(500,500)


    def InitUI(self):
        self.tabelwdiget=QTableWidget()
        self.tabelwdiget.setRowCount(4)
        self.tabelwdiget.setColumnCount(3)
        self.tabelwdiget.setHorizontalHeaderLabels(['姓名','年龄','籍贯'])
        self.tabelwdiget.setItem(0,0,QTableWidgetItem('小米'))
        self.tabelwdiget.setItem(0, 1, QTableWidgetItem('18'))
        self.tabelwdiget.setItem(0, 2, QTableWidgetItem('湖北武汉'))
        self.tabelwdiget.setEditTriggers(QAbstractItemView.NoEditTriggers)#常量
        self.tabelwdiget.setSelectionBehavior(QAbstractItemView.SelectRows)


        # self.tabelwdiget.resizeColumnsToContents()
        # self.tabelwdiget.resizeRowsToContents()
        # self.tabelwdiget.setShowGrid(False)

        layout=QVBoxLayout()
        layout.addWidget(self.tabelwdiget)
        self.setLayout(layout)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = TableWidgetDemo()
    main.show()
    sys.exit(app.exec_())
