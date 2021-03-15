from kivy.app import App
from kivy.uix.image import Image

class myApplication(App):
	def build(self):
		a = Image(source='01.png', size_hint=(0.5, 0.5), pos_hint={'center_x':0.5, 'center_y':0.5})
		return a	
myApplication().run()