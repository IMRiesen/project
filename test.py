import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from select import Ui_game  # Импортируем класс из select.py

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        self.main_widget = QtWidgets.QStackedWidget(Dialog)
        self.main_widget.setGeometry(QtCore.QRect(0, 0, 600, 510))

        self.main_menu = QtWidgets.QWidget()
        self.setup_main_menu(self.main_menu)
        self.main_widget.addWidget(self.main_menu)

        self.select_game_widget = QtWidgets.QWidget()
        self.select_game_ui = Ui_game()
        self.select_game_ui.setupUi(self.select_game_widget)
        self.main_widget.addWidget(self.select_game_widget)

        self.main_widget.setCurrentWidget(self.main_menu)

    def setup_main_menu(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(600, 510)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("иконка.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet("background-color: rgb(148, 255, 232)")

        self.Startgame = QtWidgets.QPushButton(Dialog)
        self.Startgame.setGeometry(QtCore.QRect(240, 220, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Heavy")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.Startgame.setFont(font)
        self.Startgame.setStyleSheet("background-color: rgb(0, 255, 127)")
        self.Startgame.setIconSize(QtCore.QSize(16, 16))
        self.Startgame.setDefault(False)
        self.Startgame.setFlat(False)
        self.Startgame.setObjectName("Startgame")

        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(70, 90, 481, 31))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Heavy")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(0, 0, 0)")
        self.label.setObjectName("label")

        self.finishgame = QtWidgets.QPushButton(Dialog)
        self.finishgame.setGeometry(QtCore.QRect(240, 280, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Heavy")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.finishgame.setFont(font)
        self.finishgame.setStyleSheet("background-color: rgb(0, 255, 127)")
        self.finishgame.setIconSize(QtCore.QSize(16, 16))
        self.finishgame.setDefault(False)
        self.finishgame.setFlat(False)
        self.finishgame.setObjectName("finishgame")

        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(550, 470, 41, 31))
        self.pushButton.setStyleSheet("    border-radius:  10px;\n"
                                      "    background-color:  rgb(126, 255, 163);\n"
                                      "    color:  rgb(255, 255, 255);\n"
                                      "    font-size:  33px;")
        self.pushButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("музыка.png"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setCheckable(False)
        self.pushButton.setChecked(False)
        self.pushButton.setObjectName("pushButton")

        def change_color():
            if self.pushButton.styleSheet() == ("    border-radius:  10px;\n"
                                                "    background-color:  rgb(255, 52, 62);\n"
                                                "    color:  rgb(255, 255, 255);\n"
                                                "    font-size:  33px;"):
                self.pushButton.setStyleSheet("    border-radius:  10px;\n"
                                              "    background-color:  rgb(126, 255, 163);\n"
                                              "    color:  rgb(255, 255, 255);\n"
                                              "    font-size:  33px;")
            else:
                self.pushButton.setStyleSheet("    border-radius:  10px;\n"
                                              "    background-color:  rgb(255, 52, 62);\n"
                                              "    color:  rgb(255, 255, 255);\n"
                                              "    font-size:  33px;")

        self.pushButton.clicked.connect(change_color)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setGeometry(10, 120, 590, 90)
        self.text = 'Приложение для тренировки и развития когнитивных способностей'
        self.label.setWordWrap(True)
        self.index = 0
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.updateText)
        self.timer.start(100)
        font.setFamily("Franklin Gothic Heavy")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(0,0,0)")
        self.label.setObjectName("label")

        self.Startgame.clicked.connect(self.open_select_game)  # Добавляем обработчик для кнопки "Начать"

    def updateText(self):
        self.label.setText(self.text)
        self.timer.stop()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Приложение для тренировки и развития когнитивных способностей"))
        self.Startgame.setText(_translate("Dialog", "Начать"))
        self.finishgame.setText(_translate("Dialog", "Выйти"))

    def close_application(self):
        reply = QtWidgets.QMessageBox()
        reply.setWindowIcon(QtGui.QIcon('иконка.png'))
        reply.setWindowTitle('Подтверждение')
        reply.setText("Вы уверены, что хотите покинуть приложение?")
        reply.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        reply.button(QtWidgets.QMessageBox.Yes).setText('Да')
        reply.button(QtWidgets.QMessageBox.No).setText('Нет')

        if reply.exec() == QtWidgets.QMessageBox.Yes:
            sys.exit()

    def open_select_game(self):
        self.main_widget.setCurrentWidget(self.select_game_widget)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    ui.timer.start(100)
    Dialog.show()

    ui.finishgame.clicked.connect(ui.close_application)

    sys.exit(app.exec_())

# select.py

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import os

class Ui_game(object):
    def setupUi(self, game):
        game.setObjectName("select")
        game.resize(600, 510)  # Оставляем размер окна без изменений
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
        button_height = 60  # Уменьшаем высоту кнопок
        margin_x = (600 - 2 * button_width) // 3
        margin_y = (510 - 4 * button_height - 60) // 5  # Учитываем место для заголовка

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
        self.sequence_memory_button.setFont(font)
        self.sequence_memory_button.setStyleSheet("background-color: rgb(0, 255, 127);")
        self.sequence_memory_button.setObjectName("sequence_memory_button")
        self.sequence_memory_button.clicked.connect(self.open_sequence_memory)

        self.verbal_memory_button = QtWidgets.QPushButton(game)
        self.verbal_memory_button.setGeometry(QtCore.QRect(margin_x, 2 * margin_y + button_height + 80, button_width, button_height))
        self.verbal_memory_button.setFont(font)
        self.verbal_memory_button.setStyleSheet("background-color: rgb(0, 255, 127);")
        self.verbal_memory_button.setObjectName("verbal_memory_button")
        self.verbal_memory_button.clicked.connect(self.open_verbal_memory)

        self.number_memory_button = QtWidgets.QPushButton(game)
        self.number_memory_button.setGeometry(QtCore.QRect(2 * margin_x + button_width, 2 * margin_y + button_height + 80, button_width, button_height))
        self.number_memory_button.setFont(font)
        self.number_memory_button.setStyleSheet("background-color: rgb(0, 255, 127);")
        self.number_memory_button.setObjectName("number_memory_button")
        self.number_memory_button.clicked.connect(self.open_number_memory)

        self.back_to_menu = QtWidgets.QPushButton(game)
        self.back_to_menu.setGeometry(QtCore.QRect(margin_x, 3 * margin_y + 2 * button_height + 80, button_width, button_height))
        self.back_to_menu.setFont(font)
        self.back_to_menu.setStyleSheet("background-color: rgb(0, 255, 127);")
        self.back_to_menu.setObjectName("back_to_menu")
        self.back_to_menu.clicked.connect(self.back_to_main_menu)

        self.retranslateUi(game)
        QtCore.QMetaObject.connectSlotsByName(game)

    def retranslateUi(self, game):
        _translate = QtCore.QCoreApplication.translate
        game.setWindowTitle(_translate("select", "Выбор игры"))
        self.label.setText(_translate("select", "Выберите игру для тренировки"))
        self.reaction_button.setText(_translate("select", "Реакция"))
        self.sequence_memory_button.setText(_translate("select", "Запоминание \n"
                                                            "последовательности"))
        self.verbal_memory_button.setText(_translate("select", "Вербальная \n"
                                                           "память"))
        self.number_memory_button.setText(_translate("select", "Цифровая \n"
                                                            "память"))
        self.back_to_menu.setText(_translate("select", "Назад"))

    def open_reaction(self):
        self.open_program("main reaction.py")

    def open_sequence_memory(self):
        self.open_program("main sequence memory.py")

    def open_verbal_memory(self):
        self.open_program("main verbal memory.py")

    def open_number_memory(self):
        self.open_program("main number memory.py")

    def open_program(self, program_name):
        python_interpreter = sys.executable
        script_path = os.path.join(os.getcwd(), program_name)
        os.system(f'"{python_interpreter}" "{script_path}"')

    def back_to_main_menu(self):
        self.main_widget.setCurrentWidget(self.main_menu)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    select = QtWidgets.QWidget()
    ui = Ui_game()
    ui.setupUi(select)
    select.show()
    sys.exit(app.exec_())
