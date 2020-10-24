from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys,math


class DrawCalendarDemo(QWidget):
    def __init__(self):
        super(DrawCalendarDemo, self).__init__()
        self.InitUI()

    def InitUI(self):
        self.setWindowTitle('在窗口上绘制日历')
        self.resize(800, 500)
        self.cal=QCalendarWidget(self)
        self.cal.clicked.connect(self.showData)
        self.cal.setMinimumDate(QDate(1970,1,1))
        self.cal.setMaximumDate(QDate(2050,1,1))
        self.cal.setGridVisible(True)
        self.cal.move(50,50)
        self.setWindowTitle('日历演示')

        self.datelable=QLabel(self)
        self.datelable.move(50,300)
        self.datelable.setText(self.cal.selectedDate().toString('yyyy-MM-dd HH-mm-ss dddd'))

        # layout=QVBoxLayout(self)
        # layout.setGeometry(QRect(400,50,100,100))
        datetimeEdit1=QDateTimeEdit(self)
        datetimeEdit1.move(400,50)
        datetimeEdit1.setDisplayFormat('yyyy-MM-dd HH:mm:ss')
        datetimeEdit1.dateTimeChanged.connect(self.ondatetimeChnage)
        datetimeEdit1.setObjectName('datetimeEdit1')

        self.datetimeEdit2=QDateTimeEdit(self)
        self.datetimeEdit2.setObjectName('datetimeEdit2')
        self.datetimeEdit2.setDateTime(QDateTime(QDate.currentDate()))
        self.datetimeEdit2.move(400,100)
        #设置日历弹框
        self.datetimeEdit2.setCalendarPopup(True)
        # datetimeEdit2.dateTimeChanged.connect(self.ondatetimeChnage)
        self.datetimeEdit2.dateTimeChanged.connect(lambda: self.ondatetimeChnage(self.datetimeEdit2.dateTime()))
        dateedit=QDateEdit(self)
        dateedit.setDate(QDate.currentDate())
        dateedit.move(400,150)
        dateedit.setDisplayFormat('yyyy/MM/dd')
        timeedit=QTimeEdit(self)
        timeedit.setTime(QTime.currentTime())
        timeedit.move(400,200)
        timeedit.setDisplayFormat('HH-mm-ss')
        # layout.addWidget(datetimeEdit1)
        # layout.addWidget(datetimeEdit2)
        # layout.addWidget(dateedit)
        # layout.addWidget(timeedit)


    def showData(self,data):
        self.datelable.setText(data.toString('yyyy-MM-dd HH-mm-ss dddd'))


    def ondatetimeChnage(self,datetime):
        print(self.sender().objectName())
        print(datetime)
        # print(self.sender().dateTime())

    # def ondatetimeChnage(self,datetime):
    #     print('second method')
    #     print(datetime)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = DrawCalendarDemo()
    main.show()
    sys.exit(app.exec_())
