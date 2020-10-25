from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys,math
from PyQt5.QtPrintSupport import *


class PrintDialogDemo(QWidget):
    def __init__(self):
        super(PrintDialogDemo, self).__init__()
        self.InitUI()
        self.setWindowTitle('打印机对话框DEMO')
        self.resize(500,500)
        self.printer=QPrinter()

    def InitUI(self):
        self.textedit=QTextEdit(self)
        self.textedit.setGeometry(20,20,300,300)

        self.pushbuttono1=QPushButton('打开文件',self)
        self.pushbuttono1.move(350,20)
        self.pushbuttono1.clicked.connect(self.btnopenfileClick)

        self.pushbuttono2=QPushButton('打印设置',self)
        self.pushbuttono2.move(350,80)
        self.pushbuttono2.clicked.connect(self.printsettingclick)

        self.pushbuttono3=QPushButton('打印文档',self)
        self.pushbuttono3.move(350,140)
        self.pushbuttono3.clicked.connect(self.printfileclick)

    def btnopenfileClick(self):
        file,_=QFileDialog.getOpenFileName(self,'打开文件','.')
        #files = QFileDialog.getOpenFileName(self, '打开文件', '.')
        if file:
            with open(file,encoding='utf-8',errors='ignore') as cf:
                self.textedit.setText(cf.read())


    def printsettingclick(self):
        printerDialog=QPageSetupDialog(self.printer,self)
        printerDialog.exec()
        pass
    def printfileclick(self):
        printerDailog=QPrintDialog(self.printer,self)
        if printerDailog.exec()==QDialog.Accepted:
            self.textedit.print(self.printer)




if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = PrintDialogDemo()
    main.show()
    sys.exit(app.exec_())
