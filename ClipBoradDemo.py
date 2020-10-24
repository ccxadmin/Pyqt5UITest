from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys,math


class ClipBoradDemo(QDialog):
    def __init__(self):
        super(ClipBoradDemo, self).__init__()
        self.InitUI()

    def InitUI(self):
        textCopybutton=QPushButton("复制文本")
        textCopybutton.clicked.connect(self.buttonClick)
        textPastebutton=QPushButton('粘贴文本')
        textPastebutton.clicked.connect(self.buttonClick)

        htmlCopybutton=QPushButton('复制html')
        htmlCopybutton.clicked.connect(self.buttonClick)
        htmlPastebutton=QPushButton('粘贴html')
        htmlPastebutton.clicked.connect(self.buttonClick)

        imageCopybutton=QPushButton('复制图像')
        imageCopybutton.clicked.connect(self.buttonClick)
        imagePastebutton=QPushButton('粘贴图像')
        imagePastebutton.clicked.connect(self.buttonClick)

        self.textlable=QLabel('默认文本')
        imagelable=QLabel()
        imagelable.setPixmap(QPixmap('resizeApi.png'))
        gridlayout=QGridLayout()
        gridlayout.addWidget(textCopybutton,0,0)
        gridlayout.addWidget(htmlCopybutton,0,1)
        gridlayout.addWidget(imageCopybutton,0,2)
        gridlayout.addWidget(textPastebutton,1,0)
        gridlayout.addWidget(htmlPastebutton, 1, 1)
        gridlayout.addWidget(imagePastebutton, 1, 2)
        gridlayout.addWidget(self.textlable,2,0,1,2)
        gridlayout.addWidget(imagelable,2,2)
        self.setLayout(gridlayout)

    def buttonClick(self):
        sender=self.sender()
        clipboard = QApplication.clipboard()
        if sender.text().strip()=="复制文本":

            clipboard.setText("hello,world")
        elif sender.text().strip()=="粘贴文本":
            #clipboard = QApplication.clipboard()
            self.textlable.setText(clipboard.text())
        elif sender.text().strip() == "复制图像":
            #clipboard = QApplication.clipboard()
            clipboard.setPixmap(QPixmap('resizeApi.png'))
        elif sender.text().strip() == "粘贴图像":
            #clipboard = QApplication.clipboard()
            self.textlable.setPixmap(clipboard.pixmap())
        elif sender.text().strip() == "复制html":
            mimeData=QMimeData()
            mimeData.setHtml('</b>Blod and <font color=red>Red</font></b>')
            #clipboard = QApplication.clipboard()
            clipboard.setMimeData(mimeData)
        else :
            #clipboard = QApplication.clipboard()
            mimedata=clipboard.mimeData()
            if mimedata.hasHtml():
                self.textlable.setText(mimedata.html())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = ClipBoradDemo()
    main.show()
    sys.exit(app.exec_())
