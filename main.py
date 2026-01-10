import sys
import webbrowser
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit,
    QPushButton, QFileDialog, QVBoxLayout, QHBoxLayout,
    QComboBox, QMessageBox, QFrame
)
from PyQt6.QtCore import Qt
from convertor import convert_file


class OpenConvert(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("OpenConvert")
        self.setFixedSize(520, 380)
        self.setStyleSheet(self.load_styles())
        self.init_ui()

    def init_ui(self):
        # Title
        title = QLabel("OpenConvert")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setObjectName("title")

        subtitle = QLabel("Simple • Fast • Open Source")
        subtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        subtitle.setObjectName("subtitle")

        line = QFrame()
        line.setFrameShape(QFrame.Shape.HLine)
        line.setFrameShadow(QFrame.Shadow.Sunken)

        # File input
        self.file_input = QLineEdit()
        self.file_input.setPlaceholderText("Select a file to convert…")

        browse_btn = QPushButton("Browse")
        browse_btn.clicked.connect(self.browse_file)

        file_layout = QHBoxLayout()
        file_layout.addWidget(self.file_input)
        file_layout.addWidget(browse_btn)

        # Format selection
        format_label = QLabel("Output Format")
        self.format_box = QComboBox()
        self.format_box.addItems([
            "JPG", "JPEG", "PNG", "WEBP", "BMP", "TIFF", "PDF"
        ])

        # Convert button
        self.convert_btn = QPushButton("Convert File")
        self.convert_btn.clicked.connect(self.convert_now)
        self.convert_btn.setEnabled(False)

        # -------- Footer (Contribute & About) --------
        footer_layout = QHBoxLayout()
        footer_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)

        contribute_link = QLabel('<a href="#">Contribute</a>')
        contribute_link.setOpenExternalLinks(False)
        contribute_link.linkActivated.connect(self.open_contribute)

        about_link = QLabel('<a href="#">About</a>')
        about_link.setOpenExternalLinks(False)
        about_link.linkActivated.connect(self.show_about)

        footer_layout.addWidget(contribute_link)
        footer_layout.addWidget(QLabel(" | "))
        footer_layout.addWidget(about_link)

        # Main layout
        layout = QVBoxLayout()
        layout.setSpacing(15)
        layout.setContentsMargins(25, 20, 25, 20)

        layout.addWidget(title)
        layout.addWidget(subtitle)
        layout.addWidget(line)
        layout.addLayout(file_layout)
        layout.addWidget(format_label)
        layout.addWidget(self.format_box)
        layout.addWidget(self.convert_btn)
        layout.addStretch()              # pushes footer to bottom
        layout.addLayout(footer_layout)  # bottom-left links

        self.setLayout(layout)

    def browse_file(self):
        path, _ = QFileDialog.getOpenFileName(self, "Select File")
        if path:
            self.file_input.setText(path)
            self.convert_btn.setEnabled(True)

    def convert_now(self):
        path = self.file_input.text()
        fmt = self.format_box.currentText()

        try:
            out = convert_file(path, fmt)
            QMessageBox.information(
                self,
                "Success",
                f"File converted successfully!\n\nSaved as:\n{out}"
            )
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    # -------- Footer actions --------
    def open_contribute(self):
        # Replace this with your real GitHub repo URL
        webbrowser.open("https://github.com/yourusername/OpenConvert")

    def show_about(self):
        QMessageBox.information(
            self,
            "About OpenConvert",
            "OpenConvert\n\n"
            "An open-source, multi-format file converter built with Python & PyQt.\n\n"
            "Supports images and documents:\n"
            "PNG, JPG, JPEG, WEBP, BMP, TIFF, TXT, DOCX, PPT, PPTX → PDF.\n\n"
            "Built in 2026 with passion for clean and useful software."
        )

    def load_styles(self):
        return """
        QWidget {
            background-color: #1e1e1e;
            color: #ffffff;
            font-family: Segoe UI;
            font-size: 13px;
        }

        QLabel#title {
            font-size: 22px;
            font-weight: bold;
            color: #4fc3f7;
        }

        QLabel#subtitle {
            font-size: 11px;
            color: #aaaaaa;
        }

        QLineEdit {
            background-color: #2b2b2b;
            border: 1px solid #444;
            border-radius: 6px;
            padding: 6px;
        }

        QComboBox {
            background-color: #2b2b2b;
            border: 1px solid #444;
            border-radius: 6px;
            padding: 6px;
        }

        QPushButton {
            background-color: #4fc3f7;
            color: #000;
            border-radius: 6px;
            padding: 8px;
            font-weight: bold;
        }

        QPushButton:hover {
            background-color: #81d4fa;
        }

        QPushButton:disabled {
            background-color: #555;
            color: #999;
        }

        QLabel a {
            color: #4fc3f7;
            text-decoration: none;
        }

        QLabel a:hover {
            color: #81d4fa;
            text-decoration: underline;
        }
        """


# App start
app = QApplication(sys.argv)
window = OpenConvert()
window.show()
sys.exit(app.exec())
