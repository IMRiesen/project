import sys
import random
import time
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QTimer

class AimTrainer(QWidget):
    def __init__(self, target_size=70, text_size=24):
        super().__init__()
        self.target_size = target_size
        self.text_size = text_size
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Тренажёр: Тренировка точности')
        self.setFixedSize(800, 600)

        self.background_label = QLabel(self)
        bg_pixmap = QPixmap('background.png')
        if bg_pixmap.isNull():
            print("Изображение заднего фона не найдена")
        self.background_label.setPixmap(bg_pixmap)
        self.background_label.setGeometry(0, 0, 800, 600)
        self.background_label.lower()

        self.targets_hit = 0
        self.total_targets = 30
        self.start_time = None

        self.target_label = QLabel(self)
        self.target_pixmap = QPixmap('target.png')
        if self.target_pixmap.isNull():
            print("Изображение мишени не найдено")
        self.target_label.setPixmap(self.target_pixmap)
        self.target_label.setScaledContents(True)
        self.target_label.resize(self.target_size, self.target_size)
        self.target_label.hide()

        self.remaining_label = QLabel(self)
        self.remaining_label.setText(f"Осталось: {self.total_targets - self.targets_hit}")
        self.remaining_label.setStyleSheet(f"font-size: {self.text_size}px; color: white;")
        self.remaining_label.setAlignment(Qt.AlignCenter)
        self.remaining_label.setGeometry((self.width() - 200) // 2, 10, 200, 30)
        self.remaining_label.show()

        self.result_label = QLabel(self)
        self.result_label.setStyleSheet(f"font-size: {self.text_size}px; color: white;")
        self.result_label.setAlignment(Qt.AlignCenter)
        self.result_label.setGeometry((self.width() - 600) // 2, 10, 600, 50)
        self.result_label.setWordWrap(True)
        self.result_label.hide()

        self.avg_human_label = QLabel(self)
        self.avg_human_label.setText("Средний результат у человека: 400 миллисекунд на мишень.")
        self.avg_human_label.setStyleSheet(f"font-size: {self.text_size}px; color: white;")
        self.avg_human_label.setAlignment(Qt.AlignCenter)
        self.avg_human_label.setGeometry((self.width() - 600) // 2, 60, 600, 50)
        self.avg_human_label.setWordWrap(True)
        self.avg_human_label.hide()

        self.result_image_label = QLabel(self)
        result_image_pixmap = QPixmap('statistiсaim')
        if result_image_pixmap.isNull():
            print("Изображение статистики не найдено")
        self.result_image_label.setPixmap(result_image_pixmap)
        self.result_image_label.setScaledContents(True)
        self.result_image_label.setGeometry((self.width() - 390) // 2, 120, 390, 390)
        self.result_image_label.hide()

        self.show()
        self.start_game()

    def start_game(self):
        self.targets_hit = 0
        self.start_time = time.time()
        self.result_label.hide()
        self.avg_human_label.hide()
        self.result_image_label.hide()
        self.remaining_label.show()
        self.show_next_target()

    def show_next_target(self):
        if self.targets_hit < self.total_targets:
            x = random.randint(0, self.width() - self.target_size)
            y = random.randint(0, self.height() - self.target_size)
            self.target_label.move(x, y)
            self.target_label.show()
            self.remaining_label.setText(f"Осталось: {self.total_targets - self.targets_hit}")
        else:
            self.end_game()

    def mousePressEvent(self, event):
        if self.target_label.isVisible() and self.target_label.geometry().contains(event.pos()):
            self.targets_hit += 1
            self.target_label.hide()
            QTimer.singleShot(50, self.show_next_target)

    def end_game(self):
        end_time = time.time()
        total_time = end_time - self.start_time
        avg_time_per_target = total_time / self.total_targets * 1000

        self.remaining_label.hide()
        self.result_label.setText(f"Среднее время на цель: {avg_time_per_target:.0f} мс")
        self.result_label.show()
        self.avg_human_label.show()
        self.result_image_label.show()

        self.restart_button = QPushButton('Повтор', self)
        self.restart_button.setGeometry((self.width() - 100) // 2, self.height() - 80, 100, 50)
        self.restart_button.setStyleSheet("border-radius: 25px; background-color: lightblue; font-size: 20px;")
        self.restart_button.clicked.connect(self.restart_game)
        self.restart_button.show()

    def resizeEvent(self, event):
        self.remaining_label.setGeometry((self.width() - 200) // 2, 10, 200, 30)
        self.result_label.setGeometry((self.width() - 600) // 2, 10, 600, 50)
        self.avg_human_label.setGeometry((self.width() - 600) // 2, 60, 600, 50)
        self.result_image_label.setGeometry((self.width() - 390) // 2, 120, 390, 390)
        if hasattr(self, 'restart_button'):
            self.restart_button.setGeometry((self.width() - 100) // 2, self.height() - 80, 100, 50)
        super().resizeEvent(event)

    def restart_game(self):
        self.restart_button.hide()
        self.start_game()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    target_size = 150
    text_size = 24
    ex = AimTrainer(target_size=target_size, text_size=text_size)
    sys.exit(app.exec_())
