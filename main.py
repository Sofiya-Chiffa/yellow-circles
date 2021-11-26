import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QPainter, QColor


class Interface:

    def __init__(self, widg):
        widg.setGeometry(300, 300, 450, 450)
        widg.setWindowTitle('circles')
        widg.pushButton = QPushButton('Кнопка', widg)
        widg.pushButton.setGeometry(10, 10, 50, 50)


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        Interface(self)
        self.pushButton.clicked.connect(self.run)

    def run(self):
        self.repaint()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        qp.setBrush(QColor(random.randint(0, 255), random.randint(0, 255),
                           random.randint(0, 255)))
        x, y = random.randint(70, 430), random.randint(70, 430)
        size = random.randint(5, abs(440 - max([x, y])) + 5)
        qp.drawEllipse(x, y, size, size)


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
