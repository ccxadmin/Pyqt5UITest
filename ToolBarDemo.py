from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys,math


class ToolBarDemo(QMainWindow):
    def __init__(self):
        super(ToolBarDemo, self).__init__()
        self.InitUI()
        self.setWindowTitle('创建工具栏DEMO')
        self.resize(500,500)


    def InitUI(self):
        # bar=QToolBar('file',self)
        bar= self.addToolBar('file')
        new =QAction(QIcon('new.png'),'new',self)
        bar.addAction(new)
        new2 = QAction(QIcon('save.png'), 'add', self)
        bar.addAction(new2)
        # bar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        bar2=self.addToolBar('硬件')
        bar2.addAction(QIcon('resizeApi.png'),'CCD')

        bar.actionTriggered.connect(self.press)

    def press(self,action):
        print(self.sender())
        print(action.text())



if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = ToolBarDemo()
    main.show()
    sys.exit(app.exec_())
