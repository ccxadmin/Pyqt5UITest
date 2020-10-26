from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys,math
'''
MultiWindows
Qmidarea
多文档窗口
'''

class MultiWindowsDemo(QMainWindow):
    count=0
    def __init__(self):
        super(MultiWindowsDemo, self).__init__()
        self.InitUI()
        self.setWindowTitle('多文档窗口demo')
        self.resize(600,600)


    def InitUI(self):
         self.mid=QMdiArea()
         self.setCentralWidget(self.mid)
         bar=self.menuBar()
         menu= bar.addMenu('file')
         menu.addAction('new')
         menu.addAction('cascade')
         menu.addAction('Tiled')
         menu.triggered.connect(self.menuclick)



    def menuclick(self,action):
        if action.text()=='new':
           MultiWindowsDemo.count=MultiWindowsDemo.count+1
           sub=QMdiSubWindow()
           sub.setWidget(QTextEdit())
           sub.setWindowTitle('子窗口%d'% MultiWindowsDemo.count)
           self.mid.addSubWindow(sub)
           sub.show()
        elif action.text()=='cascade':
            #窗口层叠
            self.mid.cascadeSubWindows()
        elif action.text()=='Tiled':
            #窗口平铺
            self.mid.tileSubWindows()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MultiWindowsDemo()
    main.show()
    sys.exit(app.exec_())
