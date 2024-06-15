import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPixmap, QIntValidator

class NumberMemoryTrainer(QWidget):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.current_number = ''
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Тренажёр: Запоминание чисел')
        self.setFixedSize(450, 450)

        self.background_label = QLabel(self)
        self.background_label.setGeometry(0, 0, 450, 450)
        self.background_label.setPixmap(QPixmap('background.png'))
        self.background_label.setScaledContents(True)

        self.level_counter = QLabel(f'Уровень: {self.level}', self)
        self.level_counter.setAlignment(Qt.AlignCenter)
        self.level_counter.setStyleSheet("font-size: 18px; font-weight: bold;")
        self.level_counter.setGeometry(150, 10, 150, 40)

        self.number_label = QLabel('', self)
        self.number_label.setAlignment(Qt.AlignCenter)
        self.number_label.setStyleSheet("font-size: 24px;")
        self.number_label.setGeometry(125, 70, 200, 100)

        self.input_line = QLineEdit(self)
        self.input_line.setAlignment(Qt.AlignCenter)
        self.input_line.setPlaceholderText('Какое было число?')
        self.input_line.setStyleSheet("font-size: 18px; padding: 10px; background-color: white; border: 2px solid #000000;")
        self.input_line.setGeometry(100, 200, 250, 40)
        self.input_line.setValidator(QIntValidator())
        self.input_line.returnPressed.connect(self.check_input)
        self.input_line.setDisabled(True)

        self.submit_button = QPushButton('Отправить', self)
        self.submit_button.setStyleSheet("font-size: 15px; padding: 10px; background-color: #FFA07A; border: 2px solid #000000;")
        self.submit_button.setGeometry(175, 260, 100, 40)
        self.submit_button.clicked.connect(self.check_input)
        self.submit_button.setDisabled(True)

        self.retry_button = QPushButton('Повторить', self)
        self.retry_button.setStyleSheet("font-size: 15px; padding: 10px; background-color: #FFA07A; border: 2px solid #000000;")
        self.retry_button.setGeometry(175, 260, 100, 40)
        self.retry_button.clicked.connect(self.retry_game)
        self.retry_button.hide()

        self.show()
        self.start_new_level()

    def start_new_level(self):
        self.input_line.clear()
        self.submit_button.setDisabled(True)
        self.input_line.setDisabled(True)
        self.current_number = ''.join([str(random.randint(0, 9)) for _ in range(self.level)])
        self.number_label.setText(self.current_number)
        self.level_counter.setText(f'Уровень: {self.level}')
        QTimer.singleShot(2000, self.clear_number)

    def clear_number(self):
        self.number_label.setText('')
        self.input_line.setDisabled(False)
        self.submit_button.setDisabled(False)
        self.input_line.setFocus()

    def check_input(self):
        user_input = self.input_line.text()
        if user_input == self.current_number:
            self.level += 1
            self.start_new_level()
        else:
            self.game_over()

    def game_over(self):
        self.input_line.hide()
        self.submit_button.hide()
        self.level_counter.setText('')
        self.retry_button.show()

        self.number_label.setText(f'Вы проиграли на уровне: {self.level} \n Средний показатель у человека:20')
        self.number_label.setStyleSheet("font-size: 24px; font-weight: bold; color: white;")
        self.number_label.setGeometry(75, 50, 300, 150)
        self.number_label.setAlignment(Qt.AlignCenter)
        self.number_label.setWordWrap(True)

    def retry_game(self):
        self.level = 1
        self.input_line.show()
        self.submit_button.show()
        self.retry_button.hide()
        self.number_label.setStyleSheet("font-size: 24px;")
        self.number_label.setGeometry(125, 70, 200, 100)
        self.start_new_level()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = NumberMemoryTrainer()
    sys.exit(app.exec_())
