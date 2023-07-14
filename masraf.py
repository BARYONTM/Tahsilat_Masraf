import csv
from PyQt5.QtWidgets import QDialog, QLabel, QLineEdit, QPushButton, QVBoxLayout, QApplication, QMessageBox, QComboBox
from PyQt5.QtCore import QDate, Qt
from PyQt5.QtGui import QPixmap
import maskayit

class MasrafWindow(QDialog):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Masraf')
        self.setGeometry(200, 200, 500, 400)

        # Sol üst köşede logo
        logo_label = QLabel(self)
        logo_pixmap = QPixmap('logo.png').scaled(100, 100)  # Logo boyutu burada ayarlanıyor
        logo_label.setPixmap(logo_pixmap)
        logo_label.setAlignment(Qt.AlignTop | Qt.AlignLeft)

        # Sağ üst köşede tarih
        today = QDate.currentDate()
        date_label = QLabel(self)
        date_label.setText(today.toString(Qt.DefaultLocaleLongDate))
        date_label.setAlignment(Qt.AlignTop | Qt.AlignRight)

        # Ortada Masraf makbuzu yazısı
        title_label = QLabel(self)
        title_label.setText('Masraf Makbuzu')
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("font-size: 20px; font-weight: bold; margin-top: 30px;")

        # Firma adı girişi
        firma_label = QLabel('Firma Adı:', self)
        firma_label.setStyleSheet("font-size: 14px; margin-top: 30px;")
        self.firma_input = QLineEdit(self)

        # Tutar girişi
        tutar_label = QLabel('Tutar:', self)
        tutar_label.setStyleSheet("font-size: 14px;")
        self.tutar_input = QLineEdit(self)

        # Döviz türü seçimi
        doviz_label = QLabel('Döviz Türü:', self)
        doviz_label.setStyleSheet("font-size: 14px;")
        self.doviz_combo = QComboBox(self)
        self.doviz_combo.addItem('TL')
        self.doviz_combo.addItem('USD')
        self.doviz_combo.addItem('EUR')

        # Ödeme türü seçimi
        odeme_label = QLabel('Ödeme Türü:', self)
        odeme_label.setStyleSheet("font-size: 14px;")
        self.odeme_combo = QComboBox(self)
        self.odeme_combo.addItem('Nakit')
        self.odeme_combo.addItem('Çek')
        self.odeme_combo.addItem('Kart')

        # Kısa açıklama girişi
        aciklama_label = QLabel('Kısa Açıklama:', self)
        aciklama_label.setStyleSheet("font-size: 14px;")
        self.aciklama_input = QLineEdit(self)

        # Kaydet ve Kayıtlar düğmeleri
        save_button = QPushButton('Kaydet', self)
        save_button.clicked.connect(self.save_masraf)

        kayitlar_button = QPushButton('Kayıtlar', self)
        kayitlar_button.clicked.connect(self.show_kayitlar)

        # Layout düzeni
        layout = QVBoxLayout()
        layout.addWidget(logo_label)
        layout.addWidget(date_label)
        layout.addWidget(title_label)
        layout.addWidget(firma_label)
        layout.addWidget(self.firma_input)
        layout.addWidget(tutar_label)
        layout.addWidget(self.tutar_input)
        layout.addWidget(doviz_label)
        layout.addWidget(self.doviz_combo)
        layout.addWidget(odeme_label)
        layout.addWidget(self.odeme_combo)
        layout.addWidget(aciklama_label)
        layout.addWidget(self.aciklama_input)
        layout.addWidget(save_button)
        layout.addWidget(kayitlar_button)

        self.setLayout(layout)

    def save_masraf(self):
        firma = self.firma_input.text()
        tutar = self.tutar_input.text()
        doviz = self.doviz_combo.currentText()
        odeme = self.odeme_combo.currentText()
        aciklama = self.aciklama_input.text()

        # Gerekli alanların boş olup olmadığını kontrol etme
        if not firma or not tutar or not aciklama:
            QMessageBox.warning(self, 'Hata', 'Lütfen tüm alanları doldurun.')
            return

        # Masrafı kaydetme işlemi burada gerçekleştirilir
        with open('masraf_kayitlar.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([firma, tutar, doviz, odeme, aciklama])

        QMessageBox.information(self, 'Kaydet', 'Masraf kaydedildi.')

    def show_kayitlar(self):
        self.kayitlar_window = maskayit.KayitlarWindow()
        self.kayitlar_window.exec_()

if __name__ == '__main__':
    app = QApplication([])
    window = MasrafWindow()
    window.show()
    app.exec_()
