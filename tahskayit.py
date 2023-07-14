import csv
from PyQt5.QtWidgets import QDialog, QLabel, QPushButton, QVBoxLayout, QTableWidget, QTableWidgetItem, QMessageBox

class KayitlarWindow(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Kayıtlar')
        self.setGeometry(200, 200, 675, 400)

        self.initUI()

    def initUI(self):
        # Tablo oluşturma
        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(['Firma', 'Tutar', 'Döviz', 'Ödeme Türü', 'Açıklama'])

        # Kayıtları yükleme
        self.load_kayitlar()

        # Sil düğmesi
        sil_button = QPushButton('Sil', self)
        sil_button.clicked.connect(self.delete_kayit)

        # Layout düzeni
        layout = QVBoxLayout()
        layout.addWidget(self.table)
        layout.addWidget(sil_button)

        self.setLayout(layout)

    def load_kayitlar(self):
        self.table.setRowCount(0)

        with open('tahsilat_kayitlar.csv', 'r') as file:
            reader = csv.reader(file)

            for row_data in reader:
                row = self.table.rowCount()
                self.table.insertRow(row)

                for column, data in enumerate(row_data):
                    item = QTableWidgetItem(data)
                    self.table.setItem(row, column, item)

    def delete_kayit(self):
        selected_rows = self.table.selectionModel().selectedRows()

        if len(selected_rows) > 0:
            confirm = QMessageBox.question(self, 'Sil', 'Seçili kayıtları silmek istiyor musunuz?', QMessageBox.Yes | QMessageBox.No)

            if confirm == QMessageBox.Yes:
                rows_to_delete = []
                for row in selected_rows:
                    rows_to_delete.append(row.row())

                rows_to_delete.sort(reverse=True)

                for row in rows_to_delete:
                    self.table.removeRow(row)

                self.save_kayitlar()

    def save_kayitlar(self):
        with open('tahsilat_kayitlar.csv', 'w', newline='') as file:


            for row in range(self.table.rowCount()):
                row_data = []

                for column in range(self.table.columnCount()):
                    item = self.table.item(row, column)

                    if item is not None:
                        row_data.append(item.text())
                    else:
                        row_data.append('')

                writer.writerow(row_data)

        QMessageBox.information(self, 'Kayıtlar', 'Değişiklikler kaydedildi.')

if __name__ == '__main__':
    app = QApplication([])
    window = KayitlarWindow()
    window.show()
    app.exec_()
