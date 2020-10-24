from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys,math


class Mycombobox(QComboBox):
    def __init__(self):
        super(Mycombobox, self).__init__()
        self.setAcceptDrops(True)

    def dragEnterEvent(self, Event):
        print(Event)
        if Event.mimeData().hasText():
            Event.accept()
        else:
            Event.ignore()

    def dropEvent(self, Event):
        self.addItem(Event.mimeData().text())

class DragDropDemo(QWidget):
    def __init__(self):
        super(DragDropDemo, self).__init__()
        self.InitUI()
    def InitUI(self):
        formlayout=QFormLayout()
        formlayout.addRow(QLabel("下面可进行拖拽"))
        lineEdit=QLineEdit()
        lineEdit.setDragEnabled(True)
        combox=Mycombobox()

        formlayout.addRow(lineEdit,combox)
        self.setLayout(formlayout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = DragDropDemo()
    main.show()
    sys.exit(app.exec_())
