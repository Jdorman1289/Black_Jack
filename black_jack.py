from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import random


deck = {"1♠": ["black/Pikes_A_black.png", 11],"2♠": ["black/Pikes_2_black.png", 2],"3♠": ["black/Pikes_3_black.png", 3],"4♠": ["black/Pikes_4_black.png", 4],"5♠": ["black/Pikes_5_black.png", 5],"6♠": ["black/Pikes_6_black.png", 6],"7♠": ["black/Pikes_7_black.png", 7],"8♠": ["black/Pikes_8_black.png", 8],"9♠": ["black/Pikes_9_black.png", 9],"10♠": ["black/Pikes_10_black.png", 10],"J♠": ["black/Pikes_Jack_black.png", 10],"Q♠": ["black/Pikes_Queen_black.png", 10],"K♠": ["black/Pikes_King_black.png", 10],"1♥": ["black/Hearts_A_black.png", 11],"2♥": ["black/Hearts_2_black.png", 2],"3♥": ["black/Hearts_3_black.png", 3],"4♥": ["black/Hearts_4_black.png", 4],"5♥": ["black/Hearts_5_black.png", 5],"6♥": ["black/Hearts_6_black.png", 6],"7♥": ["black/Hearts_7_black.png", 7],"8♥": ["black/Hearts_8_black.png", 8],"9♥": ["black/Hearts_9_black.png", 9],"10♥": ["black/Hearts_10_black.png", 10],"J♥": ["black/Hearts_Jack_black.png", 10],"Q♥": ["black/Hearts_Queen_black.png", 10],"K♥": ["black/Hearts_King_black.png", 10],"1♣": ["black/Clovers_A_black.png", 11],"2♣": ["black/Clovers_2_black.png", 2],"3♣": ["black/Clovers_3_black.png", 3],"4♣": ["black/Clovers_4_black.png", 4],"5♣": ["black/Clovers_5_black.png", 5],"6♣": ["black/Clovers_6_black.png", 6],"7♣": ["black/Clovers_7_black.png", 7],"8♣": ["black/Clovers_8_black.png", 8],"9♣": ["black/Clovers_9_black.png", 9],"10♣": ["black/Clovers_10_black.png", 10],"J♣": ["black/Clovers_Jack_black.png", 10],"Q♣": ["black/Clovers_Queen_black.png", 10],"K♣": ["black/Clovers_King_black.png", 10],"1♦": ["black/Tiles_A_black.png", 11],"2♦": ["black/Tiles_2_black.png", 2],"3♦": ["black/Tiles_3_black.png", 3],"4♦": ["black/Tiles_4_black.png", 4],"5♦": ["black/Tiles_5_black.png", 5],"6♦": ["black/Tiles_6_black.png", 6],"7♦": ["black/Tiles_7_black.png", 7],"8♦": ["black/Tiles_8_black.png", 8],"9♦": ["black/Tiles_9_black.png", 9],"10♦": ["black/Tiles_10_black.png", 10],"J♦": ["black/Tiles_Jack_black.png", 10],"Q♦": ["black/Tiles_Queen_black.png", 10],"K♦": ["black/Tiles_King_black.png", 10]}

keys = list(deck.keys())
random.shuffle(keys)

player = []
dealer = []

stay_counter = []

class GameScreen(Screen):
    
    def deal_cards(self):
        
        # players hand
        
        player.append(deck[keys[0]][1])
        player.append(deck[keys[1]][1])


        # show players cards
        self.ids.card_one.source = deck[keys[0]][0]
        self.ids.card_two.source = deck[keys[1]][0]
        self.ids.card_one.height = "180dp"
        self.ids.card_two.height = "180dp"

        # dealers hand
        
        dealer.append(deck[keys[2]][1]) 
        dealer.append(deck[keys[3]][1])

        # show dealer cards
        self.ids.dealer_card_two.source = deck[keys[2]][0]
        self.ids.dealer_card_two.height = "180dp"
        self.ids.dealer_card_down.source = 'black/card_back.png'
        self.ids.dealer_card_down.height = "180dp"

        self.ids.deal_button.disabled = True
        self.ids.hit_button.disabled = False
        self.ids.stay_button.disabled = False

  
        self.check_score()
    
    def hit(self):

        p_hit_count = len(player) + len(dealer)

        if self.ids.card_three.source == "":
            self.ids.card_three.source = deck[keys[p_hit_count + 1]][0]
            self.ids.card_three.height = "180dp"
        elif self.ids.card_four.source == "":
            self.ids.card_four.source = deck[keys[p_hit_count + 1]][0]
            self.ids.card_four.height = "180dp"
        elif self.ids.card_five.source == "":
            self.ids.card_five.source = deck[keys[p_hit_count + 1]][0]
            self.ids.card_five.height = "180dp"
        elif self.ids.card_six.source == "":
            self.ids.card_six.source = deck[keys[p_hit_count + 1]][0]
            self.ids.card_six.height = "180dp"

        player.append(deck[keys[p_hit_count + 1]][1])
        
        
        self.check_score()

    def stay(self):
        stay_counter.append(1)
        self.check_score()
        self.npc()

    def npc_runner(self):
        dealer_check = sum(dealer)

        if dealer_check < 17:
            self.ids.prompt.text = "The Dealer Hits"
            self.npc()
        elif dealer_check >= 17:
            self.ids.prompt.text = "The Dealer Stays"
            stay_counter.append(1)
            self.check_score()

    def npc(self):

        d_hit_count = len(player) + len(dealer)


        if self.ids.dealer_card_three.source == "":
            self.ids.dealer_card_three.source = deck[keys[d_hit_count + 1]][0]
            self.ids.dealer_card_three.height = "180dp"
            dealer.append(deck[keys[d_hit_count + 1]][1])
        elif self.ids.dealer_card_four.source == "":
            self.ids.dealer_card_four.source = deck[keys[d_hit_count + 1]][0]
            self.ids.dealer_card_four.height = "180dp"
            dealer.append(deck[keys[d_hit_count + 1]][1])
        elif self.ids.dealer_card_five.source == "":
            self.ids.dealer_card_five.source = deck[keys[d_hit_count + 1]][0]
            self.ids.dealer_card_five.height = "180dp"
            dealer.append(deck[keys[d_hit_count + 1]][1])
        elif self.ids.dealer_card_six.source == "":
            self.ids.dealer_card_six.source = deck[keys[d_hit_count + 1]][0]
            self.ids.dealer_card_six.height = "180dp"
            dealer.append(deck[keys[d_hit_count + 1]][1])
        
        
        self.check_score()

   
    def check_score(self):

        player_score = sum(player)
        dealer_score = sum(dealer)


        # Logic for Ace card values
        for values in player:
            if values == 11 and player_score > 21:
                player.remove(11)
                player.append(1)

                player_score = sum(player)

        for value in dealer:
            if value == 11 and dealer_score > 21:
                dealer.remove(11)
                dealer.append(1)

                dealer_score = sum(dealer)

       
        if len(stay_counter) >= 2:
            if player_score == dealer_score:
                self.ids.prompt.text = "You tied!"  
                self.reset_game()   
            elif player_score > dealer_score and player_score < 21:
                self.ids.prompt.text = "You won!"
                self.reset_game()
            elif player_score < dealer_score and dealer_score < 21:
                self.ids.prompt.text = "The Dealer won!"
                self.reset_game()


        if player_score == 21 and dealer_score == 21:
            self.ids.prompt.text = "Its a tie at 21!"
            self.reset_game()
        elif player_score == 21 and dealer_score != 21:
            self.ids.prompt.text = "You won with a 21!"
            self.reset_game()
        elif player_score != 21 and dealer_score == 21:
            self.ids.prompt.text = "The Dealer won with 21!"
            self.reset_game()
        elif player_score > 21 and dealer_score < 21:
            self.ids.prompt.text = "You busted 21. The Dealer wins!"
            self.reset_game()
        elif player_score < 21 and dealer_score > 21:
            self.ids.prompt.text = "You won. The Dealer busted 21!"
            self.reset_game()


 

   
    def reset_game(self):

        # clear player cards
        self.ids.card_one.height = "0dp"
        self.ids.card_two.height = "0dp"
        self.ids.card_three.height = "0dp"
        self.ids.card_four.height = "0dp"
        self.ids.card_five.height = "0dp"
        self.ids.card_six.height = "0dp"
        self.ids.card_one.source = ""
        self.ids.card_two.source = ""
        self.ids.card_three.source = ""
        self.ids.card_four.source = ""
        self.ids.card_five.source = ""
        self.ids.card_six.source = ""

        # clear dealers cards
        self.ids.dealer_card_down.source = ""
        self.ids.dealer_card_down.height = "0dp"        
        self.ids.dealer_card_two.height = "0dp"
        self.ids.dealer_card_two.source = ""
        self.ids.dealer_card_three.height = "0dp"
        self.ids.dealer_card_three.source = ""
        self.ids.dealer_card_four.height = "0dp"
        self.ids.dealer_card_four.source = ""
        self.ids.dealer_card_five.height = "0dp"
        self.ids.dealer_card_five.source = ""
        self.ids.dealer_card_six.height = "0dp"
        self.ids.dealer_card_six.source = ""

        player.clear()
        dealer.clear()
        stay_counter.clear()

        random.shuffle(keys)
  
        self.ids.deal_button.disabled = False
        self.ids.hit_button.disabled = True
        self.ids.stay_button.disabled = True



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
