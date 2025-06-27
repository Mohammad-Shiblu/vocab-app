from kivy.uix.screenmanager import Screen
from app.services.translator import translate_word
from app.services.database import save_word


class AddWordScreen(Screen):
    def on_translate(self, input_widget):
        word = input_widget.text.strip()
        output_widget = self.ids.translation_output  # From the KV file

        if not word:
            output_widget.text = "Please enter a word."
            return

        translation = translate_word(word)
        if translation:
            output_widget.text = translation
            save_word(word, translation)
        else:
            output_widget.text = "Translation failed. Please try again."

    def go_back(self):
        self.manager.current = 'home'
