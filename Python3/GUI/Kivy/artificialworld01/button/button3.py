from kivy.app import App
from kivy.uix.button import Button

class LanguageLearnerApp(App):
    def build(self):
        return Button(
        text="Click",
        size = (300, 100), size_hint = (None, None)
        )
if __name__ == '__main__':
    LanguageLearnerApp().run()