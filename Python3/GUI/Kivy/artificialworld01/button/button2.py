from kivy.app import App
from kivy.uix.button import Button

class LanguageLearnerApp(App):
    def build(self):
        return Button(
        text="Click",
        size_hint = (.2, .05)
        )
if __name__ == '__main__':
    LanguageLearnerApp().run()