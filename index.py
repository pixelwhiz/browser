import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QWebView

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Web Browser")
        self.setGeometry(100, 100, 800, 600)

        # Membuat widget untuk input URL
        self.url_input = QLineEdit()
        self.url_input.returnPressed.connect(self.load_url)

        # Membuat tombol untuk melakukan load URL
        self.load_button = QPushButton("Load")
        self.load_button.clicked.connect(self.load_url)

        # Membuat layout horizontal untuk input URL dan tombol load
        self.input_layout = QHBoxLayout()
        self.input_layout.addWidget(self.url_input)
        self.input_layout.addWidget(self.load_button)

        # Membuat widget untuk menampilkan web view
        self.web_view = QWebView()

        # Membuat layout vertical untuk input dan web view
        self.layout = QVBoxLayout()
        self.layout.addLayout(self.input_layout)
        self.layout.addWidget(self.web_view)

        self.setLayout(self.layout)

    def load_url(self):
        # Mengambil URL dari input dan load ke web view
        url = self.url_input.text()
        self.web_view.load(url)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
