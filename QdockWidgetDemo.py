from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys,math
'''
Qdockwidget
停靠控件
'''

class DockWidgetDemo(QMainWindow):
    def __init__(self):
        super(DockWidgetDemo, self).__init__()
        self.InitUI()
        self.setWindowTitle('T停靠控件的使用demo')
        self.resize(300,300)


    def InitUI(self):
        items=QDockWidget(self)
        listwidget=QListWidget(self)
        listwidget.addItem('item1')
        listwidget.addItem('item2')
        listwidget.addItem('item3')
        items.setWidget(listwidget)
        #初始化为悬浮状态
        items.setFloating(True)
        self.setCentralWidget(QTextEdit())
        self.addDockWidget(Qt.LeftDockWidgetArea,items)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = DockWidgetDemo()
    main.show()
    sys.exit(app.exec_())
