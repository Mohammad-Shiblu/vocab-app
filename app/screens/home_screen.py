from kivy.uix.screenmanager import Screen

class HomeScreen(Screen):
    def add_word(self):
        self.manager.current = 'add_word'

    def word_list(self):
        self.manager.current = 'word_list'

    def practice(self):
        print("Practice clicked")

    def quiz(self):
        print("Quiz clicked")
