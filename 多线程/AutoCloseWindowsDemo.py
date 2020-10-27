from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys,math
'''
Qtimer
'''

if __name__ == "__main__":
    app = QApplication(sys.argv)
    label=QLabel('<font color=red size=140><b>准备关闭窗口</b></font>')
    label.setWindowFlags(Qt.SplashScreen|Qt.FramelessWindowHint)
    label.show()
    QTimer.singleShot(5000,app.quit)

    sys.exit(app.exec_())
