from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

from kivymd.app import MDApp
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog

KV = '''
<Content>
    orientation: "vertical"
    spacing: "12dp"
    size_hint_y: None
    height: "120dp"

    MDTextField:
        id: city
        hint_text: "City"

    MDTextField:
        id: street
        hint_text: "Street"


MDFloatLayout:

    MDFlatButton:
        text: "ALERT DIALOG"
        pos_hint: {'center_x': .5, 'center_y': .5}
        on_release: app.show_confirmation_dialog()
'''


class Content(BoxLayout):
    pass


class Example(MDApp):
    dialog = None

    def build(self):
        return Builder.load_string(KV)
    
    def logging.info_street():
        street_name = self.dialog.content_cls.ids.street.text
        logging.info(street_name)

    def show_confirmation_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title="Address:",
                type="custom",
                content_cls=Content(),
                buttons=[
                    
                    MDFlatButton(
                                    text="CANCEL", text_color=self.theme_cls.primary_color,
                                ),
                    
                    MDFlatButton(text = "logging.info",               
                                 on_press=self.logging.info_street
                                ),
                        ],
            )
        self.dialog.open()
    
    
    
    def logging.info_city(city_name):
        logging.info(city_name)

    def logging.info_street(street_name):
        logging.info(street_name)



Example().run()