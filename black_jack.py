from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
import webbrowser
import random


Window.size = 1280, 720 

deck = {"1♠": ["Playing-Cards/card-spades-1.png", 11],"2♠": ["Playing-Cards/card-spades-2.png", 2],"3♠": ["Playing-Cards/card-spades-3.png", 3],"4♠": ["Playing-Cards/card-spades-4.png", 4],"5♠": ["Playing-Cards/card-spades-5.png", 5],"6♠": ["Playing-Cards/card-spades-6.png", 6],"7♠": ["Playing-Cards/card-spades-7.png", 7],"8♠": ["Playing-Cards/card-spades-8.png", 8],"9♠": ["Playing-Cards/card-spades-9.png", 9],"10♠": ["Playing-Cards/card-spades-10.png", 10],"J♠": ["Playing-Cards/card-spades-11.png", 10],"Q♠": ["Playing-Cards/card-spades-12.png", 10],"K♠": ["Playing-Cards/card-spades-13.png", 10],"1♥": ["Playing-Cards/card-hearts-1.png", 11],"2♥": ["Playing-Cards/card-hearts-2.png", 2],"3♥": ["Playing-Cards/card-hearts-3.png", 3],"4♥": ["Playing-Cards/card-hearts-4.png", 4],"5♥": ["Playing-Cards/card-hearts-5.png", 5],"6♥": ["Playing-Cards/card-hearts-6.png", 6],"7♥": ["Playing-Cards/card-hearts-7.png", 7],"8♥": ["Playing-Cards/card-hearts-8.png", 8],"9♥": ["Playing-Cards/card-hearts-9.png", 9],"10♥": ["Playing-Cards/card-hearts-10.png", 10],"J♥": ["Playing-Cards/card-hearts-11.png", 10],"Q♥": ["Playing-Cards/card-hearts-12.png", 10],"K♥": ["Playing-Cards/card-hearts-13.png", 10],"1♣": ["Playing-Cards/card-clubs-1.png", 11],"2♣": ["Playing-Cards/card-clubs-2.png", 2],"3♣": ["Playing-Cards/card-clubs-3.png", 3],"4♣": ["Playing-Cards/card-clubs-4.png", 4],"5♣": ["Playing-Cards/card-clubs-5.png", 5],"6♣": ["Playing-Cards/card-clubs-6.png", 6],"7♣": ["Playing-Cards/card-clubs-7.png", 7],"8♣": ["Playing-Cards/card-clubs-8.png", 8],"9♣": ["Playing-Cards/card-clubs-9.png", 9],"10♣": ["Playing-Cards/card-clubs-10.png", 10],"J♣": ["Playing-Cards/card-clubs-11.png", 10],"Q♣": ["Playing-Cards/card-clubs-12.png", 10],"K♣": ["Playing-Cards/card-clubs-13.png", 10],"1♦": ["Playing-Cards/card-diamonds-1.png", 11],"2♦": ["Playing-Cards/card-diamonds-2.png", 2],"3♦": ["Playing-Cards/card-diamonds-3.png", 3],"4♦": ["Playing-Cards/card-diamonds-4.png", 4],"5♦": ["Playing-Cards/card-diamonds-5.png", 5],"6♦": ["Playing-Cards/card-diamonds-6.png", 6],"7♦": ["Playing-Cards/card-diamonds-7.png", 7],"8♦": ["Playing-Cards/card-diamonds-8.png", 8],"9♦": ["Playing-Cards/card-diamonds-9.png", 9],"10♦": ["Playing-Cards/card-diamonds-10.png", 10],"J♦": ["Playing-Cards/card-diamonds-11.png", 10],"Q♦": ["Playing-Cards/card-diamonds-12.png", 10],"K♦": ["Playing-Cards/card-diamonds-13.png", 10]}

keys = list(deck.keys())
random.shuffle(keys)

player = []
dealer = []

stay_counter = []

class SplashWindow(Screen):
    
    def close(self):
    	exit()

class GameScreen(Screen):
    
    def deal_cards(self):

        # resets board for more than one match
        self.ids.prompt.text = ""
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
        
        # players hand
        
        player.append(deck[keys[0]][1])
        player.append(deck[keys[1]][1])


        # show players cards
        self.ids.card_one.source = deck[keys[0]][0]
        self.ids.card_two.source = deck[keys[1]][0]
        self.ids.card_one.height = "150dp"
        self.ids.card_two.height = "150dp"

        # dealers hand
        
        dealer.append(deck[keys[2]][1]) 
        dealer.append(deck[keys[3]][1])

        # show dealer cards
        self.ids.dealer_card_down.source = 'Playing-Cards/card-back1.png'
        self.ids.dealer_card_down.height = "150dp"
        self.ids.dealer_card_two.source = deck[keys[3]][0]
        self.ids.dealer_card_two.height = "150dp"


        self.ids.deal_button.disabled = True
        self.ids.hit_button.disabled = False
        self.ids.stay_button.disabled = False

  
        self.check_score()
    
    def hit(self):

        p_hit_count = len(player) + len(dealer)

        if self.ids.card_three.source == "":
            self.ids.card_three.source = deck[keys[p_hit_count + 1]][0]
            self.ids.card_three.height = "150dp"
            player.append(deck[keys[p_hit_count + 1]][1])
        elif self.ids.card_four.source == "":
            self.ids.card_four.source = deck[keys[p_hit_count + 1]][0]
            self.ids.card_four.height = "150dp"
            player.append(deck[keys[p_hit_count + 1]][1])
        elif self.ids.card_five.source == "":
            self.ids.card_five.source = deck[keys[p_hit_count + 1]][0]
            self.ids.card_five.height = "150dp"
            player.append(deck[keys[p_hit_count + 1]][1])
        elif self.ids.card_six.source == "":
            self.ids.card_six.source = deck[keys[p_hit_count + 1]][0]
            self.ids.card_six.height = "150dp"
            player.append(deck[keys[p_hit_count + 1]][1])
        else:
            self.ids.hit_button.disabled = False
            self.ids.prompt.text = "You can't draw more than 6 cards!"

        
        
        self.check_score()

    def stay(self):
        stay_counter.append(1)
        self.check_score()
        self.npc()


    def npc(self):

        dealer_check = sum(dealer)
        d_hit_count = len(player) + len(dealer)

        while dealer_check != 21:
            if dealer_check < 17:
                if self.ids.dealer_card_three.source == "":
                    self.ids.dealer_card_three.source = deck[keys[d_hit_count + 1]][0]
                    self.ids.dealer_card_three.height = "150dp"
                elif self.ids.dealer_card_four.source == "":
                    self.ids.dealer_card_four.source = deck[keys[d_hit_count + 1]][0]
                    self.ids.dealer_card_four.height = "150dp"
                elif self.ids.dealer_card_five.source == "":
                    self.ids.dealer_card_five.source = deck[keys[d_hit_count + 1]][0]
                    self.ids.dealer_card_five.height = "150dp"
                elif self.ids.dealer_card_six.source == "":
                    self.ids.dealer_card_six.source = deck[keys[d_hit_count + 1]][0]
                    self.ids.dealer_card_six.height = "150dp"
                else:
                    break

                    

                dealer.append(deck[keys[d_hit_count + 1]][1])

                dealer_check = sum(dealer)
            elif dealer_check >= 17:
                break


            
        stay_counter.append(1)
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

       
        if len(stay_counter) == 2:
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

        # Show the dealers face down card
        self.ids.dealer_card_down.source = deck[keys[2]][0]
        self.ids.dealer_card_down.height = "150dp"

        player.clear()
        dealer.clear()
        stay_counter.clear()

        random.shuffle(keys)
  
        self.ids.deal_button.disabled = False
        self.ids.hit_button.disabled = True
        self.ids.stay_button.disabled = True
        
    def donate_button(self):
        webbrowser.open('https://ko-fi.com/jessecreates', new = 2)
		

class NavBar(Screen):
	pass
	


class WindowManager(ScreenManager):
    pass



class BlackJack(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "DeepPurple"
        return Builder.load_file('layouts.kv')
        


# on launch start main window class
if __name__ == "__main__":
    BlackJack().run()
