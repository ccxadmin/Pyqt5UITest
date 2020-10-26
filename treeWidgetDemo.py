from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys,math
'''
Qtreewidget
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
        self.tree.clicked.connect(self.treeclikEvent)


       #动态添加，修改，删除树控件中的节点
        # 在树控件中的节点显示上下文菜单，单击右键可显示
        self.tree.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tree.customContextMenuRequested.connect(self.Ontreeclick)

        self.setCentralWidget(self.tree)


    def  treeclikEvent(self,index):
        item=self.tree.currentItem()
        print(item.text(0))
        print(str(index.row())+','+str(index.column()))

    def Ontreeclick(self,pos):
        screenpos=self.mapToGlobal(pos)
        print(screenpos)
        newmenu=QMenu(self)
        item1= newmenu.addAction('添加节点')
        item2=newmenu.addAction('删除节点')
        item3=newmenu.addAction('修改节点')
        actionx=newmenu.exec(screenpos)
        if actionx==item1:
            print('准备添加节点:')
            item=self.tree.currentItem()
            print(item)
            newsunitem=QTreeWidgetItem(item)
            newsunitem.setText(0,'newkey')
            newsunitem.setText(1,'newvalue')

        elif actionx==item2:
            print('准备删除节点')
            item = self.tree.currentItem()
            root=self.tree.invisibleRootItem()
            print(item)
            for s in  self.tree.selectedItems():
                (item.parent() or root).removeChild(s)



        elif actionx == item3:
            print('准备修改节点')
            item = self.tree.currentItem()
            print(item)
            item.setText(0, '修改节点')
            item.setText(1, '修改节点值')



if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = treeWidgetDemo()
    main.show()
    sys.exit(app.exec_())
