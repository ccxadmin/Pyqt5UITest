#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'ccxadmin'

import sys
import mainwinGridUI
from PyQt5.QtWidgets import QApplication, QMainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainwindow = QMainWindow()
    ui = mainwinGridUI.Ui_MainWindow()
    ui.setupUi(mainwindow)
    mainwindow.show()
    sys.exit(app.exec_())



