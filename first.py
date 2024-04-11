#тут будет класс с окном - инстукцией
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout

class First():
    def __init__(self):
        self.win = QWidget()
        self.win.show()


if __name__ == "__main__":
    app = QApplication([])
    win1 = First()
    app.exec()