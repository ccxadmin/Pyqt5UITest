from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtGui import QPainter,QFont,QColor,QPen
from PyQt5.QtCore import Qt
import sys,math

class DrawLineDemo(QWidget):
      def __init__(self):
          super(DrawLineDemo,self).__init__()
          self.InitUI()

      def InitUI(self):
          self.setWindowTitle('在窗口上绘制各种样式的直线')
          self.resize(300,400)


      def paintEvent(self,event):
          painter=QPainter()
          painter.begin(self)
          pen=QPen(Qt.blue,5)

          pen.setStyle(Qt.SolidLine)
          painter.setPen(pen)
          painter.drawLine(20,40,220,40)

          pen.setStyle(Qt.DashDotDotLine)
          painter.setPen(pen)
          painter.drawLine(20, 80, 220, 80)

          pen.setStyle(Qt.DashLine)
          painter.setPen(pen)
          painter.drawLine(20, 120, 220,120)

          pen.setStyle(Qt.CustomDashLine)
          pen.setDashPattern([1,4,2,5])
          painter.setPen(pen)
          painter.drawLine(20, 160, 220, 160)

          painter.end()

if __name__=="__main__":
    app=QApplication(sys.argv)
    main =DrawLineDemo()
    main.show()
    sys.exit(app.exec_())
