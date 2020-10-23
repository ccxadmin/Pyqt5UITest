from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

'''
Qcolordialog
颜色对话框
'''
class ColorDialogDemo(QWidget):
    def __init__(self):
        super(ColorDialogDemo,self).__init__()
        self.InitUI()

    def InitUI(self):
            self.setWindowTitle('颜色选择对话框')
            layout = QVBoxLayout()
            self.colorbutton = QPushButton('颜色选择')
            self.colorbutton.clicked.connect(self.getcolor)
            layout.addWidget(self.colorbutton)
            self.colorbutton2 = QPushButton('背景颜色选择')
            self.colorbutton2.clicked.connect(self.getbagcolor)
            layout.addWidget(self.colorbutton2)

            self.showlabel = QLabel('hello,颜色显示测试')
            layout.addWidget(self.showlabel)

            self.setLayout(layout)

    def getcolor(self):
        try:
            color = QColorDialog.getColor()
            pa=QPalette()
            pa.setColor(QPalette.WindowText,color)
            self.showlabel.setPalette(pa)
        except BaseException :
            print(BaseException.args)

    def getbagcolor(self):

            color = QColorDialog.getColor()
            pa=QPalette()
            pa.setColor(QPalette.Window,color)
            self.showlabel.setAutoFillBackground(True)
            self.showlabel.setPalette(pa)


if __name__ == "__main__":
        app = QApplication(sys.argv)
        main = ColorDialogDemo()
        main.show()
        sys.exit(app.exec_())