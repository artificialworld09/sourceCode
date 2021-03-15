from kivy.app import App
from kivy.uix.button import Button
'''
pos = (50, 50) #to change position
size_hint = (.8, .8)
size = (300, 100), size_hint = (None, None) #to change static size

23:11/59:01
'''

class LanguageLearnerApp(App):
    def build(self):
        return Button(
        text="Hello world",
        pos = (50, 50),
        size_hint = (.8, .8)
        )
if __name__ == '__main__':
    LanguageLearnerApp().run()
    
