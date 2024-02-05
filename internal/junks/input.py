from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.uix.button import MDButton, MDFlatButton

from kivymd_extensions.sweetalert import SweetAlert

KV = """
MDScreen:

    MDButton:
        text: "EXAMPLE"
        pos_hint: {"center_x": .5, "center_y": .5}
        on_release: app.show_dialog()
"""


class Test(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def show_dialog(self):
        button_ok = MDButton(
            text="OK",
            font_size=16,
            on_release=self.callback,
        )
        button_cancel = MDFlatButton(
            text="CANCEL",
            font_size=16,
            on_release=self.callback,
        )
        self.alert = SweetAlert()
        self.alert.fire(
            "Your public IP",
            buttons=[button_ok, button_cancel],
        )

    def callback(self, instance_button):
        logging.info(self.alert, instance_button)


Test().run()
