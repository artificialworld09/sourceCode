from kivy.app import App
from kivy.uix.button import Button

class myApplication(App):
    def build(self):
        a = Button(
        text="Click",
        size_hint = (.2, .05),
        pos_hint={'center_x':0.5, 'center_y':0.5},
        font_size=100
        )
        return a
myApplication().run()