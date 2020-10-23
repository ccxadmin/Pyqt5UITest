from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

'''
Qmessagebox
消息对话框
'''
class messageboxDemo(QWidget):
    def __init__(self):
        super(messageboxDemo,self).__init__()
        self.InitUI()

    def InitUI(self):
        self.setWindowTitle('显示对话框')
        self.resize(300,400)
        layout=QVBoxLayout()
        self.button1=QPushButton(self)
        # self.button1.move(50,50)
        # self.button1.setFixedWidth(200)
        self.button1.setText('显示关于对话框')
        self.button1.clicked.connect(self.showDialogEvent)
        layout.addWidget(self.button1)

        self.button2 = QPushButton(self)
        # self.button1.move(50,50)
        # self.button1.setFixedWidth(200)
        self.button2.setText('显示消息对话框')
        self.button2.clicked.connect(self.showDialogEvent)
        layout.addWidget(self.button2)

        self.button3 = QPushButton(self)
        # self.button1.move(50,50)
        # self.button1.setFixedWidth(200)
        self.button3.setText('显示警告对话框')
        self.button3.clicked.connect(self.showDialogEvent)
        layout.addWidget(self.button3)

        self.button4= QPushButton(self)
        # self.button1.move(50,50)
        # self.button1.setFixedWidth(200)
        self.button4.setText('显示错误对话框')
        self.button4.clicked.connect(self.showDialogEvent)
        layout.addWidget(self.button4)

        self.button5 = QPushButton(self)
        # self.button1.move(50,50)
        # self.button1.setFixedWidth(200)
        self.button5.setText('显示提问对话框')
        self.button5.clicked.connect(self.showDialogEvent)
        layout.addWidget(self.button5)

        self.setLayout(layout)

    def showDialogEvent(self):
        text=self.sender().text()
        reply=""
        if text.rstrip()=='显示关于对话框':
            QMessageBox.about(self,"info",'这是一个关于对话框')
        elif text.rstrip()=='显示消息对话框':
            reply=QMessageBox.information(self,'Info','这是一个消息对话框',QMessageBox.Yes|QMessageBox.No,QMessageBox.Yes)

        elif text.rstrip() == '显示警告对话框':
            reply = QMessageBox.warning(self, 'Info', '这是一个警告对话框', QMessageBox.Yes | QMessageBox.No,
                                            QMessageBox.Yes)


        elif text.rstrip() == '显示提问对话框':
            reply = QMessageBox.question(self, 'Info', '这是一个提问对话框', QMessageBox.Yes | QMessageBox.No,
                                        QMessageBox.Yes)

        else:
            reply = QMessageBox.critical(self, 'Info', '这是一个错误对话框', QMessageBox.Yes | QMessageBox.No,
                                            QMessageBox.Yes)

        print(reply == QMessageBox.Yes)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = messageboxDemo()
    main.show()
    sys.exit(app.exec_())
