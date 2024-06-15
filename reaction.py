import sys
import random
import time
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QDesktopWidget
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QPalette, QColor, QBrush, QPixmap


class ReactionTest(QWidget):
    def __init__(self):
        super().__init__()

        self.start_time = None
        self.reaction_time = None
        self.test_state = None
        self.timer = None

        self.fixed_width = 600
        self.fixed_height = 400

        self.initUI()
        self.start_test()

    def initUI(self):
        self.layout = QVBoxLayout()

        self.label = QLabel('Ждите зелёный цвет', self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setStyleSheet("font-size: 24px; color: white;")

        self.restart_button = QPushButton('Повтор', self)
        self.restart_button.setFixedSize(150, 60)
        self.restart_button.setStyleSheet("""
            QPushButton {
                background-color: #ADD8E6;
                border-style: none;
                border-radius: 30px;
                font-size: 20px;
                color: black;
            }
            QPushButton:hover {
                background-color: #87CEEB;
            }
            QPushButton:pressed {
                background-color: #87CEFA;
            }
        """)
        self.restart_button.clicked.connect(self.start_test)
        self.restart_button.hide()

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.restart_button, 0, Qt.AlignCenter)
        self.setLayout(self.layout)

        self.setWindowTitle('Тренажёр: Время реакции')
        self.setFixedSize(self.fixed_width, self.fixed_height)
        self.center()

        self.set_red_background()
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def set_red_background(self):
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(Qt.red))
        self.setPalette(palette)

    def set_green_background(self):
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(Qt.green))
        self.setPalette(palette)

    def set_image_background(self, image_path):
        palette = self.palette()
        brush = QBrush(QPixmap(image_path))
        palette.setBrush(QPalette.Window, brush)
        self.setPalette(palette)

    def start_test(self):
        if self.test_state == "waiting":
            return
        self.label.setText('Ждите зелёный цвет')
        self.set_red_background()
        self.restart_button.hide()
        self.test_state = "waiting"

        if self.timer:
            self.timer.stop()

        delay = random.randint(2000, 5000)
        self.timer = QTimer(self)
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(self.change_to_green)
        self.timer.start(delay)

    def change_to_green(self):
        if self.test_state == "waiting":
            self.set_green_background()
            self.label.setText('Нажимайте сейчас!')
            self.start_time = time.time()
            self.test_state = "ready"

    def mousePressEvent(self, event):
        if self.test_state == "waiting":
            self.show_early_click_message()
        elif self.test_state == "ready":
            self.reaction_time = int((time.time() - self.start_time) * 1000)
            self.label.setText(f'Время реакции: {self.reaction_time} мс\n Средний показатель у человека: 200 мс \nНажмите для повтора')
            self.start_time = None
            self.test_state = "finished"
        elif self.test_state == "finished":
            self.start_test()

    def show_early_click_message(self):
        self.set_image_background('background.png')
        self.label.setText('Слишком рано! Нажмите на кнопку ниже чтобы повторить')
        self.label.setStyleSheet("font-size: 20px; color: white;")
        self.restart_button.show()
        self.test_state = "early_click"

        if self.timer:
            self.timer.stop()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ReactionTest()
    sys.exit(app.exec_())
