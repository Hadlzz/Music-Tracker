import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QListWidget, QLabel, QSpinBox, QWidget, QLineEdit
)


class PerformanceScreen(QMainWindow):
    """Performance screen window"""
    
    def __init__(self, song_title):
        super().__init__()
        uic.loadUi("performance_menu.ui", self)
        self.setWindowTitle("Performance Screen")
        
        # Find and update the music_title label
        self.music_title = self.findChild(QLabel, "music_title")
        if self.music_title:
            self.music_title.setText(song_title)
        
        self.record_btn = self.findChild(QPushButton, "record_btn")
        self.bpm_adjuster = self.findChild(QSpinBox, "bpm_slider")
        self.bpm_label = self.findChild(QLabel, "label_bpm")
        self.performance_toolbar = self.findChild(QWidget, "performance_toolbar")


class MainMenu(QMainWindow):
    """Main menu for selecting and searching songs."""
    
    def __init__(self):
        super().__init__()
        uic.loadUi("main_menu.ui", self)
        

        #Identify Widgets
        self.list_music_lib = self.findChild(QListWidget, "list_musicLib")
        self.list_recently_lib = self.findChild(QListWidget, "list_recentlyPlayed")
        self.label_music_lib = self.findChild(QLabel, "label_musicLib")
        self.label_recently_lib = self.findChild(QLabel, "label_recentlyPlayed")
        self.search_bar = self.findChild(QLineEdit, "searchBar")
        
        # Store the music library with song titles
        self.music_titles = [
            "Beethoven - Für Elise", "Beethoven - Moonlight Sonata",
            "Chopin - Nocturne Op. 9 No. 2", "Chopin - Fantaisie-Impromptu",
            "Chopin - Prelude in D-flat Major (Raindrop)", "Debussy - Clair de Lune",
            "Debussy - Arabesque No. 1", "Liszt - Liebestraum No. 3",
            "Liszt - La Campanella", "Mozart - Rondo Alla Turca",
            "Mozart - Sonata in C Major (K. 545)", "Bach - Prelude in C Major",
            "Bach - Toccata and Fugue in D Minor", "Rachmaninoff - Prelude in C-sharp Minor",
            "Rachmaninoff - Piano Concerto No. 2", "Schumann - Träumerei",
            "Tchaikovsky - The Seasons: June (Barcarolle)", "Satie - Gymnopédie No. 1",
            "Saint-Saëns - The Swan", "Grieg - Morning Mood",
            "Grieg - In the Hall of the Mountain King", "Scarlatti - Sonata in D Minor (K. 141)",
            "Albeniz - Asturias", "Gershwin - Rhapsody in Blue",
            "Yiruma - River Flows in You", "Einaudi - Nuvole Bianche",
            "Einaudi - Una Mattina"
        ]
        
        #
        self.populate_music_lib()
        self.list_music_lib.doubleClicked.connect(self.list_music_lib_clicked)
        self.search_bar.textChanged.connect(self.search_query)
    
    def populate_music_lib(self):
        """Fills the music library with all available songs."""
        self.list_music_lib.clear()
        self.list_music_lib.addItems(self.music_titles)
    
    def search_query(self):
        """Filters the music list based on search input."""
        search_text = self.search_bar.text().lower()
        self.list_music_lib.clear()
        
        if not search_text:
            self.list_music_lib.addItems(self.music_titles)
            return
        
        filtered_items = [
            item for item in self.music_titles 
            if search_text in item.lower()
        ]
        
        self.list_music_lib.addItems(filtered_items)
    
    def list_music_lib_clicked(self):
        """Opens the performance screen when a song is selected."""
        current_item = self.list_music_lib.currentItem()
        if current_item:
            selected_song = current_item.text()
            self.add_recentlyPlayed(selected_song)
            self.performance = PerformanceScreen(selected_song)
            self.performance.show()


    def add_recentlyPlayed(self, song):

        # Check if the song is already in the recently played list
        recent_items = [self.list_recently_lib.item(i).text() for i in range(self.list_recently_lib.count())]
    
        if song not in recent_items:
            self.list_recently_lib.addItem(song)
            
def main():

    """Starts the PyQt5 application."""
    app = QApplication(sys.argv)
    win = MainMenu()
    win.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
