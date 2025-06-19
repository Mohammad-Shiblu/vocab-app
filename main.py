from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from app.screens.home_screen import HomeScreen
from app.screens.word_list_screen import WordListScreen
from app.screens.review_screen import ReviewScreen

class VocabApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(HomeScreen(name='home'))
        sm.add_widget(WordListScreen(name='word_list'))
        sm.add_widget(ReviewScreen(name='review'))
        return sm
    
if __name__ == '__main__':
    VocabApp().run()