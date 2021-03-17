from kivy.app import App
from kivy.uix.button import Button

class FunkyButton(Button):
	def __init__(self, **kwargs):
		super(FunkyButton, self).__init__(**kwargs)
		self.text = "Hello world"
		self.pos = (100, 100)
		self.size_hint = (None, None)
		self.size = (500, 500)

class My_app(App):
    def build(self):
        return FunkyButton()
        
My_app().run()