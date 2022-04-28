import time
import sys

tic = time.perf_counter()
from libs.uix.root import Root

ios = True
notch = True
debug = True
scale = 2
useold = False
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.properties import StringProperty
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.list import IRightBodyTouch
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.app import App
from kivy.config import Config

from kivy.utils import platform
from kivymd.uix.snackbar import Snackbar
from kivymd.toast import toast

from kivymd.uix.picker import MDThemePicker
from kivymd.uix.picker import MDTimePicker
from kivymd.uix.picker import MDDatePicker
from kivy.uix.popup import Popup


import datetime


"""
from audioop import ratecv
from kivy.lang import Builder

from kivymd.uix.list import (
    MDList,
    ThreeLineIconListItem,
    TwoLineIconListItem,
    IconLeftWidget,
)

from kivymd.uix.menu import MDDropdownMenu
from kivy.clock import Clock
from kivymd.uix.textfield import MDTextField


# from kivy.effects.dampedscroll import DampedScrollEffect

print(platform, "KIVY PLATFORM")
if platform == "linux":
    print("omgitslinux")
if platform == "win":
    notch = False
    scale = 1


from kivymd.uix.button import MDRectangleFlatIconButton

from kivy.uix.button import Button
from kivy.core.clipboard import ClipboardBase

# from kivycupertino.uix.slider import CupertinoSlider


from kivy.uix.textinput import TextInput

import json
from appdirs import *
import ssl
import logging

ssl.verify = False
mjds = []


from kivy.uix.spinner import Spinner, SpinnerOption
from kivy.uix.dropdown import DropDown
import webcolors




from kivy.core.window import Window

from kivymd.uix.dialog import MDDialog
from math import sin
from kivy_garden.graph import Graph, MeshLinePlot, LinePlot
from kivy.properties import NumericProperty
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.button import MDFlatButton
from kivymd.uix.behaviors.toggle_behavior import MDToggleButton


import os
"""
w = 1125 / 3
h = 2436 / 3
if platform == "win":

    Config.set("graphics", "width", str(w))
    Config.set("graphics", "height", str(h))
    Window.size = (w, h)
"""
HOME = os.environ.get("HOME", "/")
BUNDLE = os.environ.get("KIVY_BUNDLE_ID", "/")
os.environ["PYTHON_EGG_CACHE"] = f"{HOME}/Library/Caches/{BUNDLE}"
config_file = f"{HOME}/Library/Caches/{BUNDLE}"
print(config_file, "THIS IS THE CONFIG FILE", platform)

# if platform=='win':
#    app = App.get_running_app()
#    config_file=app.user_data_dir


import datetime
import humanize
import lib_createcache
import lib_parse
import lib_makeuserdata
import lib_readuserdata
import lib_tinyfs
import lib_think
import lib_ppdownloader
import lib_updateuserdata
import lib_extractjson
import lib_makegraphs
import lib_bonus
import lib_webserver
import paydays
import time
import webbrowser
import shutil

from functools import partial
"""
toc1 = time.perf_counter()
print(tic - toc1, "firsttimer")

"""
class SpinnerOptions(SpinnerOption):
    def __init__(self, **kwargs):
        super(SpinnerOptions, self).__init__(**kwargs)
        self.background_normal = ""
        self.background_color = [0, 0, 1, 1]  # blue colour

        self.height = 26



class SpinnerDropdown(DropDown):
    def __init__(self, **kwargs):
        super(SpinnerDropdown, self).__init__(**kwargs)
        self.auto_width = False
        self.width = 150




class SpinnerWidget(Spinner):
    def __init__(self, **kwargs):
        super(SpinnerWidget, self).__init__(**kwargs)
        self.dropdown_cls = SpinnerDropdown
        self.option_cls = SpinnerOptions
        ...
"""


class AboutScreen(Screen):
    pass


class TrophyScreen(Screen):
    pass


class StatsScreen(Screen):
    pass


class LoginScreen(Screen):
    pass


class MainMenuScreen(Screen):
    pass


class HomeScreen(Screen):
    pass


class HistoryScreen(Screen):
    pass


class PayScreen(Screen):
    pass


class YourContainer(IRightBodyTouch, MDBoxLayout):
    adaptive_width = True


class YourContainer2(IRightBodyTouch, MDBoxLayout):
    adaptive_width = False
    size_hint = (0.9, 0.9)


class HistoryItem(Screen):
    text = StringProperty()


class AnimateMoneyScreen(Screen):
    text = StringProperty()


class PayItem(Screen):
    text = StringProperty()


class NewSlider(Screen):
    text = StringProperty()


from kivy.uix.label import Label


class MD3Card(Screen):
    text = StringProperty()


class SmoothLabel(Label):
    pass


class DialogContent(MDBoxLayout):
    """OPENS A DIALOG BOX THAT GETS THE TASK FROM THE USER"""

    # from datetime import datetime

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # set the date_text label to today's date when useer first opens dialog box
        now = datetime.datetime.now()
        self.ids.newhours.text = now

    def show_date_picker(self):
        """Opens the date picker"""
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.on_save)
        date_dialog.open()

    def on_save(self, instance, value, date_range):
        """This functions gets the date from the date picker and converts its it a
        more friendly form then changes the date label on the dialog to that"""

        date = value.strftime("%A %d %B %Y")
        self.ids.date_text.text = str(date)


class SwipeToDeleteItem(Screen):

    text = StringProperty()

    def click(self, *args):
        global idex
        global mjds

        idex = self.ids.idmdlabel.text

        try:
            junk, idex = str.split(idex, "***")
            idex = int(idex)
            newxxx = xxx[idex]
        except:
            """"""
            newxxx = []
        try:
            rate = lib_extractjson.extract_pos(App, config_file, xxx[idex][8])
            App.get_running_app().root.current_screen.ids["rate"].text = rate
        except:
            App.get_running_app().root.current_screen.ids["rate"].text = "?"
        from datetime import datetime

        now = datetime.now()
        try:
            today, fdate = lib_tinyfs.format_text(idex, mjds, now, "info")
            # print("OMGWHATHAVEYOPUDONE ", idex)
        except:
            # print("omgwhathaveyoudone ", idex)
            pass
        try:
            App.get_running_app().root.current_screen.ids["date"].text = fdate
            # App.get_running_app().root.current_screen.ids['d0'].text=str(newxxx[0])
            # App.get_running_app().root.current_screen.ids['d1'].text=str(newxxx[1])
            App.get_running_app().root.current_screen.ids["jobid"].text = str(newxxx[2])
            App.get_running_app().root.current_screen.ids["show"].text = str(newxxx[3])
            App.get_running_app().root.current_screen.ids["venue"].text = str(newxxx[4])
            App.get_running_app().root.current_screen.ids["location"].text = str(
                newxxx[5]
            )
            App.get_running_app().root.current_screen.ids["client"].text = str(
                newxxx[6]
            )
            App.get_running_app().root.current_screen.ids["type"].text = str(newxxx[7])
            App.get_running_app().root.current_screen.ids["wrench"].text = str(
                newxxx[8]
            )
            App.get_running_app().root.current_screen.ids["status"].text = str(
                newxxx[10]
            )
            App.get_running_app().root.current_screen.ids["notes"].text = str(
                newxxx[11]
            )
            App.get_running_app().root.current_screen.ids["d12"].text = str(newxxx[12])
            App.get_running_app().root.current_screen.ids["d13"].text = str(newxxx[9])
            App.get_running_app().root.current_screen.ids["d10"].text = str(newxxx[13])
            if newxxx[8] == "ME":
                App.get_running_app().root.current_screen.ids[
                    "pos"
                ].icon = "power-socket-us"
            App.get_running_app().root.current_screen.ids["image"].source = (
                "images/" + x["city"] + ".png"
            )
        except:
            (newxxx)

        # print(mjds[idex]["location"], "WTHMAN")

        try:

            App.get_running_app().root.current_screen.ids["image"].source = (
                "images/" + mjds[idex]["venue"].upper() + ".png"
            )
        except:
            App.get_running_app().root.current_screen.ids["image"].source = (
                "images/" + x["city"] + ".png"
            )


class ContentNavigationDrawer(Screen):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class P(FloatLayout):

    pass


class Prestore(FloatLayout):

    pass


from kivymd.uix.button import MDRaisedButton

"""
class MyToggleButton(MDRaisedButton, MDToggleButton):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_down = self.theme_cls.primary_light
"""


class MyLabel(Screen):
    def on_size(self, *args):
        self.text_size = self.size


from kivymd.uix.card import MDCard


class BlankMDCard(MDCard):
    text = StringProperty()
    text2 = StringProperty()


newcolor = (0.2, 0.2, 0.2)
x = ""
ad = ""
xxx = ""
idex = 1
browser = ""
plus_search = 0


class Content(FloatLayout):
    pass


"""
class CountDownLbl(Label):
    angle = NumericProperty(0)
    startCount = NumericProperty(20)
    Count = NumericProperty()

    def __init__(self, **kwargs):
        super(CountDownLbl, self).__init__(**kwargs)
        Clock.schedule_once(self.set_Circle, 0.1)
        self.Count = self.startCount
        Clock.schedule_interval(lambda x: self.set_Count(), 1)

    def set_Count(self):
        self.Count = self.Count - 1

    def set_Circle(self, dt):
        self.angle = self.angle + dt * 360
        if self.angle >= 360:
            self.angle = 0
        Clock.schedule_once(self.set_Circle, 0.1)
"""

x = []


class Demo3App(MDApp):
    scale = 1
    # print("omg")
    print(tic - time.perf_counter(), "supershort")
    cspacing = 10
    mtype = "top"
    bradius = 10 * scale
    radius = 10 * scale
    mheight = 40
    cpadding = 20
    sound_effects = ["Ding", "Bang", "Lol"]

    def check_att(self, b):
        global x
        global ad

        app = App.get_running_app()
        ad = app.user_data_dir
        # config_file=ad

        if ios == True:
            import libs.lib_readuserdata

            x = libs.lib_readuserdata.readuserdata(App, ad, ios)
        try:
            # print(x[b], "checkingx[b]")
            pass
        except:
            # print("cant do that")
            x[b] = False
            app = App.get_running_app()
            ad = app.user_data_dir
            # print(ad, "adadadad33")
            libs.lib_updateuserdata.updateuser(x, ad)
        # print(x, "XSUBB")
        return x[b]

    def check_pull_refresh(self, view, grid):
        pass

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.title = "Kivy - Lazy Load"

        Window.keyboard_anim_args = {"d": 0.2, "t": "linear"}
        Window.softinput_mode = "below_target"

    def build(self):
        self.root = Root()
        self.root.set_current("home")

    def on_start(self):
        global x
        global ad
        # print("wtf")
        app = App.get_running_app()
        ad = app.user_data_dir
        # if ios == True:
        if 1 == 1:
            config_file = ad
        print(tic - time.perf_counter(), "on start !!!")
        import libs.lib_readuserdata

        try:
            x = libs.lib_readuserdata.readuserdata(App, config_file, ios)
        except:
            import libs.lib_makeuserdata

            libs.lib_makeuserdata.makeuserdata(App, config_file, ios)
            x = libs.lib_readuserdata.readuserdata(App, config_file, ios)
        try:
            self.theme_cls.theme_style = x["theme"]
            self.theme_cls.primary_palette = x["pcolor"]
            self.theme_cls.accent_palette = x["scolor"]
        except:
            pass
        print(x)

        self.do_login("", useold)

    def do_login(self, search, useold):
        print("do_login")

        # if pf[0]!='W':
        # if 1==1:
        # from lib_test import n22
        # n22()

        global xxx
        global mjds
        global config_file
        global plus_search
        good_login = False
        from datetime import datetime

        now = datetime.now()
        app = App.get_running_app()
        config_file = app.user_data_dir

        self.root.current = "home"
        self.root.current_screen.ids["users_lst"].clear_widgets()
        # print(x, "USECACHETEST")

        if x["usecache"] == "True" or x["usecache"] == True:
            print("Using Cache2")
            import libs.lib_createcache as lib_createcache
            from random import randrange

            lib_createcache.createcache(ad, randrange(1, 40, 10))
        sch = ad + "/conf.html"

        if x["usecache"] == "False" or x["usecache"] == False:
            print("Using Live Data")
            if useold == False:
                if x["refreshreload"] == True:
                    good_login = lib_think.login(ad, x, ios, App)
                    good_login = True

                if good_login == True:
                    print("GOOD LOGIN SIR")
                    sch = ad + "/realdata.html"
                if x["refreshreload"] == False:
                    try:
                        sch = ad + "/realdata.html"
                    except:
                        print("realdata not found")

        import libs.lib_parse

        # print(ad, "ADADAD")

        xxx, mjds = libs.lib_parse.parse(sch, ad, x["usecache"], x)

        try:
            cf, week, tot = libs.lib_tinyfs.stats(xxx, now, search)
        except:
            import libs.lib_tinyfs

            cf, week, tot = libs.lib_tinyfs.stats(xxx, now, search)

        founddates = ""
        if len(search) > 0:
            founddates = (
                str(tot)
                + "/"
                + str(len(xxx) - 1)
                + "dates matching: "
                + str(search)
                + "\n"
            )

        texta = (
            "[size=18 sp]"
            + founddates
            + str(cf)
            + "/"
            + str(tot)
            + " confirmed dates\n"
            + str(week)
            + " gigs this week[size=1 sp]***0"
        )

        indexnumber = 0
        indexnumber_real = -1
        self.root.current_screen.ids["users_lst"].add_widget(
            SwipeToDeleteItem(text=texta)
        )
        toc3 = time.perf_counter()
        print(tic - toc3, "toc3time")
        if cf < tot:
            indexnumber = indexnumber + 1
            texta = (
                "Click To Confirm"
                + str(tot - cf)
                + " gigs [size=1 sp]***"
                + str(indexnumber)
            )
            self.root.current_screen.ids["users_lst"].add_widget(
                SwipeToDeleteItem(text=texta)
            )
        # App.get_running_app().root.current_screen.ids['istoday'].text='wow'

        plus_search = 0
        for i in range(len(mjds)):
            # lib_bonus.create_notification(mjds[i],x)
            texta = libs.lib_tinyfs.format_text(i, mjds, now, "index")
            indexnumber = indexnumber + 1
            indexnumber_real = indexnumber_real + 1
            texta = texta + str(indexnumber_real)
            if search.lower() in str(xxx[i]).lower() or len(search) == 0:
                # print("omg its working")
                plus_search = plus_search + 1

                self.root.current_screen.ids["users_lst"].add_widget(
                    SwipeToDeleteItem(text=texta)
                )

        print(
            plus_search,
            "plussearch",
            len(mjds),
            (tic - time.perf_counter(), "after schedule"),
        )
        toast(str(tic - time.perf_counter()))
        return good_login

    def do_settings(self):
        global x
        # print(x)
        self.root.set_current("settings")
        # sm.set_current("settings")
        try:
            self.root.get_screen("notification").ids["slider2"].value = x["not2time"]
            self.root.get_screen("notification").ids["slider1"].value = x["not1time"]

            self.root.get_screen("notification").ids["disable1"].active = x["not1"]
            self.root.get_screen("notification").ids["disable2"].active = x["not2"]

            if x["not"] == True:
                App.get_running_app().root.current_screen.ids[
                    "switchnotify"
                ].active = True

            tog1 = App.get_running_app().root.current_screen.ids["switchnotify"].active
        except:
            x["not2time"] = 0
            x["not1time"] = 0
            x["not1"] = False
            x["not2"] = False
            x["not"] = False
        # print (tog1)
        import libs.lib_updateuserdata

        libs.lib_updateuserdata.updateuser(x, ad)

    """
    class Demo3App2(MDApp):
        scale = 2
        if platform[0] == "w":
            scale = 1
            notch = False
        # def __init__(self, **kwargs):
        #    self.snackbar = None
        global idex
        iii = idex
        bud2 = "65"
        global x
        x = x

        locations = [
            "denver",
            "dc",
            "florida",
            "georgia",
            "indiana",
            "kentucky",
            "lasvegas",
            "losangeles",
            "louisiana",
            "michigan",
            "minnesota",
            "missouri",
            "mississippi",
            "montana",
            "newmexico",
            "northerncalifornia",
            "northwest",
            "ohio",
            "reno",
            "california",
            "southcarolina",
            "tempe",
            "memphis",
            "texas",
            "tucson",
            "wisconsin",
        ]
        newercolor = newcolor
        xxxx = xxx + "wtf" + str(idex)
        
        
        if notch == True:
            mheight = 120
        else:
            mheight = 45
        cpadding = 20
        cspacing = 10
        mtype = "top"
        bradius = 10 * scale
        radius = 10 * scale
        # mfontel='fonts/SourceSansPro-ExtraLight.ttf'
        # mfontb='fonts/SourceSansPro-Bold.ttf'
        # mfont='fonts/SourceSansPro-Regular.ttf'
        


        notheight = 200 * scale
        

        angle = NumericProperty(0)
        startCount = NumericProperty(20)
        Count = NumericProperty()
"""
    notheight = 200 * scale
    ot = ["8", "10", "0", "1", "2", "3", "4", "5", "6", "7", "9"]
    lunch = ["0", "1", "2"]
    dialog = None

    snackbar = None
    rreverse = True
    menurotate = 10
    menuscale = 0.5, 0.5

    def set_Circle(self, dt):
        self.angle = self.angle + dt * 360
        if self.angle >= 360:
            self.angle = 0
        Clock.schedule_once(self.set_Circle, 0.1)

    def set_Count(self):
        self.Count = self.Count - 1

    def callback_for_menu_items(self, text):
        self.menu.dismiss()
        toast(text)

    def menu_callback(self, text_item, v, v2):
        # print(location[text_item])
        # print (text_item,type(text_item))
        # print(v[text_item], "v[text")
        App.get_running_app().root.current_screen.ids["button4"].text = v[text_item]
        # self.root.get_screen("notification").ids['button4'].text=v[text_item]
        global x
        x[v2] = v[text_item]
        # print(x)
        lib_updateuserdata.updateuser(x, ad)

    def choose_drop(self, v, v2):
        "oll"

        menu_items = [
            {
                "text": f"{v[i]}",
                # "scroll_type": ['bars'],
                # "effect_cls": "ScrollEffect",
                "viewclass": "OneLineListItem",
                "on_release": lambda x=i: self.menu_callback(x, v, v2),
            }
            for i in range(len(v) - 1)
        ]
        print(self.root.get_screen("notification").ids)
        self.menu = MDDropdownMenu(
            caller=self.root.get_screen("notification").ids["button4"],
            items=menu_items,
            max_height=400,
            # position="center",
            width_mult=4,
        )
        # self.menu.caller = button4
        self.menu.open()

    def format_minutes(self, t, v, d):
        # v=5
        if d == True:
            return t + " Notification will be sent " + str(v) + " minutes before call"
        if d == False:
            return t + " Notification disabled"

    def enable_nots(self):
        global x
        self.root.current = "settings"
        tog1 = App.get_running_app().root.current_screen.ids["switchnotify"].active
        # print(tog1, x)
        x["not"] = tog1
        import libs.libs_updateuserdata

        libs.lib_updateuserdata.updateuser(x, ad)

    def loadnots(self, sslider):
        global x

        self.root.current = "notification"

        if x["not1"] == True:
            App.get_running_app().root.current_screen.ids["disable1"].active = True

        if x["not2"] == True:
            App.get_running_app().root.current_screen.ids["disable2"].active = True
        App.get_running_app().root.current_screen.ids["slider2"].value = x["not2time"]
        try:
            App.get_running_app().root.current_screen.ids["slider2"].value = x[
                "not2time"
            ]
            App.get_running_app().root.current_screen.ids["slider1"].value = x[
                "not1time"
            ]
        except:
            print("rip")
        lib_updateuserdata.updateuser(x, ad)

    def makenots(self, sslider):
        from kivymd.uix.expansionpanel import (
            MDExpansionPanel,
            MDExpansionPanelThreeLine,
            MDExpansionPanelOneLine,
        )

        global x
        # self.root.current = "notification"
        self.root.set_current("notification")
        try:
            App.get_running_app().root.current_screen.ids["button4"].text = x[
                "sound_effects"
            ]
        except:
            App.get_running_app().root.current_screen.ids["button4"].text = "Normal"

        first = str(
            App.get_running_app().root.current_screen.ids["slider" + sslider].value
        )
        # App.get_running_app().root.current_screen.ids['text'+sslider].text=first

        text1 = str(App.get_running_app().root.current_screen.ids["slider1"].value)
        text2 = str(App.get_running_app().root.current_screen.ids["slider2"].value)
        tog1 = App.get_running_app().root.current_screen.ids["disable1"].active

        tog2 = App.get_running_app().root.current_screen.ids["disable2"].active

        x["not1"] = tog1
        x["not1time"] = text1

        x["not2"] = tog2
        x["not2time"] = text2
        import libs.lib_updateuserdata

        libs.lib_updateuserdata.updateuser(x, ad)
        try:
            self.root.current_screen.ids["box"].remove_widget(content.parent)

        except:
            print("omg")

    def trophys(self):
        # import lib_test
        # lib_test.n22()
        pass

    def make_stats(self):
        from kivy.utils import get_color_from_hex

        self.root.current = "stats"
        self.root.current_screen.ids["graphs"].clear_widgets()
        dd, dd2, maxd, maxm, max_dy, max_my = lib_makegraphs.parsepp(self, ad, "check")
        # print (dd[1])
        lib_makegraphs.make_stats_pp(self, "Checks", dd, maxm, max_dy)

        # print (dd[1])

        lib_makegraphs.make_stats_pp(self, "$/Day", dd2, maxd, max_dy)

        # self.root.current_screen.ids["graphs"].add_widget(MD3Card(text="wow"))
        stats = [
            "stat1: 5667",
            "stat2: 1567",
            "stat3: 5671",
            "stat4: 5o67",
        ]
        self.root.current_screen.ids["graphs"].add_widget(
            BlankMDCard(text="Current YTD", text2="coming soon")
        )
        self.root.current_screen.ids["graphs"].add_widget(
            BlankMDCard(text="Current Year", text2="soming soon!")
        )

    def maketransp(self):

        x = self.theme_cls.primary_color
        x[3] = 0.3
        return x

    def menuu(self):
        self.do_login("", useold)

    def mainmenuf(self):
        self.root.set_current("mainmenu")
        # self.root.current_screen.ids["payperiod_list"].clear_widgets()

    def dlpp(self):
        import libs.lib_ppdownloader as lib_ppdownloader

        paystubs, new = lib_ppdownloader.thinkpp(x, ad)
        self.snackbar = Snackbar(
            text="Downloaded " + str(new) + " Paystubs out of " + str(paystubs),
            bg_color=self.theme_cls.primary_color,
        )
        self.snackbar.open()

    def ccc(self):
        # print(xxx)
        confable = []
        for i in range(len(xxx)):

            try:
                z = xxx[i][13]
                z.append(confable)
            except:
                pass
        # for i in range(len(confable)):
        #    print(confable[i])
        self.snackbar = Snackbar(text="Success!", bg_color=self.theme_cls.primary_color)
        self.snackbar.open()

    def animate_money(self):
        self.root.current = "animate"
        pos = mjds[idex]["pos"]
        self.root.get_screen("animate").ids["top"].secondary_text = str("call start")
        self.root.get_screen("animate").ids["moneyinfo"].secondary_text = str(
            pos + " rate"
        )
        zzz = self.root.get_screen("info").ids["lunches"].text
        hours_text = "Rounded Hours"
        self.root.get_screen("animate").ids["moneya"].secondary_text = "Actual Hours"
        self.root.get_screen("animate").ids["moneyb"].secondary_text = "Earned"
        self.root.get_screen("animate").ids[
            "money_pay"
        ].secondary_text = "Earned (Actual)"
        try:
            if int(zzz) == 1:
                hours_text = hours_text + " (-1 Hour Lunch)"
            if int(zzz) == 2:
                hours_text = hours_text + " (-2 Hour Lunches)"
        except:
            pass

        self.root.get_screen("animate").ids["money_r"].secondary_text = hours_text

        # print(dir(self.root.get_screen("info").ids["lunches"]))
        # print(zzz, "zzz")

        Clock.schedule_interval(self.update_label, 0.1)

    def update_label(self, dt):
        from datetime import datetime

        start_time = mjds[idex]["date"] + "." + mjds[idex]["time"]
        start_time = datetime.strptime(start_time, "%m/%d/%Y.%H:%M")
        pos = mjds[idex]["pos"]
        rate = lib_extractjson.extract_pos(App, config_file, pos)
        now = datetime.now()
        difff = now - start_time
        difff = int(difff.total_seconds())
        diffs = difff / 3600
        earn = difff * float(rate)
        earn = earn / 3600
        earn = round(earn, 2)

        hours = int(diffs)
        minutes = (diffs * 60) % 60
        seconds = (diffs * 3600) % 60

        newh = "%d:%02d.%02d" % (hours, minutes, seconds)
        rhours = hours
        if minutes < 5:
            rminutes = 0
        if minutes >= 5 and minutes < 35:
            rminutes = 30
        if minutes >= 35:
            rminutes = 0
            rhours = rhours + 1
        zzz = self.root.get_screen("info").ids["lunches"].text
        ot_after = float(self.root.get_screen("info").ids["ot_spin"].text)
        try:
            if int(zzz) > 0:
                rhours = rhours - int(zzz)
        except:
            pass
        r_hours = "%d:%02d" % (rhours, rminutes)

        dec_hours = rhours
        if rminutes == 30:
            dec_hours = dec_hours + 0.5
        r_pay = dec_hours * float(rate)
        if dec_hours > ot_after:
            r_pay = ot_after * float(rate)
            ot_hours = dec_hours - ot_after
            r_pay = r_pay + (ot_hours * float(rate) * 1.5)

        # r_pay = dec_hours * float(rate)

        # new_text = datetime.datetime.now().strftime("%H:%M:%S")

        # label.text = new_text
        # print(new_text)
        self.root.get_screen("animate").ids["top"].text = str(start_time)
        self.root.get_screen("animate").ids["moneyinfo"].text = str(
            "%.2f" % float(rate)
        )
        self.root.get_screen("animate").ids["moneya"].text = str(newh)
        self.root.get_screen("animate").ids["moneyb"].text = str(earn)
        self.root.get_screen("animate").ids["money_r"].text = str(r_hours)
        self.root.get_screen("animate").ids["money_pay"].text = str("%.2f" % r_pay)

    def confirm(self, what):
        fail = self.confirm_real(what)
        old = False
        if fail != "fail":
            nf2 = ad + "/realdata.html"
            try:
                with open(nf2, mode="r") as f:
                    for line in f.readlines():
                        # print (line)

                        if "javascript'>alert" in line:
                            old = True
                            l, x = str.split(line, "(")
                            x, l = str.split(x, ")")
                            # print(x)
            except:
                self.snackbar = Snackbar(
                    text="Not Logged In", bg_color=self.theme_cls.primary_color
                )
                self.snackbar.open()
                # if not self.snackbar:
        if old == True:
            self.snackbar = Snackbar(text=x, bg_color=self.theme_cls.primary_color)
            self.snackbar.open()
        if fail == "fail":
            self.snackbar = Snackbar(
                text="Already confirmed you dum dum",
                bg_color=self.theme_cls.primary_color,
            )
            self.snackbar.open()
        if old == False and fail != "fail":
            self.snackbar = Snackbar(
                text="Success!", bg_color=self.theme_cls.primary_color
            )
            self.snackbar.open()

    def confirm_real(self, what):
        global browser
        # print (what)
        # print(len(xxx[idex]))
        try:
            # print(xxx[idex][13])
            pass
        except:
            print("nonconfirm")
            return "fail"

        print(type(browser))
        try:
            if 1 == 1:
                try:
                    browser.select_form(name="ctl00")
                    print("USED OLD BROWSER")
                except:
                    browser = lib_think.openbrowser(ad, x, ios, App)
                    browser.select_form(name="ctl00")
                    print("USED NEW BROWSER")

                # print(browser, 'browser 1')
                control_t = browser.form.find_control("__EVENTTARGET")
                control_a = browser.form.find_control("__EVENTARGUMENT")
                # print(browser, 'browser 2')
                control_t.readonly = False
                control_a.readonly = False

                control_t.value = str(xxx[idex][13])
                control_a.value = "Confirm"
                # print(browser, 'browser 3')

                response = browser.submit()
                # print(browser, 'browser 4')
                aa = response.get_data()
                # print(browser, 'browser 5')

                aaa = open(ad + "/realdata.html", "wb")
                aaa.write((aa))
                aaa.close()
        except:
            """"""

    def closeDialog(self, inst):
        self.dialog.dismiss()

    def delete_shows(self, what):
        # print (what)
        from os import walk

        filenames = next(walk(ad + "/shows"), (None, None, []))[2]  # [] if no file
        # print(filenames)
        for i in range(len(filenames)):
            os.remove(ad + "/shows/" + filenames[i])

    def show_delete_dialog(self):
        from kivymd.uix.dialog import MDDialog

        if not self.dialog:
            self.dialog = MDDialog(
                text="Discard draft?",
                buttons=[
                    MDFlatButton(
                        text="CANCEL",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_press=self.closeDialog,
                    ),
                    MDFlatButton(
                        text="DELETE",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_press=self.delete_shows,
                    ),
                ],
            )
        self.dialog.open()

    def backup(self):
        import os
        import shutil

        nf = os.path.join(ad, "shows2.zip")
        # nf='C:/Users/kw/AppData/Roaming/demo3/shows2.zip'
        try:
            shutil.make_archive(ad + "/show2", "zip", ad + "/shows")

            nfc = ad
            nf2 = os.path.join(nfc, "show2.zip")
            with open(nf2, mode="rb") as f:
                f = f.read()
                print(type(f), "typef")
                f = str(f)
            # print (f)
            return f

        except:
            self.snackbar = Snackbar(
                text="Make some show files first", bg_color=self.theme_cls.primary_color
            )
            self.snackbar.open()
            return ""

    def restorebin(self, x):
        import shutil
        import os

        try:
            # print(x)
            nf2 = os.path.join(ad, "show3.zip")
            # j,x,j=str.split(x,'"')
            # print (x)
            # x=x.encode()
            # print (bytes(x,'utf-8'))
            x = eval(x)

            with open(nf2, mode="wb") as f:
                f.write(x)
            shutil.unpack_archive(nf2, ad + "/shows")
        except:
            self.snackbar = Snackbar(
                text="Not Valid Backup Data", bg_color=self.theme_cls.primary_color
            )
            self.snackbar.open()

    def search_menu(self):
        # scale=2
        show = P()  # Create a new instance of the P class

        popupWindow = Popup(
            title="asdf",
            content=show,
            size_hint=(None, None),
            size=(400 * scale, 600 * scale),
            separator_height=0,
            title_size=0,
            background_color=(self.theme_cls.primary_dark),
        )
        # Create the popup window

        popupWindow.open()  # show the popup

    def search(self, x):
        # term=App.get_running_app().root.current_screen.ids['search'].text
        # print(x.text)
        self.do_login(x.text, useold)
        # root.dismiss()

    def set_caption(self, popup):
        self.button.text = popup.content.text

    def get_rate(self):
        try:
            # print(xxx[idex], "get_rate")
            pos = xxx[idex][8]
            rate = extract_pos(App, config_file, pos)
            App.get_running_app().root.current_screen.ids["rate"].text = str(rate)
        except:

            # print(xxx, "get_rate2error3")
            pass

    def set_rate(self):
        x = xxx[idex][8]
        # rate=str(28.5)
        rate = App.get_running_app().root.current_screen.ids["rate"].text
        import libs.lib_makeuserdata as lib_makeuserdata

        lib_makeuserdata.makeposfile(App, x, config_file, ios, rate)

    def get_date(self, date):
        """
        :type date: <class 'datetime.date'>
        """
        # return date
        pass

    def set_pp(self, current):
        App.get_running_app().root.current_screen.ids[
            "scustom"
        ].md_bg_color = self.theme_cls.primary_light
        if current == "current":
            App.get_running_app().root.current_screen.ids[
                "scustom"
            ].md_bg_color = self.theme_cls.primary_light
            App.get_running_app().root.current_screen.ids[
                "scurrent"
            ].md_bg_color = self.theme_cls.primary_dark
            App.get_running_app().root.current_screen.ids[
                "slast"
            ].md_bg_color = self.theme_cls.primary_light
            App.get_running_app().root.current_screen.ids[
                "sall"
            ].md_bg_color = self.theme_cls.primary_light

        if current == "last":
            App.get_running_app().root.current_screen.ids[
                "scustom"
            ].md_bg_color = self.theme_cls.primary_light
            App.get_running_app().root.current_screen.ids[
                "scurrent"
            ].md_bg_color = self.theme_cls.primary_light
            App.get_running_app().root.current_screen.ids[
                "slast"
            ].md_bg_color = self.theme_cls.primary_dark
            App.get_running_app().root.current_screen.ids[
                "sall"
            ].md_bg_color = self.theme_cls.primary_light
        if current == "custom":
            App.get_running_app().root.current_screen.ids[
                "scustom"
            ].md_bg_color = self.theme_cls.primary_dark
            App.get_running_app().root.current_screen.ids[
                "scurrent"
            ].md_bg_color = self.theme_cls.primary_light
            App.get_running_app().root.current_screen.ids[
                "slast"
            ].md_bg_color = self.theme_cls.primary_light
            App.get_running_app().root.current_screen.ids[
                "sall"
            ].md_bg_color = self.theme_cls.primary_light
        if current == "all":
            App.get_running_app().root.current_screen.ids[
                "scustom"
            ].md_bg_color = self.theme_cls.primary_light
            App.get_running_app().root.current_screen.ids[
                "scurrent"
            ].md_bg_color = self.theme_cls.primary_light
            App.get_running_app().root.current_screen.ids[
                "slast"
            ].md_bg_color = self.theme_cls.primary_light
            App.get_running_app().root.current_screen.ids[
                "sall"
            ].md_bg_color = self.theme_cls.primary_dark
            App.get_running_app().root.current_screen.ids["dend"].text = str("All")
            App.get_running_app().root.current_screen.ids["dstart"].text = str("All")
        flag = False
        firstdate = datetime.date(2021, 10, 13)
        #:
        now = datetime.datetime.now()
        now = datetime.date.today()
        while flag == False:

            nextdate = firstdate + datetime.timedelta(days=14)
            lastdate = nextdate + datetime.timedelta(days=13)
            if nextdate <= now <= lastdate:
                flag = True
                if current == "current":
                    App.get_running_app().root.current_screen.ids["dstart"].text = str(
                        nextdate
                    )
                    App.get_running_app().root.current_screen.ids["dend"].text = str(
                        lastdate
                    )
                if current == "last":
                    App.get_running_app().root.current_screen.ids["dstart"].text = str(
                        nextdate - datetime.timedelta(days=14)
                    )
                    App.get_running_app().root.current_screen.ids["dend"].text = str(
                        lastdate - datetime.timedelta(days=14)
                    )
            firstdate = nextdate
        if current != "custom":
            self.do_history()

    def show_date_picker(self):
        date_dialog = MDDatePicker(mode="range")
        date_dialog.bind(on_save=self.on_save, on_cancel=self.on_cancel)
        date_dialog.open()
        # App.get_running_app().root.current_screen.ids['send'].md_bg_color= self.theme_cls.primary_light
        # App.get_running_app().root.current_screen.ids['sstart'].md_bg_color= self.theme_cls.primary_light
        # App.get_running_app().root.current_screen.ids['scustom'].md_bg_color= self.theme_cls.primary_dark

    def on_cancel(self, instance, value):
        # self.root.ids.date_label.text = "You Clicked Cancel"
        pass

    def on_save(self, instance, value, date_range):
        # self.root.ids.date_label.text = str(value)
        # self.root.ids.date_label.text = f'{str(date_range[0])} - {str(date_range[-1])}'
        try:
            App.get_running_app().root.current_screen.ids["dstart"].text = str(
                date_range[0]
            )
            App.get_running_app().root.current_screen.ids["dend"].text = str(
                date_range[-1]
            )
        except:
            App.get_running_app().root.current_screen.ids["dstart"].text = str("")
            App.get_running_app().root.current_screen.ids["dend"].text = str("")
        self.do_history()

    def updatetext(self, box):
        app = App.get_running_app()
        ad = app.user_data_dir
        # print(ad)
        if ios == False:
            config_file = ad
        debugbox = App.get_running_app().root.current_screen.ids[box].active
        x[box] = debugbox
        # print(x[box], "xbox")
        import libs.lib_updateuserdata as lib_updateuserdata

        lib_updateuserdata.updateuser(x, ad)

    def maps(
        self,
    ):
        bbb = App.get_running_app().root.current_screen.ids["venue"].text
        webbrowser.open("https://www.google.com/maps/search/" + bbb)

    def save(show):
        pass

    def format_textt(self, name):
        name = str.replace(name, "/", "")
        name = str.replace(name, ":", "")
        return name

    def show_time_picker2(self):
        import libs.lib_makeuserdata

        libs.lib_makeuserdata.makeshowfile(App, xxx[idex], config_file, ios)

    def show_time_picker1(self):
        # if App.get_running_app().root.current_screen.ids['newhours'].text=='Set Worked Hours':
        if 1 == 1:
            y = time_dialog1 = MDTimePicker()
            x = time_dialog1.bind(time=self.get_time)
            z = time_dialog1.open()

    def get_time(self, instance, time):

        App.get_running_app().root.current_screen.ids["newhours"].text = str(time)
        return time

    def make_info(self, thing):

        return thing

    def on_checkbox_active(self, checkbox, value):
        global x
        if value:
            print("The checkbox", checkbox, "is active", "and", checkbox.state, "state")
            x["usecache"] = "True"
        else:
            print(
                "The checkbox", checkbox, "is inactive", "and", checkbox.state, "state"
            )
            x["usecache"] = "False"
        btnState2 = StringProperty("false")
        lib_updateuserdata.updateuser(x, ad)

    """
    def on_start(self):
        global x
        global ad
        app = App.get_running_app()
        ad = app.user_data_dir
        if ios == True:
            config_file = ad

        try:
            x = lib_readuserdata.readuserdata(App, config_file, ios)
        except:
            print("failed to read user data, making shit up now")
            lib_makeuserdata.makeuserdata(App, config_file, ios)
            x = lib_readuserdata.readuserdata(App, config_file, ios)
            print(x, "readuserdata after creating it", type(x), x["username"])
        self.do_login("", useold)
        # self.search_menu = SearchPopupMenu()
        # self.root.ids.usecache.state='down'
    """

    def lol(self):
        # x=lib_readuserdata.readuserdata(App,config_file)
        # xx=(x['usecache'])
        # if xx=="True":
        #    xx='Using Cache'
        # if xx=="False":
        #    xx='Using Real Data'

        # return str(xx)
        pass

    def removeAll(self):
        self.root.current_screen.ids["users_lst"].clear_widgets()

    def show_theme_picker(self):
        theme_dialog = MDThemePicker()
        theme_dialog.open()

    def save_theme_picker(self):
        s = self.theme_cls.theme_style
        p = self.theme_cls.primary_palette
        a = self.theme_cls.accent_palette
        x = lib_readuserdata.readuserdata(App, config_file, ios)
        # print(s, p, a, x)
        x["pcolor"] = p
        x["scolor"] = a
        x["theme"] = s
        # print(s, p, a, x)
        lib_updateuserdata.updateuser(x, ad)

    def change_screen(self, screen, direction):
        self.root.transition.direction = direction
        # self.root.current = screen
        self.root.set_current(screen)

    """
    def build(self):

        self.button = Button(text="Click", on_release=self.search_menu)

        global newcolor
        try:
            x = lib_readuserdata.readuserdata(App, config_file, ios)
        except:
            lib_makeuserdata.makeuserdata(App, config_file, ios)
            x = lib_readuserdata.readuserdata(App, config_file, ios)
        try:
            self.theme_cls.theme_style = x["theme"]
            self.theme_cls.primary_palette = x["pcolor"]
            self.theme_cls.accent_palette = x["scolor"]
        except:
            pass

        self.sm = ScreenManager()
        self.sm.add_widget(MainMenuScreen(name="mainmenu"))
        if 1 == 2:
            self.sm.add_widget(InfoScreen(name="info"))
            self.sm.add_widget(SettingsScreen(name="settings"))
            self.sm.add_widget(HomeScreen(name="home"))
            self.sm.add_widget(LoginScreen(name="login"))
            self.sm.add_widget(HistoryScreen(name="history"))
            self.sm.add_widget(PayScreen(name="Pay"))
            self.sm.add_widget(AboutScreen(name="about"))
            self.sm.add_widget(TrophyScreen(name="trophy"))
            self.sm.add_widget(StatsScreen(name="stats"))
            self.sm.add_widget(NotificationScreen(name="notification"))
            self.sm.add_widget(AnimateMoneyScreen(name="animate"))

        # newcolor=webcolors.name_to_rgb(self.theme_cls.accent_palette)

        screen = Builder.load_file("demo.kv")
        # site = server.Site(Simple())

        # reactor.listenTCP(8080, site)

        return screen
    """

    def load_paychecks(self):
        import glob, os

        try:
            os.chdir(config_file + "/pp")
        except:
            os.mkdir(config_file + "/pp")
            os.chdir(config_file + "/pp")
        x = 0
        listofdicks = []
        for file in glob.glob("*.html"):
            # print (file)
            import libs.lib_parse as lib_parse

            dd, junk = lib_parse.parsepayperiod(config_file + "/pp/" + file)
            listofdicks.append(dd)
            x = x + 1
        return listofdicks

    def do_payperiod(self, ssort, rreverse):
        self.root.set_current("pay")
        self.root.current_screen.ids["payperiod_list"].clear_widgets()
        listofdicks = self.load_paychecks()
        # self.root.current_screen.ids["payperiod_list"].add_widget(HistoryItem(text='bla1'))

        # self.root.current_screen.ids["payperiod_list"].add_widget(HistoryItem(text=str(dd)+'[size='+str(x)))
        # if x<5:
        #    self.root.current_screen.ids["payperiod_list"].add_widget(HistoryItem(text=str(dd['dtext'])+'[size=0]'+str(x)))
        # listofdicks.sort()
        # listofdicks= (sorted(listofdicks, key = lambda i: i['paydate'],reverse=True))
        # listofdicks= (sorted(listofdicks, key = lambda i: i['shows'],reverse=True))
        # listofdicks= (sorted(listofdicks, key = lambda i: i['moneytotal'],reverse=rrverse))
        listofdicks = sorted(listofdicks, key=lambda i: i[ssort], reverse=rreverse)
        moneys = 0
        hourst = 0
        hoursot = 0
        hourstot = 0
        # hourstot=0
        # print(listofdicks)
        for i in range(len(listofdicks)):

            print(listofdicks[i])
            self.root.current_screen.ids["payperiod_list"].add_widget(
                HistoryItem(text=str(listofdicks[i]["dtext"]) + "[size=0]" + str(i))
            )
            moneys = moneys + float(listofdicks[i]["moneytotal"])
            try:
                hourst = hourst + float(listofdicks[i]["reghours"])
            except:
                pass
            try:
                hoursot = hoursot + float(listofdicks[i]["othours"])
            except:
                pass
            try:
                hourstot = hourstot + float(listofdicks[i]["totalhours"])
            except:
                pass

        xy = "Found " + str(i) + " PayStubs "
        xyz1 = "Average Paycheck $ " + str(moneys / len(listofdicks))
        xyz2 = "\nAverage Reg Hours: " + str(hourst / len(listofdicks))
        xyz3 = "\nAverage Ot Hours: " + str(hoursot / len(listofdicks))
        xyz4 = "\nAverage Total Hours: " + str((hourstot) / len(listofdicks))
        xyzz = xyz1 + xyz2 + xyz3 + xyz4

        try:
            self.root.current_screen.ids["payperiod_list"].add_widget(
                HistoryItem(text=xy + "[size=0]" + str(i + 1))
            )

            self.root.current_screen.ids["payperiod_list"].add_widget(
                HistoryItem(text=xyzz + "[size=0]" + str(i + 2))
            )

        except:
            self.root.current_screen.ids["payperiod_list"].add_widget(
                HistoryItem(text="No Pay Stubs found!" + "[size=0]" + str(1))
            )
        # print(moneys, "moneys")

    def do_history(self):

        self.root.set_current("history")
        self.root.current_screen.ids["history_list"].clear_widgets()
        # self.root.current_screen.ids["history_list"].add_widget(HistoryItem(text='bla'))
        import glob, os

        try:
            os.chdir(config_file + "/shows")
        except:
            os.mkdir(config_file + "/shows")
            os.chdir(config_file + "/shows")
        x = 0

        for file in glob.glob("*.json"):
            x = x + 1
        x = "Found " + str(x) + " Shows "
        # self.root.current_screen.ids["history_list"].add_widget(HistoryItem(text=str(x))+'0')
        allshows = []
        # allshows.sort()
        hours = 0
        ot = 0
        pay = 0
        tot = 0

        now = datetime.datetime.now()
        for file in glob.glob("*.json"):
            if 1 == 1:
                import libs.lib_extractjson

                data, pay2, ot2, hours2, tot2, date = libs.lib_extractjson.extract_show(
                    App, file, config_file
                )
                print(data, pay2, ot2, hours2, tot2, date, "HOLY CRAP")
                show_date = datetime.datetime.strptime(date, "%m/%d/%Y")
                dstart = App.get_running_app().root.current_screen.ids["dstart"].text
                dend = App.get_running_app().root.current_screen.ids["dend"].text
                # print(show_date.date(), dstart, dend)
                # print(type(show_date.date()), type(dstart), type(dend))
                force = False
                if dstart == "All":

                    dstart = datetime.datetime.strptime("1900", "%Y")
                    dend = datetime.datetime.strptime("2200", "%Y")
                    force = True
                else:
                    # dstart != 'All':
                    # print(dstart, dend, "WF")
                    dstart = datetime.datetime.strptime(dstart, "%Y-%m-%d")
                    dend = datetime.datetime.strptime(dend, "%Y-%m-%d")
                    # print(
                    #    type(show_date.date()), type(dstart.date()), type(dend.date())
                    # )
                # print(data, dstart.date(), dend.date(), show_date.date(), "data66")
                if dstart.date() <= show_date.date() <= dend.date():
                    print(data, "inside the loop")

                    allshows.append(data)
                    pay = pay + pay2
                    ot = ot + ot2
                    hours = hours + hours2
                    tot = tot + tot2

            # except:
            # print("failed to add show")
        self.root.current_screen.ids["history_list"].add_widget(
            HistoryItem(
                text="pay="
                + str(pay)
                + "\nhours="
                + str(hours)
                + "\not="
                + str(ot)
                + "\nTotal Hours="
                + str(tot)
                + "\nTotal Shows="
                + str(len(allshows))
                + "[size=1 sp]***1"
            )
        )
        s = allshows
        s = allshows.sort(reverse=True)
        print(allshows, "allshows")

        for i in range(len(allshows)):
            t = allshows[i] + "[size=1 sp]***" + str(i)
            self.root.current_screen.ids["history_list"].add_widget(HistoryItem(text=t))

    def check_pull_refresh(self, view, grid):
        pass
        """
        max_pixel = 200
        # aa=self.root.get_screen("home").ids['sv']
        # print
        try:
            totwidget = (plus_search) + 2
            action = totwidget
            stupid = view.scroll_y
            max = (view.scroll_y) / totwidget
            max2 = totwidget / view.scroll_y
            max3 = totwidget * view.scroll_y
            junk = 1 * (stupid - 1)
            junk = junk * grid.height
            #print(junk, h / 3, plus_search)
            if (junk) > (h / 3):
                print("overscroll")
                # self.do_login("",useold)
        except:
            print("fail")
            """

        # for id in self.root.get_screen("home").ids:
        # for id in self.root.get_screen("home").ids:

        # print (id)
        # print (view.height,aa.height,aa.pos,aa.size,aa.scroll_distance,dir(aa))

        # to_relative = max_pixel / ( view.height)
        # if view.scroll_y < 1.0 + to_relative or self.refreshing:
        # return

        # self.refresh_data()

    def grabText(self, inst):
        from kivy.core.clipboard import Clipboard

        Clipboard.copy(inst)

        # print("grabtext", inst)

        self.snackbar = Snackbar(
            text="Copied",
            bg_color=self.theme_cls.primary_color,
        )
        self.snackbar.open()

    task_list_dialog = None

    def add_task(self, init):
        # for x in range(len(self.dialog.clear_widgets)):
        #    print(self.dialog.items[x])
        # print(dir(self.dialog))
        self.dialog.text = "loser"
        pass

    def poppy(self, v):
        from kivymd.uix.button import MDFlatButton

        from kivymd.uix.dialog import MDDialog

        # print("lol")
        ttt = mjds[idex][v]
        if len(ttt) < 2:
            self.snackbar = Snackbar(
                text="[empty]",
                bg_color=self.theme_cls.primary_color,
            )
            self.snackbar.open()

        if not self.dialog:
            self.dialog = MDDialog(
                text=ttt,
                type="custom",
                # content_cls=Content(),
                buttons=[
                    MDFlatButton(
                        text="Copy",
                        text_color=self.theme_cls.primary_color,
                        on_release=(lambda a: self.grabText(ttt)),
                    ),
                ],
            )
        if len(ttt) > 2:
            self.dialog.open()

            self.dialog.text = ttt

    def refresh_data(self):
        print("lol")

    # def check_login(self):
    # good_login=self.do_login('',False)
    # if good_login==True:
    # self.save_login()
    # self.root.current = "home"

    def save_login(self):
        self.root.current = "login"
        x["username"] = App.get_running_app().root.current_screen.ids["temail"].text
        x["password"] = App.get_running_app().root.current_screen.ids["tpassword"].text
        x["city"] = App.get_running_app().root.current_screen.ids["button4"].text
        lib_updateuserdata.updateuser(x, ad)

    # btnState2 = StringProperty("false")


Demo3App().run()
