from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen


# The different screens
class MainWindow(Screen):
    deck = ["1♠","2♠","3♠","4♠","5♠","6♠","7♠","8♠","9♠","10♠","J♠","Q♠","K♠","1♥","2♥","3♥","4♥","5♥","6♥","7♥","8♥","9♥","10♥","J♥","Q♥","K♥","1♣","2♣","3♣","4♣","5♣","6♣","7♣","8♣","9♣","10♣","J♣","Q♣","K♣","1♦","2♦","3♦","4♦","5♦","6♦","7♦","8♦","9♦","10♦","J♦","Q♦","K♦"]
    
    def show_deck(self):
        self.ids.card_table.text = str(self.deck)
    

class WindowTwo(Screen):
    pass

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file('layouts.kv')



class Wx(App):
    def build(self):
        return kv


# on launch start main window class
if __name__ == "__main__":
    Wx().run()
