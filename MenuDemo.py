from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys,math


class MenuDemo(QMainWindow):
    def __init__(self):
        super(MenuDemo, self).__init__()
        self.InitUI()

    def InitUI(self):
        bar=QMenuBar(self)
        addmenu= bar.addMenu("文件")
        action=QAction('新建',self)
        addmenu.addAction(action)
        action2=QAction('保存',self)
        action2.setShortcut('CTRL+s')
        action2.triggered.connect(self.saveclick)
        addmenu.addAction(action2)

        addmenu2=bar.addMenu('编辑')
        addmenu2.addAction('复制')
        addmenu2.addSeparator()
        acction3=QAction('粘贴',self)
        addmenu2.addAction(acction3)


    def saveclick(self,a):
        print(a)
        print(self.sender().text())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MenuDemo()
    main.show()
    sys.exit(app.exec_())
