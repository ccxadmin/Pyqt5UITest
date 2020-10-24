from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys,math

class DrawShapeDemo(QWidget):
      def __init__(self):
          super(DrawShapeDemo,self).__init__()
          self.InitUI()

      def InitUI(self):
          self.setWindowTitle('在窗口上绘制各种样式的图形')
          self.resize(500,500)


      def paintEvent(self,event):
          painter=QPainter()
          painter.begin(self)
          pen=QPen(Qt.blue,3)
          painter.setPen(pen)
          Rect=QRect(50,50,200,200)
          painter.drawArc(Rect,0,90*16)

          painter.setPen(Qt.red)
          brush=QBrush(Qt.green,Qt.SolidPattern)
          painter.setBrush(brush)
          painter.drawEllipse(100,100,50,30)

          image=QImage('resizeApi.png')
          rect=QRect(10,10,image.width(),image.height())
          painter.drawImage(rect,image)

          painter.end()

if __name__=="__main__":
    app=QApplication(sys.argv)
    main =DrawShapeDemo()
    main.show()
    sys.exit(app.exec_())
