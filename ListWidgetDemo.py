from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys,math


class ListWidgetDemo(QMainWindow):
    def __init__(self):
        super(ListWidgetDemo, self).__init__()
        self.InitUI()
        self.setWindowTitle('创建ListWidgetDemo')
        self.resize(500,500)


    def InitUI(self):
        self.listwidget=QListWidget()
        self.listwidget.addItem('item1')
        self.listwidget.addItem('item2')
        self.listwidget.addItem('item3')
        self.listwidget.setWindowTitle('demo')
        self.listwidget.itemClicked.connect(self.clickEcent)
        self.setCentralWidget(self.listwidget)


    def clickEcent(self,item):
        print(item.text())
        QMessageBox.information(self,'Infomation','你点击了：'+self.listwidget.item(self.listwidget.row(item)).text())




if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = ListWidgetDemo()
    main.show()
    sys.exit(app.exec_())
