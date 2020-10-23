from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
'''
Qmainwindow
Qwidget
slider滑块控件
弹出对话框
'''

class SliderDemo(QWidget):
    def __init__(self):
        super(SliderDemo,self).__init__()
        self.InitUI()

    def InitUI(self):
       self.setWindowTitle("滑块演示DEMO")
       self.resize(300,100)
       layout=QVBoxLayout()
       self.label=QLabel("你好 PYQT5")
       self.label.setAlignment(Qt.AlignCenter)
       layout.addWidget(self.label)
       self.slider=QSlider(Qt.Horizontal)
       self.slider.setMinimum(12)
       self.slider.setMaximum(48)
       self.slider.setSingleStep(3)
       self.slider.setValue(18)
       self.slider.setTickPosition(QSlider.TicksBelow)
       self.slider.setTickInterval(6)
       self.slider.valueChanged.connect(self.valueChange)
       layout.addWidget(self.slider)
       self.button=QPushButton(self)
       self.button.setText('弹出对话框')
       self.button.move(20,20)
       self.button.clicked.connect(self.buttonClickEvent)
       layout.addWidget(self.button)
       self.setLayout(layout)

    def valueChange(self):
        print("当前值: %s" % self.sender().value())
        size =self.slider.value()
        self.label.setFont(QFont('Arail',size))

    def buttonClickEvent(self):
        dialog=QDialog()
        button=QPushButton("对话框按钮",dialog)
        button.clicked.connect(dialog.close)
        button.move(50,50)
        dialog.setWindowTitle('对话框')
        dialog.setWindowModality(Qt.ApplicationModal)
        dialog.exec_()


if __name__=="__main__":
    app=QApplication(sys.argv)
    main=SliderDemo()
    main.show()
    sys .exit(app.exec_())

