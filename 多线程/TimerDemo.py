from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys,math
'''
Qtimer
'''

class TimerDemo(QWidget):
    def __init__(self):
        super(TimerDemo, self).__init__()
        self.InitUI()
        self.setWindowTitle('Timer计时器控件演示Demo')
        self.resize(300,200)


    def InitUI(self):
        layout=QGridLayout()
        self.label=QLabel('时间显示')
        self.timer=QTimer()
        self.startBtn=QPushButton('启动计时器')
        self.stopbtn=QPushButton('停止计时器')
        layout.addWidget(self.label,0,0,1,2)
        layout.addWidget(self.startBtn,1,0)
        layout.addWidget(self.stopbtn,1,1)
        self.setLayout(layout)

        self.timer.timeout.connect(self.timeTick)
        self.startBtn.clicked.connect(self.statrtTimer)
        self.stopbtn.clicked.connect(self.stopTimer)




    def showLabelTime(self):
        currtime=QDateTime.currentDateTime()
        self.label.setText(currtime.toString('yyyy-MM-dd HH:mm:ss dddd'))

    def timeTick(self):
        self.showLabelTime()

    def statrtTimer(self):
        self.timer.setInterval(1000)
        self.timer.start()
        self.startBtn.setEnabled(False)
        self.startBtn.setEnabled(True)
        pass
    def stopTimer(self):
        self.timer.stop()
        self.startBtn.setEnabled(True)
        self.stopbtn.setEnabled(False)






if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = TimerDemo()
    main.show()
    sys.exit(app.exec_())
