import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtGui import QColor, QPalette

import tahsilat
import masraf

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('KoçakSoft')
        self.setGeometry(200, 200, 800, 600)

        # Arka planı renklendir
        palette = self.palette()
        palette.setColor(QPalette.Background, QColor("#008080"))  # Turkuaz renk
        self.setPalette(palette)

        tahsilat_button = QPushButton('Tahsilat', self)
        tahsilat_button.setGeometry(200, 150, 400, 70)
        tahsilat_button.setStyleSheet("background-color: #FF4500; color: white; font-size: 24px;")
        tahsilat_button.clicked.connect(self.open_tahsilat)

        masraf_button = QPushButton('Masraf', self)
        masraf_button.setGeometry(200, 250, 400, 70)
        masraf_button.setStyleSheet("background-color: #4B0082; color: white; font-size: 24px;")
        masraf_button.clicked.connect(self.open_masraf)

        Pdf_button = QPushButton('PDF Gönder', self)
        Pdf_button.setGeometry(200, 350, 400, 70)
        Pdf_button.setStyleSheet("background-color: #FFD700; color: white; font-size: 24px;")
        Pdf_button.clicked.connect(self.send_Pdf)

    def open_tahsilat(self):
        self.tahsilat_window = tahsilat.TahsilatWindow()
        self.tahsilat_window.exec_()

    def open_masraf(self):
        self.masraf_window = masraf.MasrafWindow()
        self.masraf_window.exec_()

    def send_Pdf(self):
        # Pdf gönderme işlemleri burada gerçekleştirilebilir
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
