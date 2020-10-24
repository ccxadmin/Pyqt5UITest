from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys,math


class StatusBarDemo(QMainWindow):
    def __init__(self):
        super(StatusBarDemo, self).__init__()
        self.InitUI()
        self.setWindowTitle('创建状态栏DEMO')
        self.resize(500,500)


    def InitUI(self):
        bar=self.menuBar()
        file=bar.addMenu('file')
        file.addAction('showmenu')
        file.triggered.connect(self.barpress)
        self.setCentralWidget(QTextEdit())
        # self.status=QStatusBar()
        # self.setStatusBar(self.status)
        self.status=self.statusBar()

    def  barpress(self,action):
        text=action.text()
        if action.text().strip()=='showmenu':
            self.status.showMessage(action.text(),5000)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = StatusBarDemo()
    main.show()
    sys.exit(app.exec_())
