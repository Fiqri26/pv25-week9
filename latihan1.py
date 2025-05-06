import sys
from PyQt5.QtWidgets import *

class InputDialogDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Input Dialog demo")
        self.setGeometry(200, 200, 400, 200)

        self.btn_pilihBahasa = QPushButton("Choose from list")
        self.btn_nama = QPushButton("get name")
        self.btn_nim = QPushButton("get nim")
        self.btn_angka = QPushButton("Enter an integer")

        self.bahasa = QLineEdit()
        self.nama = QLineEdit()
        self.nim = QLineEdit()
        self.angka = QLineEdit()

        self.btn_pilihBahasa.clicked.connect(self.Pilih_Bahasa)
        self.btn_nama.clicked.connect(self.Masukkan_Nama)
        self.btn_nim.clicked.connect(self.Masukkan_NIM)
        self.btn_angka.clicked.connect(self.Masukkan_Angka)

        layout = QVBoxLayout()

        row1 = QHBoxLayout()
        row1.addWidget(self.btn_pilihBahasa)
        row1.addWidget(self.bahasa)

        row2 = QHBoxLayout()
        row2.addWidget(self.btn_nama)
        row2.addWidget(self.nama)

        row3 = QHBoxLayout()
        row3.addWidget(self.btn_nim)
        row3.addWidget(self.nim)

        row4 = QHBoxLayout()
        row4.addWidget(self.btn_angka)
        row4.addWidget(self.angka)

        layout.addLayout(row1)
        layout.addLayout(row2)
        layout.addLayout(row3)
        layout.addLayout(row4)

        self.setLayout(layout)

    def Pilih_Bahasa(self):
        items = ("C", "C++", "Java", "Python", "Kotlin")
        item, ok = QInputDialog.getItem(self, "select input dialog",
                                        "list of languages", items, 0, False)
        if ok and item:
            self.bahasa.setText(item)

    def Masukkan_Nama(self):
        text, ok = QInputDialog.getText(self, "Text Input Dialog", "Enter your name:")
        if ok and text:
            self.nama.setText(text)

    def Masukkan_NIM(self):
        text, ok = QInputDialog.getText(self, "Text Input Dialog", "Enter your NIM:")
        if ok and text:
            self.nim.setText(text)

    def Masukkan_Angka(self):
        num, ok = QInputDialog.getInt(self, "integer input dialog", "enter a number", 0, -100, 100, 1)
        if ok:
            self.angka.setText(str(num))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = InputDialogDemo()
    demo.show()
    sys.exit(app.exec_())
