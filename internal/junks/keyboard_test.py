from kivy.app import App
from kivy.core.window import Window
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button


class MyApp(App):
    def build(self):
        self.my_keyboard = Window.request_keyboard(self.my_keyboard_down, self.root)
        self.my_keyboard.bind(on_key_down=self.my_keyboard_down)

        widget = FloatLayout()

        text_input = TextInput(multiline=False)
        widget.add_widget(text_input)

        print_text = lambda arg: print(text_input.text)
        widget.add_widget(
            Button(on_press=print_text, size_hint=[0.2, 0.2], text="press pls")
        )

        return widget

    def my_keyboard_down(self, keyboard, keycode, text, modifiers):
        if keycode[1] == "escape":
            quit()
        if keycode[1] == "right":
            print("right")
        if keycode[1] == "left":
            print("left")


if __name__ == "__main__":
    MyApp().run()
