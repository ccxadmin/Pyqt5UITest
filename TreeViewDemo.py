from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys,math
'''
Qtreeview
数据装载模式为model，
QDirmodel 
'''

class treeviewDemo(QWidget):
    def __init__(self):
        super(treeviewDemo, self).__init__()
        self.InitUI()
        self.setWindowTitle('树控件的基本用法Demo2')
        self.resize(600,800)


    def InitUI(self):
        self.model=QDirModel()
        self.tree=QTreeView()
        self.tree.setModel(self.model)
        box=QVBoxLayout(self)
        box.addWidget(self.tree)
        self.setLayout(box)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = treeviewDemo()
    main.show()
    sys.exit(app.exec_())
