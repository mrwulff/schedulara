"""
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen,ScreenManager
from kivymd.uix.list import MDList, OneLineIconListItem,IconLeftWidget


class LoginScreen(Screen):
    pass

class HomeScreen(Screen):
    pass



class Demo2App(MDApp):
    def build(self):
        self.theme_cls.theme_style="Dark"
        
        self.sm=ScreenManager()
        self.sm.add_widget(LoginScreen(name="login"))
        self.sm.add_widget(HomeScreen(name="home"))

        screen=Builder.load_file("helper_file.kv")
        return screen
    
    def do_login(self):
        self.root.current = "home"
        for i in range(20):
            st_name = "student "
            list_item = OneLineIconListItem(text=f"student {str(i)}")
            list_item.add_widget(IconLeftWidget(icon="alpha-a-box"))

            print("this is my App:", self)
            print("this is my ScreenManager:", self.sm)
            print("this is my global app visual widget (which is equal to ScreenManager here):", self.root)
            print("this is the ScreenManager's dictionnary containing the widgets referenced with their id:", self.root.ids)
            print("this is the current Screen:",self.root.current_screen)
            print("this is current Screen dictionnary containing the widgets referenced with their id:", self.root.current_screen.ids)
            print("this is the actual MDList", self.root.current_screen.ids["users_lst"])
            self.root.current_screen.ids["users_lst"].add_widget(list_item)
Demo2App().run()
"""
