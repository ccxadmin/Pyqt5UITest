from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys,math
'''
stackwidgetControl
堆栈窗口控件
'''

class stackedWidgetDemo(QWidget):
    def __init__(self):
        super(stackedWidgetDemo, self).__init__()
        self.InitUI()
        self.setWindowTitle('TableControl控件的使用demo')
        self.resize(300,200)


    def InitUI(self):
        layout=QHBoxLayout(self)

        self.listwidget=QListWidget()
        self.listwidget.itemClicked.connect(self.itemclick)
        self.listwidget.currentItemChanged.connect(self.itemchange)
        self.listwidget.addItem(QListWidgetItem('个人信息'))
        self.listwidget.addItem('体重信息')
        self.listwidget.addItem('身份信息')
        layout.addWidget(self.listwidget)

        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tabUI1()
        self.tabUI2()
        self.tabUI3()
        self.stack=QStackedWidget()
        self.stack.addWidget(self.tab1)
        self.stack.addWidget(self.tab2)
        self.stack.addWidget(self.tab3)

        layout.addWidget(self.stack)

        self.setLayout(layout)

    def tabUI1(self):
        layout=QFormLayout(self)
        layout.addRow('姓名：',QLineEdit())
        layout.addRow('性别：',QLineEdit())
        self.tab1.setLayout(layout)


    def tabUI2(self):
        layout1=QHBoxLayout(self)
        layout1.addWidget(QRadioButton('btn1'),0)
        layout1.addWidget(QRadioButton('btn2'),1)
        layout2=QVBoxLayout()
        layout2.addLayout(layout1)
        layout2.addWidget(QLineEdit())

        self.tab2.setLayout(layout2)

    def tabUI3(self):
        layout3=QVBoxLayout()
        layout3.addWidget(QLabel('科目'))
        layout3.addWidget(QCheckBox('物理'))
        layout3.addWidget(QCheckBox('化学'))

        self.tab3.setLayout(layout3)
    def itemclick(self ,item):
        print('meth1:'+item.text())

        index = self.listwidget.indexFromItem(item).row()
        print(index)
        if self.stack.count()>index:
          self.stack.setCurrentIndex(index)

    def itemchange(self, item):
        print('meth2:'+item.text())
        index= self.listwidget.indexFromItem(item).row()
        print(index)
        if self.stack.count() > index:
          self.stack.setCurrentIndex(index)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = stackedWidgetDemo()
    main.show()
    sys.exit(app.exec_())
