from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

'''
Qfontdialog
字体对话框
'''
class FontDialogDemo(QWidget):
    def __init__(self):
        super(FontDialogDemo,self).__init__()
        self.InitUI()

    def InitUI(self):
        self.setWindowTitle('字体选择对话框')
        layout=QVBoxLayout()
        self.fontbutton=QPushButton('字体选择')
        self.fontbutton.clicked.connect(self.getFont)
        layout.addWidget(self.fontbutton)


        self.showlabel =QLabel('hello,字体显示测试')
        layout.addWidget(self.showlabel)

        self.setLayout(layout)

    def getFont(self):
        font,ok= QFontDialog.getFont()
        if ok:
            self.showlabel.setFont(font)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = FontDialogDemo()
    main.show()
    sys.exit(app.exec_())