from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.colorpicker import ColorPicker

class PaletteApp(App):
    def build(self):
        layout = BoxLayout(orientation="vertical", spacing=10, padding=10)

        # Create a button
        self.button = Button(
            text="Color Preview",
            background_color=[1, 1, 1, 1],
            size_hint=(1, 0.2),
            font_size=20
        )

        # Create a color picker
        self.picker = ColorPicker()
        self.picker.bind(color=self.change_color)

        # Add widgets to layout
        layout.add_widget(self.picker)
        layout.add_widget(self.button)

        return layout

    def change_color(self, instance, value):
        self.button.background_color = value
        # Optional: update the text color to contrast with the background
        if sum(value[:3]) / 3 < 0.5:
            self.button.color = [1, 1, 1, 1]
        else:
            self.button.color = [0, 0, 0, 1]

PaletteApp().run()
