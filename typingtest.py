import sys
import time
import random
import re
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QLabel, QVBoxLayout, QWidget
from PyQt5.QtGui import QTextCharFormat, QFont, QPixmap, QKeySequence
from PyQt5.QtCore import Qt

def read_text_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    if len(text) < 300:
        raise ValueError("Текст слишком короткий. Требуется минимум 300 символов.")

    text = ' '.join(text.split())

    pattern = re.compile(r'[А-ЯЁ]')
    match_indices = [match.start() for match in re.finditer(pattern, text)]
    if not match_indices:
        raise ValueError("Текст не содержит заглавных русских букв.")

    start_index = random.choice([index for index in match_indices if index <= len(text) - 300])
    end_index = text.find('.', start_index + 300) + 1
    if end_index == 0:
        end_index = len(text)
    text = text[start_index:end_index]

    return text


class TypingTest(QMainWindow):
    def __init__(self, text, background_image_path, width=800, height=600, text_font_size=16, input_font_size=16):
        super().__init__()
        self.text_to_type = text
        self.text_index = 0
        self.start_time = None
        self.end_time = None
        self.background_image_path = background_image_path
        self.window_width = width
        self.window_height = height
        self.text_font_size = text_font_size
        self.input_font_size = input_font_size
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Тренажёр: Скорость печати')
        self.adjust_window_size()
        self.center_window()

        self.setStyleSheet(
            f"QMainWindow {{background-image: url({self.background_image_path}); background-repeat: no-repeat; background-position: center;}}")

        self.text_edit = NoCopyTextEdit(self)
        self.text_edit.setFont(QFont('Arial', self.text_font_size))
        self.text_edit.setReadOnly(True)
        self.text_edit.setText(self.text_to_type)
        self.text_edit.setStyleSheet("QTextEdit {background: transparent;}")

        self.label = QLabel('Начинайте вводить текст в окне ниже:', self)
        self.label.setFont(QFont('Arial', 16))
        self.label.setStyleSheet("QLabel {background: transparent;}")

        self.input_edit = NoCopyTextEdit(self)
        self.input_edit.setFont(QFont('Arial', self.input_font_size))
        self.input_edit.textChanged.connect(self.on_text_changed)
        self.input_edit.setStyleSheet("QTextEdit {background: transparent;}")

        layout = QVBoxLayout()
        layout.addWidget(self.text_edit)
        layout.addWidget(self.label)
        layout.addWidget(self.input_edit)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

    def adjust_window_size(self):
        lines = self.text_to_type.count('\n') + 1
        avg_characters_per_line = len(self.text_to_type) // lines
        char_width = 8
        char_height = 20
        margin = 100

        width = max(self.window_width, min(1200, avg_characters_per_line * char_width + margin))
        height = max(self.window_height, lines * char_height + margin)

        self.setGeometry(100, 100, width, height)

    def center_window(self):
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def on_text_changed(self):
        try:
            if self.start_time is None:
                self.start_time = time.time()

            typed_text = self.input_edit.toPlainText()
            cursor_position = len(typed_text)

            if cursor_position == len(self.text_to_type):
                self.end_time = time.time()
                self.show_statistics()
                return

            format = QTextCharFormat()
            format.setFont(QFont('Arial', self.input_font_size))

            self.input_edit.blockSignals(True)
            cursor = self.input_edit.textCursor()
            cursor.select(cursor.Document)
            cursor.setCharFormat(format)
            cursor.clearSelection()

            correct_text = self.text_to_type[:cursor_position]
            if typed_text == correct_text:
                format.setBackground(Qt.green)
            else:
                format.setBackground(Qt.red)

            cursor.select(cursor.Document)
            cursor.setCharFormat(format)
            cursor.clearSelection()
            self.input_edit.blockSignals(False)
        except Exception as e:
            print(f"Ошибка: {e}")

    def show_statistics(self):
        typing_time = self.end_time - self.start_time
        words_typed = len(self.text_to_type) / 5
        wpm = words_typed / (typing_time / 60)

        self.text_edit.hide()
        self.label.hide()
        self.input_edit.hide()

        result_label = QLabel(f"Ваш результат: {wpm:.2f} слов в минуту", self)
        result_label.setFont(QFont('Arial', 16))
        result_label.setStyleSheet("QLabel {background: transparent;}")
        result_label.setAlignment(Qt.AlignCenter)

        avg_result_label = QLabel("Средний показатель у человека: 40 символов в минуту", self)
        avg_result_label.setFont(QFont('Arial', 16))
        avg_result_label.setStyleSheet("QLabel {background: transparent;}")
        avg_result_label.setAlignment(Qt.AlignCenter)

        image_label = QLabel(self)
        image_label.setPixmap(QPixmap('typingstat.PNG'))
        image_label.setAlignment(Qt.AlignCenter)

        layout = QVBoxLayout()
        layout.addWidget(result_label)
        layout.addWidget(avg_result_label)
        layout.addWidget(image_label)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)


class NoCopyTextEdit(QTextEdit):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def keyPressEvent(self, event):
        if event.matches(QKeySequence.Copy) or event.matches(QKeySequence.Paste):
            event.ignore()
        else:
            super().keyPressEvent(event)

    def contextMenuEvent(self, event):
        menu = self.createStandardContextMenu()
        for action in menu.actions():
            if action.text() in ["&Copy", "&Paste"]:
                menu.removeAction(action)
        menu.exec_(event.globalPos())


if __name__ == '__main__':
    file_path = 'book.txt'
    background_image_path = 'background.png'
    try:
        text = read_text_from_file(file_path)
    except ValueError as e:
        print(e)
        sys.exit()

    app = QApplication(sys.argv)
    ex = TypingTest(text, background_image_path, width=800, height=600, text_font_size=24, input_font_size=24)
    ex.show()
    sys.exit(app.exec_())
