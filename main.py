from kivy.config import Config
Config.set('graphics', 'width', '360')
Config.set('graphics', 'height', '640')
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from app.screens.home_screen import HomeScreen
from app.screens.word_list_screen import WordListScreen
from app.screens.review_screen import ReviewScreen
from app.screens.add_word import AddWordScreen
from app.screens.quiz import MultipleChoiceQuizScreen
from kivy.lang import Builder
import os
from kivy.logger import Logger

if 'ANDROID_PRIVATE' in os.environ:
    log_path = os.path.join(os.environ['ANDROID_PRIVATE'], 'my_app_log.txt')
    Logger.info("MyApp: Android log path exists")
    Logger.info("MyApp: Full log file path: %s", log_path)
else:
    Logger.warning("MyApp: ANDROID_PRIVATE not found — running outside Android environment?")

class VocabApp(App):
    def build(self):
        Logger.info("VocabApp: Starting application")
        Builder.load_file('app/screens/home_screen.kv') 
        Builder.load_file('app/screens/add_word.kv')
        Builder.load_file('app/screens/word_list.kv')
        Builder.load_file('app/screens/review_screen.kv')
        Builder.load_file('app/screens/quiz.kv')
        Logger.info("VocabApp: KV files loaded successfully")

        sm = ScreenManager()
        sm.add_widget(HomeScreen(name='home'))
        sm.add_widget(AddWordScreen(name='add_word'))
        sm.add_widget(WordListScreen(name='word_list'))
        sm.add_widget(ReviewScreen(name='review'))
        sm.add_widget(MultipleChoiceQuizScreen(name='quiz'))
        Logger.info("VocabApp: Screens added to ScreenManager")
        return sm
    
if __name__ == '__main__':
    print("Launching VocabApp")
    VocabApp().run()