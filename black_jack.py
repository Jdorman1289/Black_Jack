from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen




class GameScreen(Screen):
    
    deck = {"1♠": ["black/Pikes_A_black.png", 1],"2♠": ["black/Pikes_2_black.png", 2],"3♠": ["black/Pikes_3_black.png", 3],"4♠": ["black/Pikes_4_black.png", 4],"5♠": ["black/Pikes_5_black.png", 5],"6♠": ["black/Pikes_6_black.png", 6],"7♠": ["black/Pikes_7_black.png", 7],"8♠": ["black/Pikes_8_black.png", 8],"9♠": ["black/Pikes_9_black.png", 9],"10♠": ["black/Pikes_10_black.png", 10],"J♠": ["black/Pikes_Jack_black.png", 10],"Q♠": ["black/Pikes_Queen_black.png", 10],"K♠": ["black/Pikes_King_black.png", 10],"1♥": ["black/Hearts_A_black.png", 1],"2♥": ["black/Hearts_2_black.png", 2],"3♥": ["black/Hearts_3_black.png", 3],"4♥": ["black/Hearts_4_black.png", 4],"5♥": ["black/Hearts_5_black.png", 5],"6♥": ["black/Hearts_6_black.png", 6],"7♥": ["black/Hearts_7_black.png", 7],"8♥": ["black/Hearts_8_black.png", 8],"9♥": ["black/Hearts_9_black.png", 9],"10♥": ["black/Hearts_10_black.png", 10],"J♥": ["black/Hearts_Jack_black.png", 10],"Q♥": ["black/Hearts_Queen_black.png", 10],"K♥": ["black/Hearts_King_black.png", 10],"1♣": ["black/Clovers_A_black.png", 1],"2♣": ["black/Clovers_2_black.png", 2],"3♣": ["black/Clovers_3_black.png", 3],"4♣": ["black/Clovers_4_black.png", 4],"5♣": ["black/Clovers_5_black.png", 5],"6♣": ["black/Clovers_6_black.png", 6],"7♣": ["black/Clovers_7_black.png", 7],"8♣": ["black/Clovers_8_black.png", 8],"9♣": ["black/Clovers_9_black.png", 9],"10♣": ["black/Clovers_10_black.png", 10],"J♣": ["black/Clovers_Jack_black.png", 10],"Q♣": ["black/Clovers_Queen_black.png", 10],"K♣": ["black/Clovers_King_black.png", 10],"1♦": ["black/Tiles_A_black.png", 1],"2♦": ["black/Tiles_2_black.png", 2],"3♦": ["black/Tiles_3_black.png", 3],"4♦": ["black/Tiles_4_black.png", 4],"5♦": ["black/Tiles_5_black.png", 5],"6♦": ["black/Tiles_6_black.png", 6],"7♦": ["black/Tiles_7_black.png", 7],"8♦": ["black/Tiles_8_black.png", 8],"9♦": ["black/Tiles_9_black.png", 9],"10♦": ["black/Tiles_10_black.png", 10],"J♦": ["black/Tiles_Jack_black.png", 10],"Q♦": ["black/Tiles_Queen_black.png", 10],"K♦": ["black/Tiles_King_black.png", 10]}

    #def deal_cards(self, deck):



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
