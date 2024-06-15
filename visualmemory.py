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
        self.clicked_button_style = """
            QPushButton {
                border: 4px solid rgba(0, 0, 0, 0);
                border-radius: 12px;
                background-color: rgb(255, 255, 255);
                opacity: 1;
                transition: transform 0.3s ease-out, opacity 0.3s ease-out, background 0.3s ease-out;
            }
            QPushButton:pressed {
                background-color: lightgray;
            }
        """
        self.dimmed_button_style = """
            QPushButton {
                border: 4px solid rgba(0, 0, 0, 0);
                border-radius: 12px;
                background-color: rgb(0, 0, 102);
                opacity: 0.5;
                transition: transform 0.3s ease-out, opacity 0.3s ease-out, background 0.3s ease-out;
            }
            QPushButton:pressed {
                background-color: lightgray;
            }
        """
        self.buttons = []

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
        self.retry_button.setGeometry(QtCore.QRect(190, 420, 100, 30))
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
        self.average_label.setGeometry(QtCore.QRect(40, 230, 400, 30))
        font.setPointSize(12)
        self.average_label.setFont(font)
        self.average_label.setStyleSheet("color: rgb(170, 207, 237);")
        self.average_label.setAlignment(QtCore.Qt.AlignCenter)
        self.average_label.setObjectName("averageLabel")
        self.average_label.hide()

        self.level_label = QtWidgets.QLabel(game)
        self.level_label.setGeometry(QtCore.QRect(40, 190, 400, 30))
        font.setPointSize(14)
        self.level_label.setFont(font)
        self.level_label.setStyleSheet("color: rgb(170, 207, 237);")
        self.level_label.setAlignment(QtCore.Qt.AlignCenter)
        self.level_label.setObjectName("levelLabel")
        self.level_label.hide()

        self.image_label = QtWidgets.QLabel(game)
        self.image_label.setGeometry(QtCore.QRect(80, 70, 320, 130))
        self.image_label.setObjectName("imageLabel")
        self.image_label.hide()

        pixmap = QtGui.QPixmap("visualstat.PNG")
        self.image_label.setPixmap(pixmap.scaled(400, 300, QtCore.Qt.KeepAspectRatio))

        self.parent = game

        self.retranslateUi(game)
        QtCore.QMetaObject.connectSlotsByName(game)

        self.game_init()

    def retranslateUi(self, game):
        _translate = QtCore.QCoreApplication.translate
        game.setWindowTitle(_translate("game", "Тренажёр: Визуальная память"))
        self.label.setText(_translate("game", "Уровень: 1"))

    def game_init(self):
        self.level = 1
        self.sequence = []
        self.player_sequence = []
        self.is_displaying_sequence = False
        self.grid_size = 3
        self.sequence_correctly_entered = False
        self.setup_grid(self.grid_size)
        self.average_label.hide()
        self.level_label.hide()
        self.image_label.hide()
        self.label.show()
        self.retry_button.hide()
        self.disable_buttons()
        self.next_level()

    def setup_grid(self, size):
        for button in self.buttons:
            button.hide()
        self.buttons = []
        self.grid_size = size
        grid_positions = [(x, y) for x in range(size) for y in range(size)]
        button_size = int(360 / size)
        offset_x = (480 - button_size * size) // 2
        offset_y = 80

        for pos in grid_positions:
            button = QtWidgets.QPushButton(self.parent)
            button.setGeometry(QtCore.QRect(offset_x + pos[0] * button_size, offset_y + pos[1] * button_size, button_size, button_size))
            button.setObjectName(f"pushButton_{pos[0]}_{pos[1]}")
            button.setStyleSheet(self.button_style)
            button.clicked.connect(self.make_button_handler(pos))
            button.hide()
            self.buttons.append(button)
        for button in self.buttons:
            button.show()

    def next_level(self):
        if self.level % 3 == 1 and self.level != 1:
            self.grid_size += 1
            self.setup_grid(self.grid_size)
        self.sequence = random.sample(range(self.grid_size * self.grid_size), min(3 + self.level - 1, self.grid_size * self.grid_size))
        self.player_sequence = []
        self.sequence_correctly_entered = False
        self.label.setText(f"Уровень: {self.level}")
        QtCore.QTimer.singleShot(1000, self.show_sequence)

    def show_sequence(self):
        self.is_displaying_sequence = True
        self.disable_buttons()
        self.fade_in_buttons()

    def fade_in_buttons(self):
        self.fade_in_group = QtCore.QParallelAnimationGroup()
        for idx in self.sequence:
            button = self.buttons[idx]
            button.setStyleSheet(self.clicked_button_style)
            self.fade_in_group.addAnimation(self.fade_in_button(button))
        self.fade_in_group.finished.connect(self.fade_out_sequence)
        self.fade_in_group.start()

    def fade_in_button(self, button):
        effect = QtWidgets.QGraphicsOpacityEffect(button)
        button.setGraphicsEffect(effect)
        animation = QtCore.QPropertyAnimation(effect, b"opacity")
        animation.setDuration(500)
        animation.setStartValue(0.15)
        animation.setEndValue(1)
        return animation

    def fade_out_sequence(self):
        self.fade_out_group = QtCore.QParallelAnimationGroup()
        for idx in self.sequence:
            button = self.buttons[idx]
            self.fade_out_group.addAnimation(self.fade_out_button(button))
        self.fade_out_group.finished.connect(self.on_sequence_display_finished)
        self.fade_out_group.start()

    def fade_out_button(self, button):
        effect = button.graphicsEffect()
        animation = QtCore.QPropertyAnimation(effect, b"opacity")
        animation.setDuration(500)
        animation.setStartValue(1)
        animation.setEndValue(0.15)
        return animation

    def on_sequence_display_finished(self):
        self.is_displaying_sequence = False
        self.reset_sequence_colors()
        self.set_dimmed_buttons()
        self.enable_buttons()

    def reset_sequence_colors(self):
        for idx in self.sequence:
            button = self.buttons[idx]
            button.setStyleSheet(self.button_style)
            button.setGraphicsEffect(None)

    def set_dimmed_buttons(self):
        for button in self.buttons:
            button.setStyleSheet(self.dimmed_button_style)

    def make_button_handler(self, button_pos):
        def handler():
            if self.is_displaying_sequence or self.sequence_correctly_entered:
                return

            button_idx = button_pos[0] * self.grid_size + button_pos[1]
            button = self.buttons[button_idx]

            if button_idx in self.sequence and button_idx not in self.player_sequence:
                self.player_sequence.append(button_idx)
                button.setStyleSheet(self.clicked_button_style)

            elif button_idx not in self.sequence:
                self.show_game_over_message()
                return

            if sorted(self.player_sequence) == sorted(self.sequence):
                self.sequence_correctly_entered = True
                self.disable_buttons()
                self.level += 1
                self.clear_highlights()
                QtCore.QTimer.singleShot(1000, self.next_level)
        return handler

    def clear_highlights(self):
        for button in self.buttons:
            button.setStyleSheet(self.button_style)

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
        self.average_label.setText("Средний показатель у человека: 8-9 уровень")
        self.label.hide()
        for button in self.buttons:
            button.hide()
        self.level_label.setGeometry(QtCore.QRect(50, 20, 400, 30))
        self.average_label.setGeometry(QtCore.QRect(40, 60, 400, 30))
        self.image_label.setGeometry(QtCore.QRect(80, 100, 320, 280))
        self.level_label.show()
        self.average_label.show()
        self.image_label.show()
        self.retry_button.setGeometry(QtCore.QRect(190, 400, 100, 30))
        self.retry_button.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    game = QtWidgets.QDialog()
    ui = Ui_game()
    ui.setupUi(game)
    game.show()
    sys.exit(app.exec_())
