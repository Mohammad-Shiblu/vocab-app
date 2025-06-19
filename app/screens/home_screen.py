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


class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super(HomeScreen, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.spacing = dp(20)
        self.padding = dp(20)
        self.setup_ui()

    def setup_ui(self):
        
        with self.canvas.before:
            self.bg_image = Rectangle(
                source='fig/background.png',
                size=self.size,
                pos=self.pos
            )
        self.bind(size=self.update_bg, pos=self.update_bg)
        
        

        self.app_title = Label(
            text = "Vocab",
            font_size = sp(36),
            color = (0.2, 0.4, 0.4, 1),
            size_hint = None,
            height = self.texture_size[1] + dp(10),
        )

        # Input and Output Widgets
        self.input_box = TextInput(
            hint_text='Enter a word',
            font_size = 20,
            size_hint=(0.6, 0.1),
            pos_hint={'center_x': 0.5, 'center_y': 0.6},
            background_color=(1, 1, 1, 0.8),
            foreground_color=(0, 0, 0, 1),
            multiline=False
        )

        self.output_label = Label(
            text="Meaning will show here.",
            font_size=18,
            size_hint=(0.8, 0.2),
            pos_hint={'center_x': 0.5, 'center_y': 0.4},
            color=(0, 0, 0, 1),  
        )
        self.button = Button(
            text='Search',
            size_hint=(0.3, 0.1),
            pos_hint={'center_x': 0.5, 'center_y': 0.25},
            background_normal='',
            background_color=(0.3, 0.6, 0.3, 1),
            font_size=20
        )
        
        self.button.bind(on_press=self.on_translate)

        self.btn_word_list = Button(
            text='View Saved Words',
            size_hint=(0.3, 0.1),
            pos_hint={'center_x': 0.5, 'center_y': 0.1},
            background_normal='',
            background_color=(0.3, 0.6, 0.3, 1),
            font_size=20
        )
        self.btn_word_list.bind(on_press=self.go_to_word_list)

        self.layout.add_widget(self.app_title)
        self.layout.add_widget(self.input_box)
        self.layout.add_widget(self.output_label)
        self.layout.add_widget(self.button)
        self.layout.add_widget(self.btn_word_list)
        self.add_widget(self.layout)

    def update_bg(self, *args):
        self.bg_rect.pos = self.pos
        self.bg_rect.size = self.size
    def on_translate(self, instance):
        word = self.input_box.text.strip()
        if not word:
            self.output_label.text = "Please enter a word."
            return
        translation = translate_word(word)
        if translation:
            self.output_label.text = translation
            save_word(word, translation)
        else:
            self.output_label.text = "Translation failed. Please try again."

    def go_to_word_list(self, instance):
        self.manager.current = 'word_list'