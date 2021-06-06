from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys,math
'''
使用Qthread编写计数器
'''
sec=0

class WorkThread(QThread):
    #//信号自定义方式
    timer=pyqtSignal()
    end=pyqtSignal()

    def run(self):
       while True:
           self.sleep(1)
           if sec>=5:
               self.end.emit()   #信号发送，槽接收
               break
           self.timer.emit()


class TimerDemo(QWidget):
    def __init__(self, parent=None):
        super(TimerDemo, self).__init__(parent)
        self.InitUI()
        self.setWindowTitle('使用Qthread编写计数器')
        self.resize(300,200)
        loyout=QVBoxLayout()
        self.lcdnumber=QLCDNumber()
        loyout.addWidget(self.lcdnumber)

        self.button=QPushButton("开始计数")
        loyout.addWidget(self.button)

        self.workthread=WorkThread()
        self.workthread.timer.connect(self.counttime)
        self.workthread.end.connect(self.end)
        self.button.clicked.connect(self.work)
        self.setLayout(loyout)

    def counttime(self):
        global  sec
        sec+=1
        self.lcdnumber.display(sec)
    def  end(self):
        QMessageBox.information(self,"消息","计数结束",QMessageBox.Ok)
    def work(self):
        self.workthread.start()



    def InitUI(self):
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main=TimerDemo()
    main.show()
    sys.exit(app.exec_())
