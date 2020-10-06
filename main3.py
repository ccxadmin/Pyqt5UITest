import  sys
from login import *
from PyQt5.QtWidgets import QApplication, QLabel


#只有从当前文件启动才会进入，其他不进入if语句
if __name__ == '__main__':
    app = QApplication(sys.argv)
    temlabel = QLabel()
    temlabel.setText("hello,world!")
    temlabel.show()
    sys.exit(app.exec())