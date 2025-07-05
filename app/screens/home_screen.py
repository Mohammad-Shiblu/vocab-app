from kivy.uix.screenmanager import Screen
from kivy.logger import Logger

class HomeScreen(Screen):
    def add_word(self):
        Logger.info("Navigation: Switching to AddWordScreen")
        self.manager.current = 'add_word'

    def word_list(self):
        Logger.info("Navigation: Switching to WordListScreen")
        self.manager.current = 'word_list'

    def practice(self):
        Logger.info("Navigation: Switching to ReviewScreen")
        self.manager.current = 'review'

    def quiz(self):
        Logger.info("Navigation: Switching to QuizScreen")
        self.manager.current = 'quiz'
