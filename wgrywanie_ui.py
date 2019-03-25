# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wgrywanie.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_uploader(object):
    def setupUi(self, uploader):
        uploader.setObjectName("uploader")
        uploader.resize(328, 338)
        uploader.setSizeGripEnabled(False)
        uploader.setModal(False)
        self.verticalLayout = QtWidgets.QVBoxLayout(uploader)
        self.verticalLayout.setObjectName("verticalLayout")
        self.load_location = QtWidgets.QLineEdit(uploader)
        self.load_location.setAlignment(QtCore.Qt.AlignCenter)
        self.load_location.setObjectName("load_location")
        self.verticalLayout.addWidget(self.load_location)
        self.browse = QtWidgets.QPushButton(uploader)
        self.browse.setObjectName("browse")
        self.verticalLayout.addWidget(self.browse)
        self.progressBar = QtWidgets.QProgressBar(uploader)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)
        self.accept = QtWidgets.QPushButton(uploader)
        self.accept.setObjectName("accept")
        self.verticalLayout.addWidget(self.accept)

        self.retranslateUi(uploader)
        QtCore.QMetaObject.connectSlotsByName(uploader)

    def retranslateUi(self, uploader):
        _translate = QtCore.QCoreApplication.translate
        uploader.setWindowTitle(_translate("uploader", "Wgrywanie WD"))
        self.load_location.setPlaceholderText(_translate("uploader", "adres pliku..."))
        self.browse.setText(_translate("uploader", "Wybierz plik"))
        self.accept.setText(_translate("uploader", "Wgraj"))

