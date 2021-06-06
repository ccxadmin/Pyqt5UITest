'''
使用web浏览器控件(QWebEngineView 显示网页)
pyqt5 与web技术的交互
同时使用python与WEb开发程序，混合开发
python+javascript+html5+css
QwebEngineView
'''

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
import sys


class WebEnginView(QMainWindow):
    def __init__(self):
        super(WebEnginView,self).__init__()
        self.setWindowTitle("打开外部网页例子")
        self.setGeometry(5,30,1355,730)
        self.brower=QWebEngineView()
        self.brower.load(QUrl("https://wwww.baidu.com"))
        self.setCentralWidget(self.brower)

if __name__ == '__main__':
    app=QApplication(sys.argv)
    win=WebEnginView()
    win.show()
    sys.exit(app.exec_())


