from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys,math
'''
Qtabwidget
tableControl选项卡控件
'''

class tabdgetDemo(QWidget):
    def __init__(self):
        super(tabdgetDemo, self).__init__()
        self.InitUI()
        self.setWindowTitle('TableControl控件的使用demo')
        self.resize(800,600)


    def InitUI(self):

        self.tabcontrol=QTabWidget()
        self.tabcontrol.setTabText(0,'TAb演示')

        self.tab1=QWidget()
        self.tab2=QWidget()
        self.tab3=QWidget()
        self.tabcontrol.addTab(self.tab1,'tab1')
        self.tabcontrol.addTab(self.tab2, 'tab2')
        self.tabcontrol.addTab(self.tab3, 'tab3')
        box=QVBoxLayout(self)
        box.addWidget(self.tabcontrol)
        self.setLayout(box)
        self.tabUI1()
        self.tabUI2()
        self.tabUI3()
        self.tabcontrol.setTabText(0,'联系方式')

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
        layout=QVBoxLayout()
        layout.addWidget(QLabel('科目'))
        layout.addWidget(QCheckBox('物理'))
        layout.addWidget(QCheckBox('化学'))

        self.tab3.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = tabdgetDemo()
    main.show()
    sys.exit(app.exec_())
