from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtGui import QPainter,QFont,QColor
from PyQt5.QtCore import Qt
import sys,math

class DrawPointsDemo(QWidget):
      def __init__(self):
          super(DrawPointsDemo,self).__init__()
          self.InitUI()

      def InitUI(self):
          self.setWindowTitle('在窗口上绘制两个周期的正弦曲线')
          self.resize(300,400)


      def paintEvent(self,event):
          painter=QPainter()
          painter.begin(self)
          painter.setPen(Qt.blue)
          size=self.size()
          for i in range(0,1000):
              x=100*(-1+2*i/1000)+size.width()/2.0
              y=-50*math.sin((x-size.width()/2.0)*math.pi/50)+size.height()/2.0
              painter.drawPoint(x,y)
          painter.end()

if __name__=="__main__":
    app=QApplication(sys.argv)
    main =DrawPointsDemo()
    main.show()
    sys.exit(app.exec_())
