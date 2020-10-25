from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys,math


class ListviewDemo(QWidget):
    def __init__(self):
        super(ListviewDemo, self).__init__()
        self.InitUI()
        self.setWindowTitle('创建List表Demo')
        self.resize(500,500)


    def InitUI(self):
        self.listview=QListView()

        self.model=QStringListModel(['列表项1','列表项2','列表项3'])
        #self.model.setStringList()
        self.listview.setModel( self.model)
        self.listview.clicked.connect(self.showmessage)

        layout=QVBoxLayout()
        layout.addWidget(self.listview)
        self.setLayout(layout)

    def showmessage(self,index):
        QMessageBox.information(self,'Information','你点击了Listview中的'+self.model.data(index,0))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = ListviewDemo()
    main.show()
    sys.exit(app.exec_())
