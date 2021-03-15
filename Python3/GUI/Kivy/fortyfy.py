##basics of kivy
#from kivy.app import App
#class myApplication(App):
#	pass	
#myApplication().run()


##Button
#from kivy.app import App
#from kivy.uix.button import Button

#class myApplication(App):
#	def build(self):
#		a = Button(text='Click me')
#		return a	
#myApplication().run()


##Button
#from kivy.app import App
#from kivy.uix.button import Button
'''
background_color=(255,255,255,.5) #rgb (0-255), alpha(0-1)
font_size=100
'''
#class myApplication(App):
#	def build(self):
#		a = Button(text='Click me', font_size=100)
#		return a	
#myApplication().run()

##Image
from kivy.app import App
from kivy.uix.image import Image
'''
size_hint=(0.5, 0.5)
pos_hint={'center_x':0.5, 'center_y':0.5} #(0-1)
'''
class myApplication(App):
	def build(self):
		a = Image(source='01.png', size_hint=(0.5, 0.5), pos_hint={'center_x':0.5, 'center_y':0.5})
		return a	
myApplication().run()