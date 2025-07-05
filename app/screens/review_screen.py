from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty, BooleanProperty
from app.services.database import get_all_words
import random

class ReviewScreen(Screen):
    current_display = StringProperty("")
    flipped = BooleanProperty(False)

    def on_enter(self):
        self.words = get_all_words()
        random.shuffle(self.words)
        self.index = 0
        self.flipped = False
        self.current_display = self.words[self.index][0] if self.words else "No words available"

    def flip_card(self):
        if not self.words:
            return
        word, meaning = self.words[self.index]
        self.flipped = not self.flipped
        self.current_display = meaning if self.flipped else word

    def next_card(self):
        if not self.words:
            return
        self.index = (self.index + 1) % len(self.words)
        self.flipped = False
        self.current_display = self.words[self.index][0]

    def go_back(self):
        self.manager.current = "home"
