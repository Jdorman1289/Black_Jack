from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen




class GameScreen(Screen):
    
    deck = {"1♠": ["black/Pikes_A_black.png", 1],"2♠": ["black/Pikes_2_black.png", 2],"3♠": ["black/Pikes_3_black.png", 3],"4♠": ["black/Pikes_4_black.png", 4],"5♠": ["black/Pikes_5_black.png", 5],"6♠": ["black/Pikes_6_black.png", 6],"7♠": ["black/Pikes_7_black.png", 7],"8♠": ["black/Pikes_8_black.png", 8],"9♠": ["black/Pikes_9_black.png", 9],"10♠": ["black/Pikes_10_black.png", 10],"J♠": ["black/Pikes_Jack_black.png", 10],"Q♠": ["black/Pikes_Queen_black.png", 10],"K♠": ["black/Pikes_King_black.png", 10],"1♥","2♥","3♥","4♥","5♥","6♥","7♥","8♥","9♥","10♥","J♥","Q♥","K♥","1♣","2♣","3♣","4♣","5♣","6♣","7♣","8♣","9♣","10♣","J♣","Q♣","K♣","1♦","2♦","3♦","4♦","5♦","6♦","7♦","8♦","9♦","10♦","J♦","Q♦","K♦"}




class WindowManager(ScreenManager):
    pass



class BlackJack(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Teal"
        return Builder.load_file('layouts.kv')
        


# on launch start main window class
if __name__ == "__main__":
    BlackJack().run()
