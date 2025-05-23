from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.dialog import MDDialog
from kivy.logger import Logger
import webbrowser
import random
import sys
import traceback
import os
import pygame  # For better cross-platform audio support
from threading import Thread

# Robust cross-platform sound player using PyGame
class PygameSoundPlayer:
    def __init__(self):
        Logger.info('PygameSoundPlayer: Initializing PyGame mixer')
        # Initialize PyGame mixer in a way that minimizes startup delay
        self._initialize_mixer()
        self.sounds = {}
        self.initialized = False
    
    def _initialize_mixer(self):
        # Start PyGame mixer initialization in a separate thread to avoid blocking
        Thread(target=self._init_thread, daemon=True).start()
    
    def _init_thread(self):
        try:
            # Low buffer size and frequency for faster startup
            pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=512)
            pygame.mixer.set_num_channels(16)  # More channels for overlapping sounds
            Logger.info('PygameSoundPlayer: PyGame mixer initialized successfully')
            self.initialized = True
        except Exception as e:
            Logger.error(f'PygameSoundPlayer: Failed to initialize mixer: {e}')
            
    def load(self, sound_id, path):
        """Load a sound file and associate it with an ID"""
        try:
            if not os.path.exists(path):
                Logger.warning(f'PygameSoundPlayer: Sound file not found: {path}')
                return None
                
            # Add the sound to our dictionary but wait to load it until the mixer is ready
            self.sounds[sound_id] = {'path': path, 'sound': None, 'loaded': False}
            Logger.info(f'PygameSoundPlayer: Sound registered: {sound_id} - {path}')
            
            # Try to load immediately if mixer is ready
            if self.initialized:
                self._load_sound(sound_id)
            return sound_id
        except Exception as e:
            Logger.error(f'PygameSoundPlayer: Error registering sound {path}: {e}')
            return None
    
    def _load_sound(self, sound_id):
        """Actually load the sound using PyGame mixer"""
        try:
            if sound_id not in self.sounds:
                return
                
            sound_info = self.sounds[sound_id]
            if sound_info['loaded']:
                return  # Already loaded
                
            sound_info['sound'] = pygame.mixer.Sound(sound_info['path'])
            sound_info['loaded'] = True
            Logger.info(f'PygameSoundPlayer: Sound loaded: {sound_id}')
        except Exception as e:
            Logger.error(f'PygameSoundPlayer: Error loading sound {sound_id}: {e}')
    
    def play(self, sound_id):
        """Play a previously loaded sound by its ID"""
        try:
            # If mixer isn't ready yet, just return silently
            if not self.initialized:
                return
                
            # If this sound hasn't been loaded yet, load it now
            if sound_id in self.sounds and not self.sounds[sound_id]['loaded']:
                self._load_sound(sound_id)
                
            # Play the sound if it's available
            if sound_id in self.sounds and self.sounds[sound_id]['loaded']:
                self.sounds[sound_id]['sound'].play()
        except Exception as e:
            Logger.error(f'PygameSoundPlayer: Error playing sound {sound_id}: {e}')

deck = {
    "1♠": ["Playing-Cards/card-spades-1.png", 11],
    "2♠": ["Playing-Cards/card-spades-2.png", 2],
    "3♠": ["Playing-Cards/card-spades-3.png", 3],
    "4♠": ["Playing-Cards/card-spades-4.png", 4],
    "5♠": ["Playing-Cards/card-spades-5.png", 5],
    "6♠": ["Playing-Cards/card-spades-6.png", 6],
    "7♠": ["Playing-Cards/card-spades-7.png", 7],
    "8♠": ["Playing-Cards/card-spades-8.png", 8],
    "9♠": ["Playing-Cards/card-spades-9.png", 9],
    "10♠": ["Playing-Cards/card-spades-10.png", 10],
    "J♠": ["Playing-Cards/card-spades-11.png", 10],
    "Q♠": ["Playing-Cards/card-spades-12.png", 10],
    "K♠": ["Playing-Cards/card-spades-13.png", 10],
    "1♥": ["Playing-Cards/card-hearts-1.png", 11],
    "2♥": ["Playing-Cards/card-hearts-2.png", 2],
    "3♥": ["Playing-Cards/card-hearts-3.png", 3],
    "4♥": ["Playing-Cards/card-hearts-4.png", 4],
    "5♥": ["Playing-Cards/card-hearts-5.png", 5],
    "6♥": ["Playing-Cards/card-hearts-6.png", 6],
    "7♥": ["Playing-Cards/card-hearts-7.png", 7],
    "8♥": ["Playing-Cards/card-hearts-8.png", 8],
    "9♥": ["Playing-Cards/card-hearts-9.png", 9],
    "10♥": ["Playing-Cards/card-hearts-10.png", 10],
    "J♥": ["Playing-Cards/card-hearts-11.png", 10],
    "Q♥": ["Playing-Cards/card-hearts-12.png", 10],
    "K♥": ["Playing-Cards/card-hearts-13.png", 10],
    "1♣": ["Playing-Cards/card-clubs-1.png", 11],
    "2♣": ["Playing-Cards/card-clubs-2.png", 2],
    "3♣": ["Playing-Cards/card-clubs-3.png", 3],
    "4♣": ["Playing-Cards/card-clubs-4.png", 4],
    "5♣": ["Playing-Cards/card-clubs-5.png", 5],
    "6♣": ["Playing-Cards/card-clubs-6.png", 6],
    "7♣": ["Playing-Cards/card-clubs-7.png", 7],
    "8♣": ["Playing-Cards/card-clubs-8.png", 8],
    "9♣": ["Playing-Cards/card-clubs-9.png", 9],
    "10♣": ["Playing-Cards/card-clubs-10.png", 10],
    "J♣": ["Playing-Cards/card-clubs-11.png", 10],
    "Q♣": ["Playing-Cards/card-clubs-12.png", 10],
    "K♣": ["Playing-Cards/card-clubs-13.png", 10],
    "1♦": ["Playing-Cards/card-diamonds-1.png", 11],
    "2♦": ["Playing-Cards/card-diamonds-2.png", 2],
    "3♦": ["Playing-Cards/card-diamonds-3.png", 3],
    "4♦": ["Playing-Cards/card-diamonds-4.png", 4],
    "5♦": ["Playing-Cards/card-diamonds-5.png", 5],
    "6♦": ["Playing-Cards/card-diamonds-6.png", 6],
    "7♦": ["Playing-Cards/card-diamonds-7.png", 7],
    "8♦": ["Playing-Cards/card-diamonds-8.png", 8],
    "9♦": ["Playing-Cards/card-diamonds-9.png", 9],
    "10♦": ["Playing-Cards/card-diamonds-10.png", 10],
    "J♦": ["Playing-Cards/card-diamonds-11.png", 10],
    "Q♦": ["Playing-Cards/card-diamonds-12.png", 10],
    "K♦": ["Playing-Cards/card-diamonds-13.png", 10],
}

keys = list(deck.keys())
random.shuffle(keys)

player = []
dealer = []

stay_counter = []


class SplashWindow(Screen):
    def close(self):
        exit()


class GameScreen(Screen):
    def __init__(self, **kwargs):
        try:
            Logger.info('GameScreen: Initializing')
            super().__init__(**kwargs)
            
            # Create PyGame-based sound player for cross-platform compatibility
            self.sound_player = PygameSoundPlayer()
            
            # Initialize sound properties with string IDs that map to the actual sound files
            Logger.info('GameScreen: Loading sounds')
            # Now our sound handling uses IDs rather than direct sound objects
            self.sound_card = self.sound_player.load('card', 'sounds/card.wav')
            self.sound_win = self.sound_player.load('win', 'sounds/win.wav')
            self.sound_lose = self.sound_player.load('lose', 'sounds/lose.wav')
            self.sound_click = self.sound_player.load('click', 'sounds/click.wav')
            
            Logger.info('GameScreen: Initialization complete')
        except Exception as e:
            Logger.error(f'GameScreen: Error in __init__: {str(e)}')
            traceback.print_exc()
    
    def play_sound(self, sound_id):
        """Play a sound using the cross-platform PyGame sound player"""
        if sound_id:
            self.sound_player.play(sound_id)

    def _clear_player_cards(self):
        """Helper to clear all player card widgets."""
        for card in ["card_one", "card_two", "card_three", "card_four", "card_five", "card_six"]:
            card_widget = getattr(self.ids, card)
            card_widget.height = "0dp"
            card_widget.source = ""

    def _clear_dealer_cards(self):
        """Helper to clear all dealer card widgets."""
        for card in ["dealer_card_down", "dealer_card_two", "dealer_card_three", "dealer_card_four", "dealer_card_five", "dealer_card_six"]:
            card_widget = getattr(self.ids, card)
            card_widget.height = "0dp"
            card_widget.source = ""

    def show_tie(self, msg):
        """Show a tie message and reset the game."""
        self.ids.prompt.text = msg
        self.reset_game()

    def show_victory(self, msg=None):
        """Show a victory dialog and reset the game on confirmation."""
        self.play_sound(self.sound_win)
        from kivymd.uix.button import MDRaisedButton
        dialog = MDDialog(
            title="Victory!",
            text=msg or "Congratulations, you won!",
            buttons=[
                MDRaisedButton(
                    text="OK",
                    on_release=lambda *a: (dialog.dismiss(), self.reset_game())
                )
            ]
        )
        dialog.open()

    def show_defeat(self, msg=None):
        """Show a defeat dialog and reset the game on confirmation."""
        self.play_sound(self.sound_lose)
        from kivymd.uix.button import MDRaisedButton
        dialog = MDDialog(
            title="Better Luck Next Time",
            text=msg or "The dealer wins this round.",
            buttons=[
                MDRaisedButton(
                    text="OK",
                    on_release=lambda *a: (dialog.dismiss(), self.reset_game())
                )
            ]
        )
        dialog.open()

    def deal_cards(self):
        """Deal initial cards to player and dealer, reset UI for new round."""
        self.play_sound(self.sound_card)
        self.ids.prompt.text = ""
        self._clear_player_cards()
        self._clear_dealer_cards()
        # Player hand
        self.player = [deck[keys[0]][1], deck[keys[1]][1]]
        # Dealer hand
        self.dealer = [deck[keys[2]][1], deck[keys[3]][1]]
        # Show dealer cards
        self.ids.dealer_card_down.source = "Playing-Cards/card-back2.png"
        self.ids.dealer_card_down.height = "150dp"
        self.ids.dealer_card_down.grow()
        self.ids.dealer_card_two.source = deck[keys[3]][0]
        self.ids.dealer_card_two.height = "150dp"
        self.ids.dealer_card_two.grow()
        # Show player cards
        self.ids.card_one.source = deck[keys[0]][0]
        self.ids.card_two.source = deck[keys[1]][0]
        self.ids.card_one.height = "150dp"
        self.ids.card_one.grow()
        self.ids.card_two.height = "150dp"
        self.ids.card_two.grow()
        self.ids.deal_button.disabled = True
        self.ids.hit_button.disabled = False
        self.ids.stay_button.disabled = False
        self.stay_counter = []
        self.check_score()

    def hit(self):
        """Deal an additional card to the player if possible."""
        self.play_sound(self.sound_card)
        p_hit_count = len(self.player) + len(self.dealer)
        card_slots = ["card_three", "card_four", "card_five", "card_six"]
        for idx, slot in enumerate(card_slots):
            card_widget = getattr(self.ids, slot)
            if card_widget.source == "":
                card_widget.source = deck[keys[p_hit_count + idx + 1]][0]
                card_widget.height = "150dp"
                card_widget.shake()
                self.player.append(deck[keys[p_hit_count + idx + 1]][1])
                break
        else:
            self.ids.hit_button.disabled = False
            self.ids.prompt.text = "You can't draw more than 6 cards!"
        self.check_score()

    def stay(self):
        """Player chooses to stay. Dealer's turn."""
        self.stay_counter.append(1)
        self.check_score()
        self.npc()

    def npc(self):
        """Dealer draws cards according to standard rules."""
        dealer_check = sum(self.dealer)
        d_hit_count = len(self.player) + len(self.dealer)
        dealer_slots = ["dealer_card_three", "dealer_card_four", "dealer_card_five", "dealer_card_six"]
        slot_offset = 1
        while dealer_check != 21 and dealer_check < 17:
            for idx, slot in enumerate(dealer_slots):
                card_widget = getattr(self.ids, slot)
                if card_widget.source == "":
                    card_widget.source = deck[keys[d_hit_count + idx + slot_offset]][0]
                    card_widget.height = "150dp"
                    card_widget.grow()
                    self.dealer.append(deck[keys[d_hit_count + idx + slot_offset]][1])
                    break
            else:
                break
            dealer_check = sum(self.dealer)
        self.stay_counter.append(1)
        self.check_score()

    def calculate_player_score(self):
        """Calculate the player's score, handling Aces as 1 or 11."""
        player_score = sum(self.player)
        while 11 in self.player and player_score > 21:
            self.player[self.player.index(11)] = 1
            player_score = sum(self.player)
        return player_score

    def calculate_dealer_score(self):
        """Calculate the dealer's score, handling Aces as 1 or 11."""
        dealer_score = sum(self.dealer)
        while 11 in self.dealer and dealer_score > 21:
            self.dealer[self.dealer.index(11)] = 1
            dealer_score = sum(self.dealer)
        return dealer_score

    def determine_winner(self):
        """Determine and display the winner based on current scores."""
        player_score = self.calculate_player_score()
        dealer_score = self.calculate_dealer_score()
        if len(self.stay_counter) == 2:
            if player_score == dealer_score:
                self.show_tie("You tied!")
            elif player_score > dealer_score and player_score <= 21:
                self.show_victory("You won!")
            elif player_score < dealer_score and dealer_score <= 21:
                self.show_defeat("The Dealer won!")
        if player_score == 21 and dealer_score == 21:
            self.show_tie("It's a tie at 21!")
        elif player_score == 21:
            self.show_victory("You won with a 21!")
        elif dealer_score == 21:
            self.show_defeat("The Dealer won with 21!")
        elif player_score > 21 and dealer_score < 21:
            self.show_defeat("You busted 21. The Dealer wins!")
        elif player_score < 21 and dealer_score > 21:
            self.show_victory("You won. The Dealer busted 21!")


    def check_score(self):
        """Check and display the winner if conditions are met."""
        self.determine_winner()

    def reset_game(self):
        """Reset the game state and UI for a new round."""
        Logger.info('GameScreen: Resetting game')
        self.play_sound(self.sound_click)
        self.ids.dealer_card_down.source = deck[keys[2]][0]
        self.ids.dealer_card_down.height = "150dp"
        self.player = []
        self.dealer = []
        self.stay_counter = []
        random.shuffle(keys)
        self.ids.deal_button.disabled = False
        self.ids.hit_button.disabled = True
        self.ids.stay_button.disabled = True
        Logger.info('GameScreen: Game reset complete')

    # functions for nav bar items

    def show_about(self):
        import webbrowser
        # Open the project's GitHub page
        webbrowser.open('https://github.com/Jdorman1289/Black_Jack')

    def donate_button(self):
        webbrowser.open("https://ko-fi.com/jessecreates", new=2)

    def close_two(self):
        sys.exit(0)


class NavBar(Screen):
    pass


class WindowManager(ScreenManager):
    pass


class BlackJack(MDApp):
    def build(self):
        try:
            Logger.info('BlackJack: Initializing app')
            Logger.info(f'BlackJack: Running on platform: {sys.platform}')
            Logger.info(f'BlackJack: Current directory: {os.getcwd()}')
            
            # Set theme properties
            Logger.info('BlackJack: Setting theme properties')
            self.theme_cls.theme_style = "Dark"
            self.theme_cls.primary_palette = "DeepPurple"
            
            # Load KV file with error handling
            kv_file = "layouts.kv"
            Logger.info(f'BlackJack: Attempting to load KV file: {kv_file}')
            if not os.path.exists(kv_file):
                Logger.error(f'BlackJack: KV file not found: {kv_file}')
                return None
                
            # Try to load the KV file
            try:
                Logger.info('BlackJack: Loading KV file')
                root = Builder.load_file(kv_file)
                Logger.info('BlackJack: KV file loaded successfully')
                return root
            except Exception as e:
                Logger.error(f'BlackJack: Error loading KV file: {str(e)}')
                traceback.print_exc()
                return None
                
        except Exception as e:
            Logger.error(f'BlackJack: Unhandled exception in build: {str(e)}')
            traceback.print_exc()
            return None


# on launch start main window class
if __name__ == "__main__":
    BlackJack().run()
