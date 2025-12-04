# esta es una version sin class, lo mas simple
from PySide6.QtWidgets import QApplication, QWidget, QPushButton
import sys

app = QApplication(sys.argv)

window = QWidget()
window.resize(500, 500)

btn = QPushButton("Hola Mundo", window)
btn.move(200, 200)

window.show()
sys.exit(app.exec())

sys.exit(app.exec());
# 