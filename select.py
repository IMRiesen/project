import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import os

class Ui_game(object):
    def setupUi(self, game):
        game.setObjectName("select")
        game.resize(600, 510)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        game.setWindowIcon(icon)
        game.setStyleSheet("background-color: rgb(148, 255, 232)")

        self.label = QtWidgets.QLabel(game)
        self.label.setGeometry(QtCore.QRect(50, 20, 500, 51))
        font = QtGui.QFont()
        font.setFamily("Script MT Bold")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setStyleSheet("color:rgb(0, 0, 0)")
        self.label.setObjectName("label")

        button_width = 180
        button_height = 60
        margin_x = (600 - 2 * button_width) // 3
        margin_y = (510 - 4 * button_height - 60) // 5

        self.reaction_button = QtWidgets.QPushButton(game)
        self.reaction_button.setGeometry(QtCore.QRect(margin_x, margin_y + 80, button_width, button_height))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Heavy")
        font.setPointSize(12)
        self.reaction_button.setFont(font)
        self.reaction_button.setStyleSheet("background-color: rgb(0, 255, 127);")
        self.reaction_button.setObjectName("reaction_button")
        self.reaction_button.clicked.connect(self.open_reaction)

        self.sequence_memory_button = QtWidgets.QPushButton(game)
        self.sequence_memory_button.setGeometry(QtCore.QRect(2 * margin_x + button_width, margin_y + 80, button_width, button_height))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Heavy")
        font.setPointSize(12)
        self.sequence_memory_button.setFont(font)
        self.sequence_memory_button.setStyleSheet("background-color: rgb(0, 255, 127);")
        self.sequence_memory_button.setObjectName("sequence_memory_button")
        self.sequence_memory_button.clicked.connect(self.open_sequence_memory)

        self.aim_trainer_button = QtWidgets.QPushButton(game)
        self.aim_trainer_button.setGeometry(QtCore.QRect(margin_x, 2 * margin_y + 80 + button_height, button_width, button_height))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Heavy")
        font.setPointSize(12)
        self.aim_trainer_button.setFont(font)
        self.aim_trainer_button.setStyleSheet("background-color: rgb(0, 255, 127);")
        self.aim_trainer_button.setObjectName("aim_trainer_button")
        self.aim_trainer_button.clicked.connect(self.open_aim_trainer)

        self.visual_memory_button = QtWidgets.QPushButton(game)
        self.visual_memory_button.setGeometry(QtCore.QRect(2 * margin_x + button_width, 2 * margin_y + 80 + button_height, button_width, button_height))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Heavy")
        font.setPointSize(12)
        self.visual_memory_button.setFont(font)
        self.visual_memory_button.setStyleSheet("background-color: rgb(0, 255, 127);")
        self.visual_memory_button.setObjectName("visual_memory_button")
        self.visual_memory_button.clicked.connect(self.open_visual_memory)

        self.number_memory_button = QtWidgets.QPushButton(game)
        self.number_memory_button.setGeometry(QtCore.QRect(margin_x, 3 * margin_y + 80 + 2 * button_height, button_width, button_height))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Heavy")
        font.setPointSize(12)
        self.number_memory_button.setFont(font)
        self.number_memory_button.setStyleSheet("background-color: rgb(0, 255, 127);")
        self.number_memory_button.setObjectName("number_memory_button")
        self.number_memory_button.clicked.connect(self.open_number_memory)

        self.verbal_button = QtWidgets.QPushButton(game)
        self.verbal_button.setGeometry(QtCore.QRect(2 * margin_x + button_width, 3 * margin_y + 80 + 2 * button_height, button_width, button_height))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Heavy")
        font.setPointSize(12)
        self.verbal_button.setFont(font)
        self.verbal_button.setStyleSheet("background-color: rgb(0, 255, 127);")
        self.verbal_button.setObjectName("verbal_button")
        self.verbal_button.clicked.connect(self.open_verbal)

        self.typing_test_button = QtWidgets.QPushButton(game)
        self.typing_test_button.setGeometry(QtCore.QRect((600 - button_width) // 2, 4 * margin_y + 80 + 3 * button_height, button_width, button_height))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Heavy")
        font.setPointSize(12)
        self.typing_test_button.setFont(font)
        self.typing_test_button.setStyleSheet("background-color: rgb(0, 255, 127);")
        self.typing_test_button.setObjectName("typing_test_button")
        self.typing_test_button.clicked.connect(self.open_typing_test)

        self.retranslateUi(game)
        QtCore.QMetaObject.connectSlotsByName(game)

    def retranslateUi(self, game):
        _translate = QtCore.QCoreApplication.translate
        game.setWindowTitle(_translate("game", "Выбор теста"))
        self.label.setText(_translate("game", "Выберите тест для тренировки"))

        self.reaction_button.setText(_translate("game", "Время реакции"))
        self.sequence_memory_button.setText(_translate("game", "Запоминание порядка"))
        self.aim_trainer_button.setText(_translate("game", "Тренировка точности"))
        self.visual_memory_button.setText(_translate("game", "Визуальная память"))
        self.number_memory_button.setText(_translate("game", "Запоминание чисел"))
        self.verbal_button.setText(_translate("game", "Запоминание слов"))
        self.typing_test_button.setText(_translate("game", "Скорость печати"))

    def open_reaction(self):
        os.system('python reaction.py')

    def open_sequence_memory(self):
        os.system('python sequencememory.py')

    def open_aim_trainer(self):
        os.system('python aimtrainer.py')

    def open_visual_memory(self):
        os.system('python visualmemory.py')

    def open_number_memory(self):
        os.system('python numbermemory.py')

    def open_verbal(self):
        os.system('python verbal.py')

    def open_typing_test(self):
        os.system('python typingtest.py')

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    game = QtWidgets.QDialog()
    ui = Ui_game()
    ui.setupUi(game)
    game.show()
    sys.exit(app.exec_())
