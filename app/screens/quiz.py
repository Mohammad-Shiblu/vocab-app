
from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty, ListProperty
import random
from app.services.database import get_all_words  

class MultipleChoiceQuizScreen(Screen):
    question_text = StringProperty("")
    options = ListProperty([])
    correct_answer = StringProperty("")
    option_buttons = ListProperty([])

    def on_enter(self):
        self.load_question()
        self.option_buttons = [
        self.ids.btn1,
        self.ids.btn2,
        self.ids.btn3,
        self.ids.btn4,
        ]

    def load_question(self):
        words = get_all_words()
        if len(words) < 4:
            self.question_text = "Not enough words in database."
            self.options = []
            return

        word, meaning = random.choice(words)
        self.correct_answer = meaning
        self.question_text = f"[b]{word}[/b]?"

        # Create 3 wrong answers + 1 correct
        other_meanings = list({m for w, m in words if m != meaning})
        choices = random.sample(other_meanings, 3) + [meaning]
        random.shuffle(choices)
        self.options = choices

        for btn in self.option_buttons:
            btn.background_color = (1, 1, 1, 1)

    def check_answer(self, selected_text):
        for btn in self.option_buttons:
            if btn.text == selected_text:
                if btn.text == self.correct_answer:
                    btn.background_color = (0.8, 1, 0.8, 1)  # Green for correct
                    self.question_text = "Correct!"
                else:
                    btn.background_color = (1, 0.8, 0.8, 1)  # Red for wrong
                    self.question_text = f"Incorrect! Correct ans: {self.correct_answer}"
                break 

        self.ids.next_btn.disabled = False

    def next_question(self):
        self.ids.next_btn.disabled = True
        self.load_question()

    def go_back(self):
        self.manager.current = "home"
