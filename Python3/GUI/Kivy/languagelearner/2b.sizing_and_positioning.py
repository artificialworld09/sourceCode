from kivy.app import App
from kivy.uix.button import Button
'''
pos = (50, 50) #to change position
size_hint = (.8, .8)
size = (300, 100), size_hint = (None, None) #to change static size

32:15/59:01
'''
class FunkyButton(Button):
	def __init__(self, **kwargs):
		super(FunkyButton, self).__init__(**kwargs)
		self.text = "Hello world"
		self.pos = (100, 100)
		self.size_hint = (.25, .25)

class LanguageLearnerApp(App):
    def build(self):
        return FunkyButton()
        
if __name__ == '__main__':
    LanguageLearnerApp().run()