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
        self.tabelwdiget.setColumnCount(4)
        self.tabelwdiget.setHorizontalHeaderLabels(['姓名','年龄','籍贯','显示图片'])
        item1= QTableWidgetItem('小米')
        item1.setFont(QFont('Times',14))
        item1.setForeground(QBrush(Qt.red))
        item1.setBackground(QBrush(Qt.green))
        item1.setTextAlignment(Qt.AlignCenter|Qt.AlignRight) #文本排列方式
        self.tabelwdiget.setItem(0,0,item1)

        #self.tabelwdiget.setItem(0, 0, QTableWidgetItem('小米'))
        self.tabelwdiget.setItem(0, 1, QTableWidgetItem('18'))
        self.tabelwdiget.setItem(0, 2, QTableWidgetItem('武汉'))

        self.tabelwdiget.setItem(1, 0, QTableWidgetItem('李四'))
        self.tabelwdiget.setItem(1, 1, QTableWidgetItem('19'))
        self.tabelwdiget.setItem(1, 2, QTableWidgetItem('深圳'))

        self.tabelwdiget.setItem(2, 0, QTableWidgetItem('王五'))
        self.tabelwdiget.setItem(2, 1, QTableWidgetItem('20'))
        self.tabelwdiget.setItem(2, 2, QTableWidgetItem('广州'))


        #合并单元格
        # self.tabelwdiget.setSpan(0,0,2,1)
        #显示图片
        imageitem=QTableWidgetItem(QIcon('package.png'),'背包')
        self.tabelwdiget.setItem(2,3,imageitem)

        self.tabelwdiget.setEditTriggers(QAbstractItemView.NoEditTriggers)#常量
        self.tabelwdiget.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.sortbutton=QPushButton('降序排列')
        self.sortbutton.clicked.connect(self.sortClick)

        # self.tabelwdiget.resizeColumnsToContents()
        # self.tabelwdiget.resizeRowsToContents()
        # self.tabelwdiget.setShowGrid(False)
        self.orderType=Qt.DescendingOrder
        layout=QVBoxLayout()
        layout.addWidget(self.tabelwdiget)
        layout.addWidget(self.sortbutton)
        self.setLayout(layout)

    def sortClick(self):
        if self.orderType==Qt.DescendingOrder:
            self.orderType=Qt.AscendingOrder
        else:
            self.orderType=Qt.DescendingOrder
        self.tabelwdiget.sortItems(1,self.orderType)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = TableWidgetDemo()
    main.show()
    sys.exit(app.exec_())
