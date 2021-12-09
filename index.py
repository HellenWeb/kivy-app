
# Modules

from random import randint
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

# Window Settings

Window.size = (300, 200)
Window.title = ('Application')

# Class "Application"

class Application(App):

    def __init__(self):
        super().__init__()
        self.label = Label(text="...")

    def press(self, *args):
            self.label.text = (str(randint(0, 100000000)))

    def build(self):
        box = BoxLayout()
        button = Button(text="Get Number")
        button.bind(on_press=self.press)
        box.add_widget(button)
        box.add_widget(self.label)

        return box

# __name__ == __main___

if __name__ == '__main__':
    Application().run()
