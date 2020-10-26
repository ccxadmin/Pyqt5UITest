#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '
'''
多控件显示
关联信号与槽
校验器
输入限制
正则表达式
等等demo

'''
__author__ = 'ccxadmin'

import sys
import BuddySetUI
from PyQt5.QtWidgets import QApplication, QMainWindow


def TestCloseEvent(self):
    try:
      print(self.text())
    except Exception:
      pass

def linkHovered(self):
    print("鼠标滑过"+self)
def linkActivated(self):
    print("鼠标点击Label"+self)

def CobxSelectChnage(comboBox):
    print("鼠标点击" +comboBox.currentText()+"index:%s"%(comboBox.currentIndex()))



if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainwindow = QMainWindow()
    ui = BuddySetUI.Ui_MainWindow()
    ui.setupUi(mainwindow)
    ui.comboBox.addItem('VB')
    ui.comboBox.addItems(['C++','C#','JAVA','PYTHON'])
    ui.comboBox.currentIndexChanged.connect(lambda:CobxSelectChnage(ui.comboBox))
    ui.pushButton.clicked.connect(lambda:TestCloseEvent(ui.pushButton))
    ui.label_5.linkActivated.connect(linkActivated)
    ui.label_5.linkHovered.connect(linkHovered)
    mainwindow.show()
    sys.exit(app.exec_())



