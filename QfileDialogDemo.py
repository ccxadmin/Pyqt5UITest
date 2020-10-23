from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

'''
QFiledialog
文件对话框
'''
class FileDialogDemo(QWidget):
    def __init__(self):
        super(FileDialogDemo,self).__init__()
        self.InitUI()

    def InitUI(self):
            self.setWindowTitle('文件择对话框')
            layout = QVBoxLayout()
            self.button1 = QPushButton('图像加载')
            self.button1.clicked.connect(self.getImageFile)
            layout.addWidget(self.button1)
            self.loadImageLabel=QLabel()
            layout.addWidget(self.loadImageLabel)

            self.button2 = QPushButton('文件选择')
            self.button2.clicked.connect(self.getContents)
            layout.addWidget(self.button2)
            self.contents=QTextEdit()
            layout.addWidget(self.contents)

            self.setLayout(layout)

    def getImageFile(self):
        try:
           frame,_=  QFileDialog.getOpenFileName(self,'打开文件','.','图像(*.png *.jpg)')
           self.loadImageLabel.setPixmap(QPixmap(frame))
        except BaseException :
            print(BaseException.args)

    def getContents(self):
        qdialog=QFileDialog()
        qdialog.setFileMode(QFileDialog.AnyFile)
        qdialog.setFilter(QDir.Files)
        if qdialog.exec():
            with open(qdialog.selectedFiles()[0],encoding='utf-8',mode='r') as f:
               self.contents.setText(f.read())


if __name__ == "__main__":
        app = QApplication(sys.argv)
        main = FileDialogDemo()
        main.show()
        sys.exit(app.exec_())