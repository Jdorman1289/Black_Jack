from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen


# The different screens
class MainWindow(Screen):
    pass
    
    

class WindowTwo(Screen):
    pass

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file('path to kv')



class Wx(App):
    def build(self):
        return kv


# on launch start main window class
if __name__ == "__main__":
    Wx().run()
