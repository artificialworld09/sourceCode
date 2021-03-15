from kivy.app import App
from kivy.uix.button import Button

class FunkyButton(Button):
	def __init__(self, **kwargs):
		super(FunkyButton, self).__init__(**kwargs)
		self.text = "Hello world"
		self.pos = (100, 100)
		self.size_hint = (None, None)
		self.size = (500, 500)

class LanguageLearnerApp(App):
    def build(self):
        return FunkyButton()
        
if __name__ == '__main__':
    LanguageLearnerApp().run()