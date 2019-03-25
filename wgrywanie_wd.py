from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtPrintSupport import *
from PyQt5.QtWidgets import *
import sys
import requests
import json
from webapiVendo import VendoApi
import xlrd
import re
import wgrywanie_ui
import os
class WgrywanieWD(QDialog, wgrywanie_ui.Ui_uploader):
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)

        #self.load_location.setPlaceholderText("adres pliku...")

        self.browse.clicked.connect(self.browse_file)
        self.accept.clicked.connect(self.upload)
        

    
    
    def browse_file(self):
        load_file = QFileDialog.getOpenFileName(self, caption="Wybierz plik do wczytania...", directory=".")

        load_file1 = load_file[0]



        # text_load = str(load_file)
        self.load_location.setText(QDir.toNativeSeparators(load_file1))
        #plik = xlrd.open_workbook(load_file1)
        

    
    def upload(self):
        load_file1 = self.load_location.text()

        plik = xlrd.open_workbook(load_file1)
        strona = plik.sheet_by_index(0)
        total_cols = strona.ncols
        total_rows = strona.nrows
        licznik = (total_cols - 1) * (total_rows - 1)


        vendoApi = VendoApi()
        vendoApi.setApi("adres")
        vendoApi.setHeader({'Content-Type' : 'application/json', "Content-Length" : "length"})
        vendoApi.logInApi("login","pswd")
        vendoApi.loginUser("login","pswd")
        liczba = 0
        j = 1
        updated = 0
        errors = 0
        

        for e in range(total_cols-1):
            
            i = 1
            nazwa = strona.cell(0,j).value
            for d in range(total_rows-1):
                try:
                    kod = strona.cell(i,0).value
                    kod_query = vendoApi.getJson ('/Magazyn/Towary/Towar', {"Token":vendoApi.USER_TOKEN,"Model":{"Towar":{"Kod":kod}}})
                    numerID = kod_query["Wynik"]["Towar"]["ID"]
                    wartosc = strona.cell(i,j).value
                    response_data = vendoApi.getJson ('/json/reply/Magazyn_Towary_Aktualizuj', {"Token":vendoApi.USER_TOKEN,"Model":{"ID":numerID,"PolaUzytkownika":{"NazwaWewnetrzna":nazwa ,"Wartosc":wartosc}}})
                    updated += 1
                    liczba += 1
                    procent = liczba * 100 / licznik
                    self.progressBar.setValue(int(procent))

                    try:
                        dodane = open("dodane.txt", 'a')
                        dodane.write("Dodaję KOD: " + kod + " | ")
                        dodane.write("nazwaWD: " + nazwa + " | ")
                        dodane.write("wartość: " + wartosc + "\n")
                        dodane.close()
                    except UnicodeEncodeError:
                        pass
                    i += 1
                except KeyError:

                    err = open("errors.txt", 'a')
                    err.write(kod + "\n")
                    err.close()
                    i += 1
                    liczba += 1
                    errors += 1
            procent = liczba * 100 / licznik
            self.progressBar.setValue(int(procent))
            j += 1
            if procent == 100:
                komunikat = "Dodano: {}\nBłędów: {}"  .format(updated, errors)
                QMessageBox.information(self, "Wgrywanie zakończone sukcesem", komunikat)
                self.progressBar.setValue(0)
                self.load_location.setText("adres pliku...")
            else:
                pass



app = QApplication(sys.argv)
wgrywanie = WgrywanieWD()
wgrywanie.show()
app.exec_()