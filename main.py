import sys, time
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QListWidget,QListWidgetItem, QLabel, QTextBrowser,\
      QComboBox, QListWidget, QProgressBar, QMessageBox, QDialogButtonBox , QLineEdit, QInputDialog
from mainwindow import Ui_MainWindow

from PyQt5 import uic
from datetime import datetime

TIME_LIMIT = 100

class main_menu(QtWidgets.QMainWindow):

    def __init__(self):

        super(main_menu,self).__init__() # call constrcutor of parent class
        
        uic.loadUi("mainwindow.ui", self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.list_musicLib = self.findChild(QListWidget, "list_musicLib")
        self.list_recentlyLib = self.findChild(QListWidget, "list_recentlyPlayed")
        self.label_musicLib = self.findChild(QLabel, "label_musicLib")
        self.label_recentlyLib = self.findChild(QLabel, "label_recentlyPlayed")
        self.searchBar = self.findChild(QLineEdit, "searchBar")
        self.populate_musicLib()
    
    
    def populate_musicLib(self):
        self.ui.list_musicLib.addItems([
    "Beethoven - Für Elise",
    "Beethoven - Moonlight Sonata",
    "Chopin - Nocturne Op. 9 No. 2",
    "Chopin - Fantaisie-Impromptu",
    "Chopin - Prelude in D-flat Major (Raindrop)",
    "Debussy - Clair de Lune",
    "Debussy - Arabesque No. 1",
    "Liszt - Liebestraum No. 3",
    "Liszt - La Campanella",
    "Mozart - Rondo Alla Turca",
    "Mozart - Sonata in C Major (K. 545)",
    "Bach - Prelude in C Major (Well-Tempered Clavier)",
    "Bach - Toccata and Fugue in D Minor",
    "Rachmaninoff - Prelude in C-sharp Minor",
    "Rachmaninoff - Piano Concerto No. 2",
    "Schumann - Träumerei",
    "Tchaikovsky - The Seasons: June (Barcarolle)",
    "Satie - Gymnopédie No. 1",
    "Saint-Saëns - The Swan",
    "Grieg - Morning Mood",
    "Grieg - In the Hall of the Mountain King",
    "Scarlatti - Sonata in D Minor (K. 141)",
    "Albeniz - Asturias",
    "Gershwin - Rhapsody in Blue",
    "Yiruma - River Flows in You",
    "Einaudi - Nuvole Bianche",
    "Einaudi - Una Mattina"
])
        self.list_musicLib.doubleClicked.connect(self.list_musicLib_clicked)

    def list_musicLib_clicked(self):
        current_item = self.list_musicLib.currentitem()
        if current_item:
             selected_song = current_item.text()
             
         
         





def app():
        app = QtWidgets.QApplication(sys.argv)
        win = main_menu()
        win.show()
        sys.exit(app.exec_())

app()



        


    






        

