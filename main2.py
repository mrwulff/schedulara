from kivymd.app import MDApp
from kivy.app import App
from libs.uix.root import Root
from kivymd.uix.menu import MDDropdownMenu
from kivy.utils import hex_colormap


class Demo3App(MDApp):
    menu: MDDropdownMenu = None

    def open_menu(self, menu_button):
        menu_items = []
        for item, method in {
            "Set palette": lambda: self.set_palette(),
            "Switch theme style": lambda: self.theme_cls.switch_theme(),
            "Disabled widgets": lambda: self.disabled_widgets(),
        }.items():
            menu_items.append(
                {
                    "text": item,
                    "on_release": method,
                }
            )
        self.menu = MDDropdownMenu(
            caller=menu_button,
            items=menu_items,
        )
        self.menu.open()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Window.bind(on_keyboard=self.keyboard)

        # self.title = "Kivy - Lazy Load"

        # Window.keyboard_anim_args = {"d": 0.2, "t": "linear"}
        # Window.softinput_mode = "below_target"

    def build(
        self,
    ):
        self.root = Root()

    def md2(self):
        self.root.set_current("md2")
        print("md2")

    def on_start(self):
        global x
        global ad
        app = App.get_running_app()
        ad = app.user_data_dir

        if 1 == 1:
            config_file = ad
        # print(tic - time.perf_counter(), "on start !!!")
        import libs.lib_readuserdata

        try:
            x = libs.lib_readuserdata.readuserdata(App, config_file, False)
            print("read user data at begining")
        except:
            import libs.lib_makeuserdata

            libs.lib_makeuserdata.makeuserdata(App, config_file, False)
            x = libs.lib_readuserdata.readuserdata(App, config_file, False)
            print("made user data at begining!!!!!")
        if 1 == 1:
            # try:
            self.theme_cls.theme_style = x["theme"]
            self.theme_cls.primary_palette = x["pcolor"]

        # except:
        #    pass
        # print(x, "lol")

        # self.do_login("", useold)
        # self.theme_cls.switch_theme()
        x1 = self.theme_cls.theme_style
        x2 = self.theme_cls.primary_palette
        # x3 = self.theme_cls.accent_palette
        # x4 = self.theme_cls.material_style
        # self.theme_cls.switch_theme()
        print(x1, x2, "THEME STUFF")
        self.md2()

    def switch_palette(self, selected_palette):
        self.theme_cls.primary_palette = selected_palette
        print("switch palet")

    def set_palette(self):
        instance_from_menu = self.get_instance_from_menu("Set palette")
        available_palettes = [
            name_color.capitalize() for name_color in hex_colormap.keys()
        ]

        menu_items = []
        for name_palette in available_palettes:
            print(name_palette)
            menu_items.append(
                {
                    "text": name_palette,
                    "on_release": lambda x=name_palette: self.switch_palette(x),
                    # "md_bg_color": name_palette,
                }
            )
        MDDropdownMenu(
            caller=instance_from_menu,
            items=menu_items,
        ).open()

    def get_instance_from_menu(self, name_item):
        index = 0
        rv = self.menu.ids.md_menu
        opts = rv.layout_manager.view_opts
        datas = rv.data[0]

        for data in rv.data:
            if data["text"] == name_item:
                index = rv.data.index(data)
                break

        instance = rv.view_adapter.get_view(index, datas, opts[index]["viewclass"])
        return instance

    def disabled_widgets(self):
        for widget in self.root.ids.widget_box.children:
            widget.disabled = not widget.disabled

        for widget in self.root.ids.custom_widget_box.children:
            widget.disabled = not widget.disabled


Demo3App().run()
