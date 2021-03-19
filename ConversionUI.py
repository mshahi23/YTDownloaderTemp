from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.uix.label import Label
from conversion_therapy import intro


def error(flag):
    content = BoxLayout(orientation='vertical')
    if flag == 1:
        message_label = Label(text="URL is empty")
    if flag == 2:
        message_label = Label(text="Please select a file type")
    if flag == 3:
        message_label = Label(text="The URL is invalid or not supported")
    dismiss_button = Button(text='OK')
    content.add_widget(message_label)
    content.add_widget(dismiss_button)
    popup = Popup(title='Error', content=content, size_hint=(0.3, 0.25))
    dismiss_button.bind(on_press=popup.dismiss)
    popup.open()


class UI(FloatLayout):
    def submit(self):
        url = self.ids['urlInput'].text
        if self.ids['mp3Box'].active:
            filetype = "mp3"
        elif self.ids['mp4Box'].active:
            filetype = "mp4"
        elif self.ids['gifBox'].active:
            filetype = "gif"
        else:
            filetype = ""

        string = self.ids['output'].text + "\n"
        flag = intro(url, filetype)
        if flag == 1:
            string = string + "URL is empty"
            self.ids['output'].text = string
            error(flag)
        elif flag == 2:
            string = string + "Please select a file type"
            self.ids['output'].text = string
            error(flag)
        elif flag == 3:
            string = string + "The URL is invalid or not supported"
            self.ids['output'].text = string
            error(flag)
        else:
            string = string + flag
            self.ids['output'].text = string


class ConversionApp(App):
    def build(self):
        return UI()


if __name__ == '__main__':
    ConversionApp().run()
