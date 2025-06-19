from kivy.graphics import Color, Rectangle, RoundedRectangle
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.metrics import sp, dp
from kivy.core.image import Image as CoreImage
from app.services.translator import translate_word
from app.services.database import save_word
from kivy.uix.boxlayout import BoxLayout

class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super(HomeScreen, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.spacing = dp(20)
        self.padding = dp(20)
        self.setup_ui()

    def setup_ui(self):
        
        with self.canvas.before:
            Color(0.125, 0.698, 0.667, 1)
            self.bg_rect = Rectangle(pos=self.pos, size=self.size)
        self.bind(size=self.update_bg, pos=self.update_bg)
        
        layout = BoxLayout(orientation='vertical', spacing=dp(20), padding=dp(20))
        # Title label
        title =Label(
            text='Vocab',
            font_size=sp(42),
            size_hint=(1, 0.2),
            height=dp(30),
            color=(0.2, 0.4, 0.4, 1),  
            font_name = "fonts/Roboto/static/Roboto-Bold.ttf"
        )
        layout.add_widget(title)

        # Buttons
        buttons = [
            ("Add Word", self.add_word),
            ("Word List", self.word_list),
            ("Practice", self.practice),
            ("Quiz", self.quiz),
        ]
        for text, callback in buttons:
            btn = Button(
                text=text,
                size_hint_y=None,
                height=dp(60),
                background_color=(1, 1, 1, 1),
                color = (0.2, 0.4, 0.4, 1),
                font_size= '18sp',
                background_normal=''
            )
            with btn.canvas.before:
                Color(1, 1, 1, 1)
                btn.bg = RoundedRectangle(pos=btn.pos, size=btn.size, radius=[20])
                btn.bind(pos=self.update_btn_bg(btn), size= self.update_btn_bg(btn))
            btn.bind(on_press=callback)
            layout.add_widget(btn)

        self.add_widget(layout)
        

    def update_bg(self, *args):
        self.bg_rect.pos = self.pos
        self.bg_rect.size = self.size

    def update_btn_bg(self, btn):
        def update(instance, value):
            btn.bg.pos = instance.pos
            btn.bg.size = instance.size
        return update
    
    def add_word(self, instance): print("Add Word clicked")
    def word_list(self, instance): print("Word List clicked")
    def practice(self, instance): print("Practice clicked")
    def quiz(self, instance): print("Quiz clicked")


    # def on_translate(self, instance):
    #     word = self.input_box.text.strip()
    #     if not word:
    #         self.output_label.text = "Please enter a word."
    #         return
    #     translation = translate_word(word)
    #     if translation:
    #         self.output_label.text = translation
    #         save_word(word, translation)
    #     else:
    #         self.output_label.text = "Translation failed. Please try again."

    # def go_to_word_list(self, instance):
    #     self.manager.current = 'word_list'