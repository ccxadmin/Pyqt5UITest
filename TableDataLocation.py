from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys,math
'''

'''

class TableDataLocationDemo(QMainWindow):
    def __init__(self):
        super(TableDataLocationDemo, self).__init__()
        self.InitUI()
        self.setWindowTitle('创建表格单元数据查找')
        self.resize(600,800)


    def InitUI(self):
        self.tabelwdiget=QTableWidget()
        self.tabelwdiget.setRowCount(40)
        self.tabelwdiget.setColumnCount(4)

        for i in range(0,40):
            for j in range(4):
                itemcontent="(%d,%d)"%(i,j)
                self.tabelwdiget.setItem(i,j,QTableWidgetItem(itemcontent))

        # searchtext="(13,0)"
        # items = self.tabelwdiget.findItems(searchtext, Qt.MatchExactly)
        searchtext = "(13"
        items= self.tabelwdiget.findItems(searchtext,Qt.MatchStartsWith)
        if len(items)>0:
            for s in items:
                # s.setBackground(QBrush(Qt.red))
                s.setBackground(QBrush(QColor(0,255,0)))
                s.setForeground(QBrush(Qt.red))
                print(s.text())
                #self.tabelwdiget.verticalScrollBar().setSliderPosition(items[0].row())
        else:
            print('None find')



        self.setCentralWidget(self.tabelwdiget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = TableDataLocationDemo()
    main.show()
    sys.exit(app.exec_())
