from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys,math
'''

'''

class treeWidgetDemo(QMainWindow):
    def __init__(self):
        super(treeWidgetDemo, self).__init__()
        self.InitUI()
        self.setWindowTitle('树控件的基本用法Demo')
        self.resize(600,800)


    def InitUI(self):
        self.tree=QTreeWidget()
        #为树控件指定列数
        self.tree.setColumnCount(2)
        self.tree.setHeaderLabels(['key','value'])

        #添加根节点
        self.root=QTreeWidgetItem(self.tree)
        self.root.setText(0,'根节点1')
        self.root.setIcon(0,QIcon('save.png'),)
        self.tree.setColumnWidth(0,200)

       #添加子节点
        self.child1=QTreeWidgetItem(self.root)
        self.child1.setIcon(0,QIcon('new.png'))
        self.child1.setText(0,'子节点')
        self.child1.setText(1,'子节点的值')
       #为子节点添加复选框
        self.child1.setCheckState(0,Qt.Unchecked)

        # 添加子节点
        self.child2 = QTreeWidgetItem(self.root)
        self.child2.setIcon(0, QIcon('delete.png'))
        self.child2.setText(0, '子节点2')

        # 添加二级子节点
        self.child11 = QTreeWidgetItem(self.child1)
        self.child11.setIcon(0, QIcon('delete.png'))
        self.child11.setText(0, '二级子节点')

        self.tree.expandAll()


        #为树节点添加响应事件



        self.setCentralWidget(self.tree)





if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = treeWidgetDemo()
    main.show()
    sys.exit(app.exec_())
