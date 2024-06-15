from PyQt5 import QtWidgets, QtGui, QtCore
import sys
import random


class VocabularyTrainerApp(QtWidgets.QWidget):
    def __init__(self, words):
        super().__init__()
        self.words = words
        self.seen_words = set()
        self.current_word = ""
        self.score = 0
        self.steps_since_last_seen = 0

        self.default_font = "Arial"
        self.default_font_size = 30

        self.score_font = "MS Serif"
        self.score_font_size = 20

        self.game_over_font_size = 20

        self.button_width = 100
        self.button_height = 50

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Тренажёр: Запоминание слов")
        self.setGeometry(100, 100, 600, 600)
        self.setStyleSheet("background-color: #3498db;")

        self.center()

        layout = QtWidgets.QVBoxLayout()

        self.score_label = QtWidgets.QLabel(f"Уровень | {self.score}", self)
        self.apply_custom_style(self.score_label, self.score_font, self.score_font_size)

        self.place_score_label()

        self.word_label = QtWidgets.QLabel("", self)
        self.word_label.setWordWrap(True)
        self.word_label.setAlignment(QtCore.Qt.AlignCenter)
        self.apply_custom_style(self.word_label, self.default_font, self.default_font_size)
        self.word_label.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)

        self.place_word_label()

        self.setup_buttons(self.button_width, self.button_height)
        self.place_buttons()

        self.setLayout(layout)

        self.setup_game_over_elements()

        self.show_new_word()

    def center(self):
        qr = self.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def setup_buttons(self, width, height):
        self.seen_button = QtWidgets.QPushButton("БЫЛО", self)
        self.seen_button.setStyleSheet("""
            QPushButton {
                border: 4px solid rgba(0, 0, 0, 0);
                border-radius: 12px;
                background-color: #f1c40f;
                font-size: 40px;
                padding: 10px;
                opacity: 0.85;
                transition: transform 0.3s ease-out, opacity 0.3s ease-out, background 0.3s ease-out;
            }
            QPushButton:pressed {
                background-color: lightgray;
            }
        """)
        self.seen_button.setFixedSize(width, height)
        self.seen_button.clicked.connect(self.seen_clicked)

        self.new_button = QtWidgets.QPushButton("НОВОЕ", self)
        self.new_button.setStyleSheet("""
            QPushButton {
                border: 4px solid rgba(0, 0, 0, 0);
                border-radius: 12px;
                background-color: #f1c40f;
                font-size: 40px;
                padding: 10px;
                opacity: 0.85;
                transition: transform 0.3s ease-out, opacity 0.3s ease-out, background 0.3s ease-out;
            }
            QPushButton:pressed {
                background-color: lightgray;
            }
        """)
        self.new_button.setFixedSize(width, height)
        self.new_button.clicked.connect(self.new_clicked)

    def place_buttons(self):
        self.seen_button.setGeometry(50, 300, self.button_width, self.button_height)
        self.new_button.setGeometry(350, 300, self.button_width, self.button_height)

    def place_word_label(self):
        self.word_label.setGeometry(50, 100, 500, 150)

    def place_score_label(self):
        self.score_label.setGeometry(450, 20, 100, 30)

    def setup_game_over_elements(self):
        self.average_label = QtWidgets.QLabel("Средний показатель у человека: 9-10 уровень ", self)
        self.average_label.setWordWrap(True)
        self.average_label.setGeometry(QtCore.QRect(50, 50, 500, 60))
        self.apply_custom_style(self.average_label, self.default_font, self.game_over_font_size)
        self.average_label.setAlignment(QtCore.Qt.AlignCenter)
        self.average_label.hide()

        self.level_label = QtWidgets.QLabel(self)
        self.level_label.setWordWrap(True)
        self.level_label.setGeometry(QtCore.QRect(50, 110, 500, 60))
        self.apply_custom_style(self.level_label, self.default_font, self.game_over_font_size)
        self.level_label.setAlignment(QtCore.Qt.AlignCenter)
        self.level_label.hide()

        self.image_label = QtWidgets.QLabel(self)
        self.image_label.setGeometry(QtCore.QRect(50, 180, 500, 300))
        pixmap = QtGui.QPixmap("verbalstat.png")
        self.image_label.setPixmap(pixmap.scaled(500, 300, QtCore.Qt.KeepAspectRatio))
        self.image_label.setAlignment(QtCore.Qt.AlignCenter)
        self.image_label.hide()

        self.retry_button = QtWidgets.QPushButton("Повтор", self)
        self.retry_button.setGeometry(QtCore.QRect(250, 500, 100, 30))
        self.retry_button.setStyleSheet("""
            QPushButton {
                background-color: rgb(0, 102, 204);
                color: white;
                border-radius: 12px;
            }
            QPushButton:pressed {
                background-color: lightgray;
            }
        """)
        self.retry_button.clicked.connect(self.retry_game)
        self.retry_button.hide()

    def show_new_word(self):
        if self.steps_since_last_seen >= random.randint(3, 5) and self.seen_words:
            self.current_word = random.choice(list(self.seen_words))
            self.steps_since_last_seen = 0
        else:
            self.current_word = random.choice(self.words)
            self.steps_since_last_seen += 1
        self.word_label.setText(self.current_word)

    def seen_clicked(self):
        if self.current_word in self.seen_words:
            self.score += 1
            self.update_score()
            self.show_new_word()
        else:
            self.game_over()

    def new_clicked(self):
        if self.current_word not in self.seen_words:
            self.seen_words.add(self.current_word)
            self.score += 1
            self.update_score()
            self.show_new_word()
        else:
            self.game_over()

    def update_score(self):
        self.score_label.setText(f"Уровень | {self.score}")

    def game_over(self):
        self.word_label.hide()
        self.seen_button.hide()
        self.new_button.hide()
        self.score_label.hide()

        self.level_label.setText(f"Вы закончили на уровне: {self.score}")
        self.level_label.show()
        self.average_label.show()
        self.image_label.show()
        self.retry_button.show()

    def retry_game(self):
        self.seen_words.clear()
        self.score = 0
        self.steps_since_last_seen = 0
        self.update_score()
        self.word_label.show()
        self.seen_button.show()
        self.new_button.show()
        self.score_label.show()
        self.average_label.hide()
        self.level_label.hide()
        self.image_label.hide()
        self.retry_button.hide()
        self.show_new_word()

    def apply_custom_style(self, widget, font, size):
        widget.setStyleSheet(f"font-size: {size}px; font-family: {font};")

    def adjust_font_and_size(self, font=None, size=None):
        if font:
            self.default_font = font
        if size:
            self.default_font_size = size

        self.apply_custom_style(self.word_label, self.default_font, self.default_font_size)
        self.apply_custom_style(self.average_label, self.default_font, self.game_over_font_size)
        self.apply_custom_style(self.level_label, self.default_font, self.game_over_font_size)

    def adjust_button_size(self, width=None, height=None):
        if width:
            self.button_width = width
        if height:
            self.button_height = height

        self.setup_buttons(self.button_width, self.button_height)
        self.place_buttons()


def load_words(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        words = file.read().splitlines()
    return words


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    words = load_words("complex_words.txt")
    window = VocabularyTrainerApp(words)
    window.adjust_font_and_size(size=50)
    window.adjust_button_size(width=200, height=100)
    window.show()
    sys.exit(app.exec_())
