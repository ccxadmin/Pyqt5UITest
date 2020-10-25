from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys,math
'''
setitem:将文本放入单元格
setcellwidget:将控件放入单元格
'''

class PlaceControlCell(QMainWindow):
    def __init__(self):
        super(PlaceControlCell, self).__init__()
        self.InitUI()
        self.setWindowTitle('创建表格单元控件放置')
        self.resize(500,500)


    def InitUI(self):
        self.tabelwdiget=QTableWidget()
        self.tabelwdiget.setRowCount(4)
        self.tabelwdiget.setColumnCount(3)
        self.tabelwdiget.setHorizontalHeaderLabels(['姓名','性别','体重'])


        self.tabelwdiget.setItem(0,0,QTableWidgetItem('小敏'))

        self.combox=QComboBox()
        self.combox.addItem('男')
        self.combox.addItem('女')
        self.combox.setStyleSheet('QComboBox{margin:3px};')
        #放置控件
        self.tabelwdiget.setCellWidget(0,1,self.combox)

        self.modifyBtn=QPushButton('修改')
        self.modifyBtn.setDown(True)
        self.modifyBtn.setStyleSheet('QPushButton{margin:3px};')
        self.tabelwdiget.setCellWidget(0,2,self.modifyBtn)

        self.setCentralWidget(self.tabelwdiget)





if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = PlaceControlCell()
    main.show()
    sys.exit(app.exec_())
