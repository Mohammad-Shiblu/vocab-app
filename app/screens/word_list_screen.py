from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.utils import get_color_from_hex
from app.services.database import get_all_words  

class WordListScreen(Screen):
    all_words = []  # store all words here

    def on_enter(self):
        self.all_words = get_all_words()
        self.display_words(self.all_words)

    def display_words(self, words):
        word_container = self.ids.word_container
        word_container.clear_widgets()

        from kivy.graphics import Color, Rectangle
        from kivy.utils import get_color_from_hex

        alt_colors = ['#e0f7fa', '#ffffff']

        for idx, (word, meaning) in enumerate(words):
            row = BoxLayout(orientation='horizontal', size_hint_y=None, height=50, padding=[10,0,10,0], spacing=10)

            row.canvas.before.clear()
            with row.canvas.before:
                Color(*get_color_from_hex(alt_colors[idx % 2]))
                rect = Rectangle(pos=row.pos, size=row.size)
            row.bind(pos=lambda instance, val, rect=rect: setattr(rect, 'pos', val))
            row.bind(size=lambda instance, val, rect=rect: setattr(rect, 'size', val))

            word_label = Label(text=word, color=(0, 0, 0, 1), bold=True, size_hint_x=0.4)
            meaning_label = Label(text=meaning, color=(0, 0, 0, 1), size_hint_x=0.6)

            row.add_widget(word_label)
            row.add_widget(meaning_label)

            word_container.add_widget(row)

    def filter_words(self, query):
        filtered = [w for w in self.all_words if query.lower() in w[0].lower()]
        self.display_words(filtered)

    def go_back(self):
        self.manager.current = "home"
