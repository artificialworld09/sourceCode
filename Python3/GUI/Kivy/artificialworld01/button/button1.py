from kivy.app import App
from kivy.uix.button import Button

class myApplication(App):
    def build(self):
        a = Button(
        text="Click"
        )
        return a
myApplication().run()