# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets


class InheritedClass(QtWidgets.QDialog, QtWidgets.QMainWindow):
    def closeEvent(self, bool):
        pass


class NoneInheritedClass(object):
    def closeEvent(self):
        pass