from PyQt5 import QtCore, QtGui, QtWidgets
import random
import sys

class Ui_game(object):
    def setupUi(self, game):
        game.setObjectName("game")
        game.resize(480, 480)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        game.setWindowIcon(icon)

        game.setStyleSheet("QDialog { background-image: url('background.png'); }")

        self.buttons = []

        self.button_style = """
            QPushButton {
                border: 4px solid rgba(0, 0, 0, 0);
                border-radius: 12px;
                background-color: rgb(0, 0, 102);
                opacity: 0.85;
                transition: transform 0.3s ease-out, opacity 0.3s ease-out, background 0.3s ease-out;
            }
            QPushButton:pressed {
                background-color: lightgray;
            }
        """

        self.setup_grid(game, 3)

        self.label = QtWidgets.QLabel(game)
        self.label.setGeometry(QtCore.QRect(150, 20, 180, 30))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(170, 207, 237);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.retry_button = QtWidgets.QPushButton(game)
        self.retry_button.setGeometry(QtCore.QRect(190, 430, 100, 30))
        self.retry_button.setObjectName("retryButton")
        self.retry_button.setText("Повтор")
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

        self.average_label = QtWidgets.QLabel(game)
        self.average_label.setGeometry(QtCore.QRect(50, 260, 380, 30))
        font.setPointSize(12)
        self.average_label.setFont(font)
        self.average_label.setStyleSheet("color: rgb(170, 207, 237);")
        self.average_label.setAlignment(QtCore.Qt.AlignCenter)
        self.average_label.setObjectName("averageLabel")
        self.average_label.hide()

        self.level_label = QtWidgets.QLabel(game)
        self.level_label.setGeometry(QtCore.QRect(50, 220, 380, 30))
        font.setPointSize(14)
        self.level_label.setFont(font)
        self.level_label.setStyleSheet("color: rgb(170, 207, 237);")
        self.level_label.setAlignment(QtCore.Qt.AlignCenter)
        self.level_label.setObjectName("levelLabel")
        self.level_label.hide()

        self.image_label = QtWidgets.QLabel(game)
        self.image_label.setGeometry(QtCore.QRect(40, 80, 400, 130))
        self.image_label.setObjectName("imageLabel")
        self.image_label.hide()

        pixmap = QtGui.QPixmap("sequencestat.PNG")
        self.image_label.setPixmap(pixmap.scaled(400, 450, QtCore.Qt.KeepAspectRatio))

        self.retranslateUi(game)
        QtCore.QMetaObject.connectSlotsByName(game)

        self.game_init()

    def setup_grid(self, game, size):
        for button in self.buttons:
            button.hide()
        self.buttons = []
        self.grid_size = size
        grid_positions = [(x, y) for x in range(size) for y in range(size)]
        button_size = int(360 / size)
        offset_x = (480 - button_size * size) // 2
        offset_y = 80

        for pos in grid_positions:
            button = QtWidgets.QPushButton(game)
            button.setGeometry(QtCore.QRect(offset_x + pos[0] * button_size, offset_y + pos[1] * button_size, button_size, button_size))
            button.setObjectName(f"pushButton_{pos[0]}_{pos[1]}")
            button.setStyleSheet(self.button_style)
            button.clicked.connect(self.make_button_handler(pos[0] * size + pos[1] + 1))
            button.hide()
            self.buttons.append(button)
        for button in self.buttons:
            button.show()

    def retranslateUi(self, game):
        _translate = QtCore.QCoreApplication.translate
        game.setWindowTitle(_translate("game", "Тренажёр: Запоминание порядка"))

    def game_init(self):
        self.level = 1
        self.sequence = []
        self.player_sequence = []
        self.is_displaying_sequence = False
        self.average_label.hide()
        self.level_label.hide()
        self.image_label.hide()
        self.label.show()
        for button in self.buttons:
            button.show()
        self.retry_button.hide()
        self.next_level()

    def next_level(self):
        self.sequence.append(random.randint(1, 9))
        self.player_sequence = []
        self.label.setText(f"Уровень: {self.level}")
        QtCore.QTimer.singleShot(1000, self.show_sequence)

    def show_sequence(self):
        self.is_displaying_sequence = True
        self.disable_buttons()
        self.highlight_index = 0
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.highlight_next_button)
        self.timer.start(1000)

    def highlight_next_button(self):
        if self.highlight_index > 0:
            self.fade_out_button(self.buttons[self.sequence[self.highlight_index - 1] - 1])
        if self.highlight_index < len(self.sequence):
            button = self.buttons[self.sequence[self.highlight_index] - 1]
            self.fade_in_button(button)
            self.highlight_index += 1
        else:
            self.timer.stop()
            self.is_displaying_sequence = False
            self.enable_buttons()
            button = self.buttons[self.sequence[-1] - 1]
            effect = QtWidgets.QGraphicsOpacityEffect(button)
            button.setGraphicsEffect(effect)
            animation = QtCore.QPropertyAnimation(effect, b"opacity")
            animation.setDuration(500)
            animation.setStartValue(1)
            animation.setEndValue(0.15)
            animation.finished.connect(lambda: self.reset_button_color(button))
            animation.start()

    def fade_in_button(self, button):
        effect = QtWidgets.QGraphicsOpacityEffect(button)
        button.setGraphicsEffect(effect)
        animation = QtCore.QPropertyAnimation(effect, b"opacity")
        animation.setDuration(500)
        animation.setStartValue(0.15)
        animation.setEndValue(1)
        animation.start()
        self.animation = animation

    def fade_out_button(self, button):
        effect = QtWidgets.QGraphicsOpacityEffect(button)
        button.setGraphicsEffect(effect)
        animation = QtCore.QPropertyAnimation(effect, b"opacity")
        animation.setDuration(500)
        animation.setStartValue(1)
        animation.setEndValue(0.15)
        animation.finished.connect(lambda: self.reset_button_color(button))
        animation.start()
        self.animation = animation

    def reset_button_color(self, button):
        button.setStyleSheet(self.button_style)

    def make_button_handler(self, button_id):
        def handler():
            if self.is_displaying_sequence:
                self.show_game_over_message()
                return

            self.player_sequence.append(button_id)
            if self.player_sequence == self.sequence:
                self.level += 1
                self.next_level()
            elif len(self.player_sequence) == len(self.sequence):
                self.show_game_over_message()
        return handler

    def disable_buttons(self):
        for button in self.buttons:
            button.setEnabled(False)

    def enable_buttons(self):
        for button in self.buttons:
            button.setEnabled(True)

    def retry_game(self):
        self.game_init()
        self.label.setText(f"Уровень: {self.level}")
        self.retry_button.hide()

    def show_game_over_message(self):
        self.level_label.setText(f"Вы закончили на уровне: {self.level}")
        self.average_label.setText("Средний показатель у человека 8-9 уровень")
        self.label.hide()
        for button in self.buttons:
            button.hide()
        self.level_label.setGeometry(QtCore.QRect(50, 20, 380, 30))
        self.average_label.setGeometry(QtCore.QRect(50, 60, 380, 30))
        self.image_label.setGeometry(QtCore.QRect(40, 100, 400, 280))
        self.level_label.show()
        self.average_label.show()
        self.image_label.show()
        self.retry_button.setGeometry(QtCore.QRect(190, 410, 100, 30))
        self.retry_button.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    game = QtWidgets.QDialog()
    ui = Ui_game()
    ui.setupUi(game)
    game.show()
    sys.exit(app.exec_())
