from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivy.uix.screenmanager import Screen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelTwoLine
from kivymd.uix.list import MDList
from kivy.properties import StringProperty, ListProperty
from kivy.core.window import Window

Window.size = (300, 500)


class MenuScreen(Screen):
    pass


class Content(MDList):
    pass


class AnotherContent(MDList):
    pass


class RecipeLine(MDBoxLayout):
    text = StringProperty()


class IngContent:
    items = ListProperty


class GroceryApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.list_items = []
        self.dialog = None

        self.card_file = [
            {
                "Category": "Chicken",
                "Recipes": [
                    {
                        "title": "Chicken Adobo",
                        "shopping list": ["Fish", "parchment paper", "tomatoes"],
                    },
                    {
                        "title": "Chicken Noodle Soup",
                        "shopping list": ["ground beef", "cheese", "buns"],
                    },
                ],
            },
            {
                "Category": "Pork",
                "Recipes": [
                    {
                        "title": "Pork Adobo",
                        "shopping list": ["Bacon", "spices", "tomatoes"],
                    },
                    {
                        "title": "Pork Burger",
                        "shopping list": ["ground pork", "cheese", "buns"],
                    },
                ],
            },
        ]

    def build(self):
        self.theme_cls.primary_palette = "Pink"
        self.theme_cls.theme_style = "Dark"
        return Builder.load_file("main.kv")

    def on_start(self):
        for category in self.card_file:
            panel = MDExpansionPanel(
                icon="recipe.png",
                content=Content(),
                panel_cls=MDExpansionPanelTwoLine(
                    text=category["Category"], secondary_text="Tap to view recipes"
                ),
            )
            self.root.ids.sm.get_screen("menu").ids.rlist.add_widget(panel)

            for recipe in category["Recipes"]:
                rw = RecipeLine(text=recipe["title"])
                self.root.ids.sm.get_screen("menu").ids.rlist.children[
                    0
                ].content.add_widget(rw)

    def showinfo(self, category, recipe):
        close_button = MDFlatButton(text="Done", on_release=self.close_dialog)
        add_button = MDFlatButton(text="Add to list", on_release=self.close_dialog)

        for c in self.card_file:
            if c["Category"] == category:
                for r in c["Recipes"]:
                    if r["title"] == recipe:
                        print(r["shopping list"])

        ing = IngContent(
            items=ingredient_list(category, recipe)
        )  # I'm also getting unresolved reference on ingredient_list
        self.dialog = MDDialog(
            size_hint=(0.8, 0.8),
            text="Ingredients:",
            content=ing,
            auto_dismiss=True,
            buttons=[close_button, add_button],
        )
        self.dialog.open()

    def close_dialog(self, obj):  # Method that close the dialog box
        self.dialog.dismiss()


GroceryApp().run()
