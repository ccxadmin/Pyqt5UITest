from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtGui import QPainter,QFont,QColor
from PyQt5.QtCore import Qt
import sys

class DrawTextDemo(QWidget):
      def __init__(self):
          super(DrawTextDemo,self).__init__()
          self.InitUI()

      def InitUI(self):
          self.setWindowTitle('在窗口上绘制文本')
          self.resize(300,200)
          self.text='Python从菜鸟到高手'

      def paintEvent(self,event):
          painter=QPainter()
          painter.begin(self)
          painter.setPen(QColor(255,0,0))
          #painter.setFont(QFont('SimSun',25))
          painter.setFont(QFont('SimSum',25,10, False))
          painter.drawText(event.rect(),Qt.AlignCenter,self.text)
          painter.end()

if __name__=="__main__":
    app=QApplication(sys.argv)
    main =DrawTextDemo()
    main.show()
    sys.exit(app.exec_())

