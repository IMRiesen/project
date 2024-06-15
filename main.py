import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from select import Ui_game

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

        self.Startgame.clicked.connect(self.open_select_game)

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
