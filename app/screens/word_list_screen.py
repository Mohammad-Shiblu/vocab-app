from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from app.services.database import get_all_words
from kivy.uix.button import Button

class WordListScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical')
        self.add_widget(self.layout)
        
    def on_enter(self):
        self.layout.clear_widgets()
        words = get_all_words()
        if not words:
            self.layout.add_widget(Label(text="No words saved yet."))
        else:
            for word, meaning in words:
                self.layout.add_widget(Label(text=f"{word}: {meaning}"))
            
        btn_back = Button(text="Back to Home", size_hint_y=0.1)
        btn_back.bind(on_press=lambda x: setattr(self.manager, 'current', 'home'))
        self.layout.add_widget(btn_back)