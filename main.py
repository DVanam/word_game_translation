import sys
import random
import json
from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow
from googletrans import Translator

from ui_game import Ui_MainWindow
from ui_new_add import Ui_Dialog
from database import Database

class TranslatorApp(QMainWindow):
    def __init__(self):
        # QMainWindow.__init__(self)
        super(TranslatorApp, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.input_text = self.ui.input_text
        self.output_text = self.ui.output_text


        self.en_text = self.ui.en_le_text
        self.en_text.returnPressed.connect(self.check_answer)

        self.ru_text = self.ui.ru_qeustion

        self.history_field = self.ui.check_qeust_ans_text

        self.session_spin = self.ui.session_spinbox
        self.start_button = self.ui.start_session
        self.start_button.clicked.connect(self.start_session)
        self.add_new_btn = self.ui.save_word_button
        self.add_new_btn.clicked.connect(self.open_window_add_words)


        self.translator = Translator()

        self.database = Database('trans_database.db')

        self.input_text.textChanged.connect(self.translate_text)

        self.words = {
            "привет": "hello",
            "пока": "goodbye",
            "спасибо": "thank you",
            # Add more words here
        }

        self.session_words = []
        self.current_word = None
        # self.show()

    def open_window_add_words(self):
        self.new_window = QtWidgets.QDialog()
        self.ui_window = Ui_Dialog()
        self.ui_window.setupUi(self.new_window)
        self.new_window.show()
        sender = self.sender()

    def start_session(self):
        self.session_words = random.sample(list(self.words.items()), self.session_spin.value())
        self.next_word()

    def next_word(self):
        if not self.session_words:
            self.history_field.append("End of session. Start a new session.")
            self.ru_text.clear()
            return
        self.current_word = self.session_words.pop()
        self.ru_text.setText(self.current_word[0])

    def check_answer(self):
        user_answer = self.en_text.text().strip()
        correct_answer = self.current_word[1]

        if user_answer.lower() == correct_answer.lower():
            self.history_field.append(f"Q: {self.current_word[0]}\nA: {user_answer} - Correct!\n")
        else:
            self.history_field.append(
                f"Q: {self.current_word[0]}\nA: {user_answer} - Incorrect, Correct Answer: {correct_answer}\n")

        self.en_text.clear()
        self.next_word()

    def translate_text(self):
        input_text = self.input_text.toPlainText()
        if input_text.strip():  # Проверяем, что введенный текст не пустой
            translated_text = self.translator.translate(input_text, src='ru', dest='en').text
            self.output_text.setPlainText(translated_text)
        else:
            self.output_text.clear()  # Если введен пустой текст, очищаем поле вывода


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TranslatorApp()
    window.show()
    sys.exit(app.exec())