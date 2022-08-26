###cp \schedulara\.buildozer\android\platform\build-arm64-v8a_armeabi-v7a\dists\kw.schedulara\build\outputs\apk\debug\kw.schedulara-0.1-arm64-v8a_armeabi-v7a-debug.apk /mnt/c/Users/kw/Desktop/app.apk


from ast import Pass
from asyncio import queues
from audioop import reverse
import profile
import time
import sys

#
#


tic = time.perf_counter()
from libs.uix.root import Root

ios = True
notch = True
debug = True
scale = 2
useold = False
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.properties import StringProperty, Property
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.list import IRightBodyTouch, ILeftBodyTouch
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.app import App
from kivy.config import Config

from kivy.utils import platform
from kivymd.uix.snackbar import Snackbar
from kivymd.toast import toast
from kivymd.uix.pickers import MDColorPicker

# from kivymd.uix.pickers import MDThemePicker
# from kivymd.uix.picker import MDTimePicker


# from kivymd.uix.picker import MDDatePicker
# from kivymd.uix.pickers import MDTimePicker

# print("cant do mddatepicker")
from kivy.uix.popup import Popup
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.list import (
    OneLineAvatarIconListItem,
    TwoLineAvatarListItem,
    TwoLineListItem,
    ThreeLineListItem,
    ThreeLineAvatarListItem,
)

from kivymd.uix.expansionpanel import (
    MDExpansionPanel,
    MDExpansionPanelTwoLine,
    MDExpansionPanelThreeLine,
)


from kivy.uix.label import Label
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.button import MDFlatButton
from kivy.metrics import dp


import datetime
import libs.lib_think as lib_think
import libs.lib_google2 as lib_google

try:
    import libs.lib_google2 as lib_google
except:
    print("fail google")
import libs.lib_readuserdata as lib_readuserdata


"""
from audioop import ratecv
from kivy.lang import Builder

from kivymd.uix.list import (
    MDList,
    ThreeLineIconListItem,
    TwoLineIconListItem,
    IconLeftWidget,
)

from kivymd.uix.textfield import MDTextField


# from kivy.effects.dampedscroll import DampedScrollEffect

print(platform, "KIVY PLATFORM")
if platform == "linux":
    print("omgitslinux")



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
import os
cwd=os.getcwd()
from pyparsing import ParseExpression
import webcolors

w = 1125 / 3
h = 2436 / 3
if platform == "win":

    Config.set("graphics", "width", str(w))
    Config.set("graphics", "height", str(h))
    Window.size = (w, h)
    scale = 1
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
from kivy.utils import platform

# import storagepath

# storagepath.get_downloads_dir()

if platform == "ios":

    app = App.get_running_app()
    import ios
    from pyobjus import autoclass

    NSURL = autoclass("NSURL")
    UIApplication = autoclass("UIApplication")
    sharedApplication = UIApplication.sharedApplication()

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


class HomeScreen(Screen):
    pass


class SmoothLabel(Label):
    pass


class HistoryScreen(Screen):
    pass


class PayScreen(Screen):
    pass


class YourContainer(IRightBodyTouch, MDBoxLayout):
    adaptive_width = True


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


class SwipeToDeleteItem2(Screen):
    text = StringProperty()


from kivy.uix.recycleview import RecycleView
from kivy.properties import StringProperty, ListProperty


class RV(RecycleView):
    rv_data_list = (
        ListProperty()
    )  # A list property is used to hold the data for the recycleview, see the kv code

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.rv_data_list = [
            {"left_text": f"Left {i}", "right_text": f"Right {i}"} for i in range(2)
        ]
        # This list comprehension is used to create the data list for this simple example.
        # The data created looks like:
        # [{'left_text': 'Left 0', 'right_text': 'Right 0'}, {'left_text': 'Left 1', 'right_text': 'Right 1'},
        # {'left_text': 'Left 2', 'right_text': 'Right 2'}, {'left_text': 'Left 3'},...
        # notice the keys in the dictionary correspond to the kivy properties in the TwoButtons class.
        # The data needs to be in this kind of list of dictionary formats.  The RecycleView instances the
        # widgets, and populates them with data from this list.

    def add(self):
        l = len(self.rv_data_list)
        self.rv_data_list.extend(
            [
                {"left_text": f"Added Left {i}", "right_text": f"Added Right {i}"}
                for i in range(l, l + 1)
            ]
        )


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
            import libs.lib_extractjson as lib_extractjson

            rate = lib_extractjson.extract_pos(App, config_file, xxx[idex][8])
            App.get_running_app().root.current_screen.ids["rate"].text = rate
        except:
            App.get_running_app().root.current_screen.ids["rate"].text = "?"
        from datetime import datetime

        now = datetime.now()
        try:
            import libs.lib_tinyfs as lib_tinyfs

            today, fdate = lib_tinyfs.format_text(idex, mjds, now, "info")
            # print("OMGWHATHAVEYOPUDONE ", idex)
        except:
            # print("omgwhathaveyoudone ", idex)
            pass
        if 1 == 1:
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
            # App.get_running_app().root.current_screen.ids["d10"].text = str(newxxx[13])
            if newxxx[8] == "ME":
                App.get_running_app().root.current_screen.ids[
                    "pos"
                ].icon = "power-socket-us"
            App.get_running_app().root.current_screen.ids["image"].source = (
                "images/" + x["city"] + ".png"
            )
        # except:
        #    (newxxx)

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


from kivymd.uix.dialog import MDDialog


class IngredientDialog(MDDialog):
    pass


class TwoLineAvatarListItem22(TwoLineAvatarListItem):
    icon = StringProperty("")
    # icon2 = StringProperty("android")
    # icon_color = Property([0, 0, 1, 0])
    # text_color = Property("")


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
today_index = 0
s_index = 0


class RecipeLine(MDBoxLayout):
    text = StringProperty()


class Content(MDBoxLayout):
    pass


class Content2(MDBoxLayout):
    pass


from plyer import filechooser

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
    fday = ""
    lday = ""
    date_range_pp = "All"
    sort_pp = "paydate"
    scale = 1
    reverse = True

    i = 0
    # print("omg")
    print(tic - time.perf_counter(), "supershort")
    cspacing = 10
    mtype = "top"
    bradius = 10 * scale
    radius = 10 * scale
    cpadding = 20
    sound_effects = ["Ding", "Bang", "Lol"]
    mheight = dp(170)
    pictures = [
        "light",
        "hammer",
        "speaker",
        "bossman",
        "default",
    ]
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

    pcolor = [
        "Red",
        "Pink",
        "Purple",
        # "DeepPurple",
        "Indigo",
        "Blue",
        "LightBlue",
        "Cyan",
        "Teal",
        "Green",
        "LightGreen",
        "Lime",
        "Yellow",
        # "Amber",
        "Orange",
        # "DeepOrange",
        "Brown",
        "Gray",
        "BlueGray",
    ]
    wall = ["Rhino", "Dark", "Light", "Stage", "Sing", "schedulara"]
    profile = 0
    profile_data = []
    data = {
        "History": "calendar-star",
        "Paystubs": "cash-100",
        "Stats": "chart-areaspline",
        "Trophys": "trophy-award",
        # "Old_Schedule": "book-clock",
        "About": "information",
        "firedb": "database",
        # "Profile": "account-circle",
        # "Chat": "message-outline",
        "Google Cal Backup": "google-downasaur",
        "Settings": "cog-outline",
        "Backup": "test-tube",
        "animate": "test-tube-empty",
    }
    c_radius = dp(3)

    def get_dates(self, t):
        from datetime import datetime
        from dateutil.relativedelta import relativedelta

        now = datetime.now()
        # print(now, type(now))
        if t == "All":
            date_string = "1 January, 2000"
            d = datetime.strptime(date_string, "%d %B, %Y")

            date_string = "1 January, 2099"
            now = datetime.strptime(date_string, "%d %B, %Y")
        if t == "Year":
            d = datetime.now() - relativedelta(years=1)
        if t == "YTD":
            d = datetime.now().date().replace(month=1, day=1)
            d = datetime.combine(d, datetime.min.time())
            now = datetime.now().date().replace(month=12, day=31)
            now = datetime.combine(now, datetime.min.time())

        print(d, type(d))

        return d, now

    def call(self, lol):
        print("call", (lol), lol.icon)
        self.root.current_screen.ids.menub.close_stack()
        if lol.icon == "cog-outline":
            self.do_settings()
        if lol.icon == "database":
            self.do_db()
        if lol.icon == "account-circle":
            self.do_profile()

        if lol.icon == "message-outline":
            self.do_chat(0)

        if lol.icon == "chart-areaspline":
            fdate, ldate = self.get_dates("YTD")
            self.do_new_stats(fdate, ldate, "YTD")
        if lol.icon == "cash-100":
            # self.do_payperiod("paydate", self.rreverse)
            self.do_payperiod_f("YTD")
        if lol.icon == "google-downasaur":
            self.do_google_cal()
        if lol.icon == "test-tube":
            self.do_gbackup()
        if lol.icon == "information":
            self.poppy("about")

        if lol.icon == "test-tube-empty":
            self.test_animate()

    def test_animate(self):
        print("test animate")

    def do_restore(self, f):
        import shutil

        global x

        print(f)
        f2 = lib_google.search_files(ad, f)
        print(f2)
        f3 = lib_google.download_google_drive(ad, f2)
        fw = open(ad + "/temp.zip", "wb")
        fw.write(f3)
        fw.close()
        shutil.unpack_archive(ad + "/temp.zip", ad)
        x = lib_readuserdata.readuserdata(App, ad, ios)

    def do_gbackup(self):
        self.root.set_current("backupgoogle")

        import libs.lib_new
        import datetime

        import humanize

        x = libs.lib_readuserdata.readuserdata(App, ad, ios)

        print("test00")
        if x.get("drive_id") == None:
            x["drive_id"] = lib_google.search_files(ad, "Schedulara_Backups")

            print(x["drive_id"])
            import libs.lib_updateuserdata

            libs.lib_updateuserdata.updateuser(x, ad)
        print(x["drive_id"], "this is do_gbackup")
        l_backup = App.get_running_app().root.current_screen.ids["last_backup"]
        # l_backup.text=
        if x.get("last_backup") == None:
            l_backup.secondary_text = "Last Backup: Never"
        else:
            old_update = datetime.datetime.strptime(
                x["last_backup"], "%Y-%m-%d %H:%M:%S.%f"
            )
            now = datetime.datetime.now()
            diff2 = humanize.naturaltime(now - old_update)
            print("why no update", diff2)
            l_backup.secondary_text = "Last Backup: " + diff2
        # print(x.get("last_backup"), "LAST BACKUP")

    def do_backups(self):
        toast("starting backup")
        import os
        import shutil
        import datetime

        global x

        bu = ["backup_checks", "backup_config", "backup_shows"]
        for i in range(len(bu)):
            if x[bu[i]]:

                if bu[i] == "backup_checks":
                    # print(bu[i])
                    src = os.path.join(ad, "pp")
                    dest = os.path.join(ad, "backup/pp")
                    try:
                        shutil.rmtree(dest)
                    except:
                        pass
                    destination = shutil.copytree(src, dest)
                if bu[i] == "backup_shows":
                    # print(bu[i])
                    src = os.path.join(ad, "future_shows")
                    dest = os.path.join(ad, "backup/future_shows")

                    try:
                        shutil.rmtree(dest)
                    except:
                        pass
                    destination = shutil.copytree(src, dest)
                if bu[i] == "backup_config":
                    # print(bu[i])
                    src = os.path.join(ad, "userdata.json.txt")
                    dest = os.path.join(ad, "backup/userdata.json")
                    destination = shutil.copy2(src, dest)

        zsrc = os.path.join(ad, "backup")
        zdest = os.path.join(ad, "backup")
        shutil.make_archive(zsrc, "zip", zdest)
        import libs.lib_google2

        self.do_test_open()
        tt = libs.lib_google2.google_files(ad, "backup.zip", x["drive_id"])
        toast(tt)
        # nf = os.path.join(ad, "shows2.zip")
        # nf='C:/Users/kw/AppData/Roaming/demo3/shows2.zip'
        # shutil.make_archive(ad + "/show3", "zip", ad + "/shows")
        now = datetime.datetime.now()
        # now = humanize.naturaltime(now)
        import libs.lib_updateuserdata

        x["last_backup"] = str(now)

        libs.lib_updateuserdata.updateuser(x, ad)
        # print(x)
        self.do_gbackup()

    def file_selection(self, selection):
        import os
        import logging as Logger

        tmp_images_path = ad
        if selection:
            path = str(selection[0])
            if not os.path.exists(tmp_images_path):
                os.makedirs(tmp_images_path)

            filename = os.path.basename(path)

            tmp_file = os.path.join(tmp_images_path, filename)
            # copyfile(path, tmp_file)

            Logger.debug(f"Image copied to tmp folder: {tmp_file}")
            Logger.debug(f"Image selected: {path}")

            print(f"Temp: {tmp_file}\nReal: {path}")
            print("on_image_selected", path)
        else:
            path = ""

    def find_gbackups(self):
        import libs.lib_readuserdata

        x = libs.lib_readuserdata.readuserdata(App, ad, ios)

        print("test00")
        if x.get("drive_id") == None:
            x["drive_id"] = lib_google.search_files(ad, "Schedulara_Backups")

            print(x["drive_id"], "drive.id find_gbackups")
            import libs.lib_updateuserdata

            libs.lib_updateuserdata.updateuser(x, ad)

        z = lib_google.find_backup(ad, [x["drive_id"]])
        # print(z, "this is the list of backups")
        return z

    def do_test_open(self):

        import libs.lib_new

        print("test00")
        if x.get("drive_id") == None:
            x["drive_id"] = lib_google.search_files(ad, "Schedulara_Backups")

            print(x["drive_id"])
            import libs.lib_updateuserdata

            libs.lib_updateuserdata.updateuser(x, ad)
        print(x)
        return x

    def snackbarx(self, text1):
        self.snackbar = Snackbar(
            text=text1,
            bg_color=self.theme_cls.primary_color,
        )
        self.snackbar.open()

    def add_google_calendar(self, y):
        import libs.lib_google2 as lib_google

        print(y)
        if x.get("cal_id") != None:
            lib_google.google_calendar_add(ad, y, x["cal_id"])
            # lib_google.get_calendar_service(ad)

    def remove_google_token(self, z):
        import os

        try:
            os.remove(ad + "/" + z)
            self.snackbarx("success")
        except:
            self.snackbarx("failed to remove")

    def do_google_cal(self):
        import libs.lib_readuserdata
        import json

        x = libs.lib_readuserdata.readuserdata(App, ad, ios)
        import libs.lib_google2 as lib_google
        import libs.lib_new

        # lib_google.create(ad)
        if x.get("cal_id") == None:
            print("has name")
            x["cal_id"] = lib_google.make_user_cals(ad)
            import libs.lib_updateuserdata

            libs.lib_updateuserdata.updateuser(x, ad)

        js = libs.lib_new.get_json_schedule_1(x, ad)
        gg = js["shows"]
        added = 0
        if x.get("cal_id") != None:
            for show in range(len(gg)):
                # print(gg[show])
                # self.snackbarx(gg[show]["show"])
                # print(gg[show], "goddamn")
                if gg[show].get("google_id") == None:
                    # lib_google.google_calendar_add(ad, gg[show], x["cal_id"])

                    try:
                        x2 = open(
                            ad + "/future_shows/" + self.filename(gg[show]) + ".json",
                            "r",
                        )
                        print("FOUND FILE")
                    except:
                        try:
                            os.mkdir(ad + "/future_shows")
                        except:
                            "ok"
                        zz = lib_google.google_calendar_add(ad, gg[show], x["cal_id"])
                        gg[show]["google_id"] = zz
                        x2 = open(
                            ad + "/future_shows/" + self.filename(gg[show]) + ".json",
                            "w",
                        )

                        json_object = json.dumps(gg[show], indent=4)
                        self.snackbarx("Added " + str(added))

                        x2.write(json_object)
                        +added
        self.snackbarx("Added " + str(added))

    def filename(self, x):
        f = str.replace(x["show"], "/", "")
        f = str.replace(f, ":", "")
        f1 = str.replace(x["date"], "/", "")
        f2 = str.replace(x["time"], ":", "")
        f3 = x["job"]
        return f1 + "_" + f2 + f3 + f

    def format_date(self, d, year):
        from datetime import datetime

        if year == "short":
            d = d.strftime("%m/%d")
        if year == "full":
            d = d.strftime("%m/%d/%Y")

        return str(d)

    def do_new_stats_format(self, f):

        fdate, ldate = self.get_dates(f)
        try:
            self.do_new_stats(fdate, ldate, f)
        except:
            print("div by 0")

    def check_stats(self, li):
        print(li, "LIST OF CHECKS")
        sum2 = sum(li)
        ave = sum2 / (len(li))
        return round(sum2, 2), round(ave, 2)

    future_pos = {
        "name": "Future Position",
        "file": "jason_show_cache_real.json",
        "filter": "pos",
        "id": "c6",
    }

    future_venue = {
        "name": "Future Venue",
        "file": "jason_show_cache_real.json",
        "filter": "venue",
        "id": "c7",
    }

    future_type = {
        "name": "Future Show Type",
        "file": "jason_show_cache_real.json",
        "filter": "type",
        "id": "c8",
    }
    venue_chart = {
        "name": "Venue",
        "file": "json_pps.json",
        "filter": "VENUE",
        "id": "c5",
    }
    client_chart = {
        "name": "Client",
        "file": "json_pps.json",
        "filter": "CLIENT",
        "id": "c4",
    }
    paycheck_amount_chart = {
        "name": "Paycheck Amount",
        "file": "json_pps.json",
        "filter": "PCDA",
        "id": "c3",
    }
    type_chart = {
        "name": "Type",
        "file": "json_pps.json",
        "filter": "TYPE",
        "id": "c2",
    }
    pos_chart = {
        "name": "Positions",
        "file": "json_pps.json",
        "filter": "POS",
        "id": "c1",
    }

    def do_new_stats(self, fdate, ldate, rng):
        import kivymd_extensions.akivymd

        print("omg")
        self.root.set_current("newstats")
        import libs.lib_makegraphs
        import libs.lib_parse2

        bu = ["YTD", "Year", "All", "Custom"]

        App.get_running_app().root.current_screen.ids["dstart"].text = (
            self.format_date(fdate, "full") + "     to"
        )

        App.get_running_app().root.current_screen.ids["dend"].text = self.format_date(
            ldate, "full"
        )
        for i in range(len(bu)):
            if rng == bu[i]:
                App.get_running_app().root.current_screen.ids[
                    bu[i]
                ].md_bg_color = self.theme_cls.primary_dark
            else:
                App.get_running_app().root.current_screen.ids[
                    bu[i]
                ].md_bg_color = self.theme_cls.primary_light

        # s = App.get_running_app().root.current_screen.ids["dstart"].text
        # e = App.get_running_app().root.current_screen.ids["dend"].text
        libs.lib_makegraphs.make_full_json_pp(ad, fdate, ldate)
        """"
        ##loads all shows from /pp ###POS
        pos_k2, pos_v2, pos_l = libs.lib_parse2.load_full_pp(ad, "json_pps.json", "POS")
        if len(pos_k2) < 1:
            pos_k2 = [0]
            pos_v2 = [0]

        chart1 = App.get_running_app().root.current_screen.ids["c1"]
        chart1.x_values = pos_v2
        chart1.y_values = pos_v2
        chart1.x_labels = pos_k2
        if 100 * len(pos_v2) > dp(400):
            App.get_running_app().root.current_screen.ids["c4"].width = dp(50) * len(
                pos_v2
            )
        else:
            App.get_running_app().root.current_screen.ids["c4"].width = dp(400)
        chart1.update()

        ##loads all shows from /pp   ###SHOW/in/Out
        pos_k2, pos_v2, pos_l = libs.lib_parse2.load_full_pp(
            ad, "json_pps.json", "TYPE"
        )
        if len(pos_k2) < 1:
            pos_k2 = [0]
            pos_v2 = [0]
        chart2 = App.get_running_app().root.current_screen.ids["c2"]
        chart2.x_values = pos_v2
        chart2.y_values = pos_v2
        chart2.x_labels = pos_k2
        App.get_running_app().root.current_screen.ids["c2d"].width = 1 * len(pos_v2)
        if 100 * len(pos_v2) > dp(400):
            App.get_running_app().root.current_screen.ids["c2"].width = dp(130) * len(
                pos_v2
            )
        else:
            App.get_running_app().root.current_screen.ids["c2"].width = dp(400)
        chart2.update()
        
        ##loads all shows from /pp   ###PAYCHECK DOLLAR AMOUNT
        pos_k2, pos_v2, pos_v3 = libs.lib_parse2.load_full_pp(
            ad, "json_pps.json", "PCDA"
        )
        if len(pos_k2) < 1:
            pos_k2 = [0]
            pos_v2 = [0]
            toast("No PP data Found")
        chart3 = App.get_running_app().root.current_screen.ids["c3"]
        chart3.x_values = pos_k2
        chart3.y_values = pos_k2
        chart3.x_labels = pos_v2
        check = App.get_running_app().root.current_screen.ids["c3d"]
        ave, tot = self.check_stats(pos_k2)
        check.secondary_text = "average: " + str(ave)
        check.tertiary_text = "total: " + str(tot)
        check.text = "Paychecks: " + str(len(pos_k2))
        if 100 * len(pos_v2) > dp(300):
            App.get_running_app().root.current_screen.ids["c3"].width = dp(50) * len(
                pos_v2
            )
        else:
            App.get_running_app().root.current_screen.ids["c3"].width = dp(400)
        try:
            chart3.update()
        except:
            print("chart3 fail")
            # chart3.update()
        
        ##loads all shows from /pp   ###Client!!!
        pos_k2, pos_v2, pos_l = libs.lib_parse2.load_full_pp(
            ad, "json_pps.json", "CLIENT"
        )
        if len(pos_k2) < 1:
            pos_k2 = [0]
            pos_v2 = [0]
        chart4 = App.get_running_app().root.current_screen.ids["c4"]
        chart4.x_values = pos_v2
        chart4.y_values = pos_v2
        chart4.x_labels = pos_k2
        if 100 * len(pos_v2) > dp(300):
            App.get_running_app().root.current_screen.ids["c4"].width = dp(80) * len(
                pos_v2
            )
        else:
            App.get_running_app().root.current_screen.ids["c4"].width = dp(400)
        try:
            chart4.update()
        except:
            print("chart4 fail")

        "LOAD BUILDING AUTOMATIC"
        
        pos_k2, pos_v2, pos_v3 = libs.lib_parse2.load_full_pp(
            ad, "json_pps.json", "VENUE"
        )
        chart5 = App.get_running_app().root.current_screen.ids["c5"]
        chart5.x_values = pos_v2
        chart5.y_values = pos_v2
        chart5.x_labels = pos_k2
        if 100 * len(pos_v2) > dp(300):
            App.get_running_app().root.current_screen.ids["c5"].width = dp(70) * len(
                pos_v2
            )
        else:
            App.get_running_app().root.current_screen.ids["c5"].width = dp(400)

        try:
            chart5.update()
        except:
            print("chart5 fail")
        
        """
        chart_list = []
        chart_list.append(self.pos_chart)
        chart_list.append(self.type_chart)
        chart_list.append(self.paycheck_amount_chart)
        chart_list.append(self.client_chart)

        chart_list.append(self.future_pos)
        chart_list.append(self.future_venue)
        chart_list.append(self.future_type)
        chart_list.append(self.venue_chart)

        for i in range(len(chart_list)):
            chart = [0] * len(chart_list)
            "LOAD BUILDING AUTOMATIC"
            pos_k2, pos_v2, pos_v3 = libs.lib_parse2.load_full_pp(
                ad, chart_list[i]["file"], chart_list[i]["filter"]
            )
            chart[i] = App.get_running_app().root.current_screen.ids[
                chart_list[i]["id"]
            ]
            chart[i].x_values = pos_v2
            chart[i].y_values = pos_v2
            chart[i].x_labels = pos_k2
            App.get_running_app().root.current_screen.ids[
                chart_list[i]["id"]
            ].width = dp(80) * len(pos_v2)

            #        chart_list[i]["id"]
            #    ].width = dp(80) * len(pos_v2)
            # if 100 * len(pos_v2) > dp(300):
            ##    App.get_running_app().root.current_screen.ids[
            #        chart_list[i]["id"]
            #    ].width = dp(80) * len(pos_v2)
            # else:
            #    App.get_running_app().root.current_screen.ids[
            #        chart_list[i]["id"]
            #    ].width = dp(40)
            App.get_running_app().root.current_screen.ids[
                chart_list[i]["id"] + "d"
            ].text = chart_list[i]["name"]
            try:
                chart[i].update()
            except:
                print("chart5 fail")
            if chart_list[i]["name"] == "Paycheck Amount":
                check = App.get_running_app().root.current_screen.ids["c3d"]
                ave, tot = self.check_stats(pos_v2)
                check.secondary_text = "Total: $" + str(ave)
                check.tertiary_text = "Average:  $" + str(tot)
                check.text = "Paychecks: " + str(len(pos_v2))
                # App.get_running_app().root.current_screen.ids[
                #    chart_list[i]["id"]
                # ].height = (self.mheight * 2)

    def add_message_to_chat(self, message):
        import libs.lib_firefriend

        import libs.lib_new

        js = libs.lib_new.get_json_schedule_1(x, ad)
        gg = js["shows"][today_index]
        import libs.lib_firefriend

        print(message, "sending message")

        libs.lib_firefriend.try_add_chat(self, gg, x, message)
        toast("Success!")
        self.do_chat(0)

    def do_chat(self, show):
        # print(show)

        self.root.set_current("chat")
        self.root.current_screen.ids["history_list"].clear_widgets()
        # test_message = "hello w2orld with a super long random string and stuff attached to it to make it seem longer"

        import libs.lib_new
        from kivymd.uix.dialog import MDDialog as md33

        js = libs.lib_new.get_json_schedule_1(x, ad)
        gg = js["shows"][today_index]
        import libs.lib_firefriend

        App.get_running_app().root.current_screen.ids["show_info"].text = gg["show"]
        App.get_running_app().root.current_screen.ids["show_info"].secondary_text = gg[
            "date"
        ]
        z = libs.lib_firefriend.view_chat(self, gg, x)
        # print(z)

        # print(gg)

        for i in range(len(z)):
            try:
                # t = z[i]["name"] + " " + z[i]["message"] + "[size=1 sp]***" + str(i)
                self.root.current_screen.ids["history_list"].add_widget(
                    ThreeLineListItem(
                        text=z[i]["message"],
                        secondary_text="[size=15dp]" + z[i]["name"],
                        tertiary_text="[size=15dp]" + z[i]["date"],
                    )
                )
            except:
                print(z[i], "failure")

    def update_profile(self):
        bio = App.get_running_app().root.current_screen.ids["bio"].text
        phone = App.get_running_app().root.current_screen.ids["phone"].text
        nick = App.get_running_app().root.current_screen.ids["nick"].text
        button4 = App.get_running_app().root.current_screen.ids["button4"].text
        # print(bio, phone, nick, pic)
        x["bio"] = bio
        x["phone"] = phone
        x["nick"] = nick
        x["button4"] = button4
        import libs.lib_updateuserdata

        libs.lib_updateuserdata.updateuser(x, ad)

        import libs.lib_firefriend

        t = libs.lib_firefriend.update_user_profile(x)
        toast(t)

    def do_profile(self):
        print("profile")
        l = ["bio", "phone", "nick", "button4", "name"]
        self.root.set_current("profile")
        for i in range(len(l)):

            try:
                App.get_running_app().root.current_screen.ids[l[i]].text = x[l[i]]
            except:
                print(x[l[i]])
        # App.get_running_app().root.current_screen.ids["phone"].text = x["phone"]
        # App.get_running_app().root.current_screen.ids["nnmae"].text = x["nname"]
        # App.get_running_app().root.current_screen.ids["button4"].text = x["button4"]
        # App.get_running_app().root.current_screen.ids["name"].text = x["name"]

    def do_db(self):
        print(
            "db",
        )
        import libs.lib_fire

        libs.lib_fire.idk(App, ad, x)

    def check_att(self, b):
        global x
        global ad

        app = App.get_running_app()
        ad = app.user_data_dir
        # config_file=ad

        import libs.lib_readuserdata

        x = libs.lib_readuserdata.readuserdata(App, ad, ios)

        # x[b] = False
        app = App.get_running_app()
        ad = app.user_data_dir
        import libs.lib_updateuserdata

        try:
            print("already set")
            return x[b]

        except:
            print("not set yet")

            x[b] = "False"
            libs.lib_updateuserdata.updateuser(x, ad)
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
        # rv = self.root.ids.rv
        # self.data = [self.create_random_input(rv, index) for index in range(20)]

        # self.root.set_current("home")

    def on_start(self):
        toast(str(tic - time.perf_counter()))
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
        # print(x, "lol")

        # self.do_login("", useold)

        import subprocess

        try:
            asdf = (
                subprocess.check_output(["git", "rev-parse", "--short", "HEAD"])
                .decode("ascii")
                .strip()
            )
        except:
            asdf = "1.1"
        print(asdf)

        try:
            if x["today_start"] == False:
                self.newstart("", useold)

            if x["today_start"] == True:
                toast("Success " + asdf)
                self.today()
        except:
            self.today()

    def callback(self, instance_button):
        print(
            self.alert,
        )
        b = instance_button.text
        nb = int(b[-1])
        self.alert.dismiss()
        if nb < 2:

            self.do_onboarding(nb + 1)
        if nb == 9:
            self.alert.dismiss()
        if nb == 8:

            self.alert.dismiss()
            self.root.set_current("login")

    def do_onboarding(self, i):
        s = "[size=20dp]"
        title = ["Hello", "First Step:", "Extras:"]
        text = [
            s + "Welcome to Schedulara",
            s + "1. Click the MENU button\n2. Click Settings\n3. Click Login",
            s + "Notifications\nGoogle Calendar Export\n\Cloud Backups",
        ]
        b_b = s + "Next", s + "Next", s + "Login"
        b_b2 = s + "Skip", s + "Skip", s + "Demo"

        from kivymd_extensions.sweetalert import SweetAlert

        button_ok = MDRaisedButton(
            text=b_b[i] + "[size=0]" + str(i),
            font_size=16,
            on_release=self.callback,
        )
        button_cancel = MDFlatButton(
            text=b_b2[i] + "[size=0]" + "9",
            font_size=16,
            on_release=self.callback,
        )
        button_login = MDFlatButton(
            text=b_b[i] + "[size=0]" + "8",
            font_size=16,
            on_release=self.callback,
        )
        bb = (
            [button_ok, button_cancel],
            [button_ok, button_cancel],
            [button_login, button_cancel],
        )
        self.alert = SweetAlert()
        self.alert.fire(title[i], text[i], buttons=bb[i])
        return True

    def soon(self, b):
        toast("Coming Soon!")
        print(b)

    def show_profile(self, name, d, zzl, i):
        from kivymd.uix.dialog import MDDialog as md33
        import libs.lib_firefriend

        cat = "nothing"
        r = "what is r"

        # gg=str(name)

        self.dialog_name = [0] * (int(zzl) + 1)
        # for q in range(len(profile)):
        #    print(profile[q]["name"], q)
        # print(profile[i]["name"], name, i, "why")
        # print(profile[i], "what emails bitch")
        pro = libs.lib_firefriend.get_profile(profile[i]["Email"])
        # print(pro)
        # pro.value
        # (name2) = pro.items()
        # print(
        #    name2,
        # )
        try:
            for key, value in pro.items():
                print(key, value)
            prof = (
                "[size=30]"
                + key
                + "\n[/size]"
                + value["City"]
                + "\n"
                + value["NickName"]
                + "\n"
                + value["Phone"]
                + "\n"
                + value["bio"]
            )
        except:
            print(profile[i])
            prof = profile[i]["name"]
            toast("profile not found :(")

        # print(i, zzl, self.dialog_name, "WHATTTTT")
        if not self.dialog_name[i]:
            self.dialog_name[i] = md33(
                text=str(prof),
                type="custom",
                #
                # content_cls=Content(),
                buttons=[
                    MDFlatButton(
                        text="Add Friend",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_release=self.soon,
                    ),
                    MDFlatButton(
                        text="Hide",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_release=self.soon,
                    ),
                    MDFlatButton(
                        text="Block",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_release=self.soon,
                    ),
                ],
            )

        self.dialog_name[i].open()

    def print_id(
        self,
        a,
        b,
    ):

        # print("bla", type(a), type(b), "\nblabla")
        # print(a, b.index)

        # print("bla222", (data), (b), "\nblabla222")
        name = a.row_data
        name = name[0]
        # print(name)
        # print(dir(b))
        # print("OMG")
        zz = int(b.index) / 5
        zzl = zz * 5
        zz = str(zz)
        # print(zz, "zzzzzz")
        i, r = str.split(zz, ".")
        i = int(i)
        name = name[i * 5]
        self.show_profile(name, 1, zzl, i)

    def check_in(self, gg):
        global profile
        global profile_data
        # print(gg, x)
        self.dialog_close()
        #
        self.root.set_current("checkin")
        self.root.current_screen.ids["check_id"].clear_widgets()

        import libs.lib_firefriend

        names, t, d = libs.lib_firefriend.try_add_show(App, gg, x)
        toast(t)
        profile = d
        # print(profile, "WHY YOU SUCK)")
        """
        names = libs.lib_firefriend.add_show(App, gg, x)
        names = libs.lib_firefriend.add_show(App, gg, x)
        names = libs.lib_firefriend.add_show(App, gg, x)
        names = libs.lib_firefriend.add_show(App, gg, x)
        names = libs.lib_firefriend.add_show(App, gg, x)
        names = libs.lib_firefriend.add_show(App, gg, x)
        """
        # print(names)

        tables = MDDataTable(
            # size_hint=(0.9, 0.6),
            #
            # background_color_selected_cell=self.theme_cls.primary_light,
            column_data=[
                ("Name", dp(20)),
                ("Pos", dp(20)),
                ("Time", dp(20)),
                ("Stamp", dp(10)),
                ("Type", dp(20)),
            ],
            row_data=[
                names
                # "a","b","c"
                # The number of elements must match the length
                # of the `column_data` list.
            ],
        )
        tables.bind(on_row_press=self.print_id)
        # tables.bind(lambda x, y=d,: self.print_id(y))
        # tables.bind(
        #    on_row_press=(
        #        lambda x, y=(
        #            "x",
        #            "x",
        #            d,
        #        ): self.print_id(names, tables, d)
        #    )
        # )

        # (lambda x, y=d,: self.print_id(y))
        self.root.current_screen.ids["check_id"].add_widget(tables)

    def pop_new(self, d):

        global today_index
        today_index = d

        import libs.lib_new
        import libs.lib_makeuserdata
        from kivymd.uix.dialog import MDDialog as md33

        js = libs.lib_new.get_json_schedule_1(x, ad)
        gg = js["shows"][d]
        # print(gg)
        ngg = (
            gg["show"]
            + "\n"
            + gg["date"]
            + " "
            + gg["time"]
            + " "
            + gg["pos"]
            + "\n"
            + gg["venue"]
            + ""
            + gg["location"]
            + "\n"
            + gg["client"]
            + "\n"
            + gg["status"]
        )
        libs.lib_makeuserdata.makeshowfile(App, gg, ad, False)
        cat = "nothing"
        r = "what is r"
        if not self.dialog2[d]:
            self.dialog2[d] = md33(
                text=str(ngg),
                type="custom",
                #
                # content_cls=Content(),
                buttons=[
                    MDFlatButton(
                        text="Save Time",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_release=lambda x, y=(gg): self.add_google_calendar(y),
                    ),
                    MDFlatButton(
                        text="Check In",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_release=lambda x, y=(gg): self.check_in(y),
                    ),
                    MDFlatButton(
                        text="$",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_release=lambda x, y=(cat, r, d): self.animate_money_new(y),
                    ),
                ],
            )

        self.dialog2[d].open()

    def today(self):
        import humanize
        from datetime import datetime

        self.root.set_current("today")
        self.root.get_screen("today").ids["pic"].source = self.get_wall("theme")
        import libs.lib_new

        #####hustle error checks
        try:
            js = libs.lib_new.get_json_schedule(x, ad)
        except:
            toast("login failed")
            return "fail"
        shows = js["shows"]
        li = ["first", "second", "third"]
        ns = 3
        if len(shows) < 3:
            ns = len(shows)
        for i in range(ns):
            show_date = datetime.strptime(shows[i]["date"], "%m/%d/%Y")
            show_date = show_date.strftime("%A, %m/%d")
            z = shows[i]["time"]
            h, m = str.split(z, ":")
            h = int(h)
            print(h)
            ppp = " AM"
            h2 = h
            if h == 12 and m == "00":
                ppp = " Noon"

            if h == 24 and m == "00":
                ppp = " Midnight"

            if h > 12:
                h2 = h2 - 12
                ppp = " PM"

            ntime = str(h2) + ":" + m + "[sup]" + ppp
            color = ""
            if shows[i]["canceled"] == True:
                color = "[color=#ff0000]"

            self.root.get_screen("today").ids[li[i]].text = (
                color + show_date + " " + ntime
            )
            self.root.get_screen("today").ids[li[i]].secondary_text = (
                color + shows[i]["show"]
            )
            self.root.get_screen("today").ids[li[i]].tertiary_text = (
                color + shows[i]["venue"]
            )

        numshows = len(shows)
        numconf = js["num_shows"]
        confirmable = numshows - numconf
        try:
            update = js["updated"]

            old_update = datetime.strptime(update, "%Y-%m-%d %H:%M:%S.%f")
            now = datetime.now()
            diff2 = humanize.naturaltime(now - old_update)
            next_show = shows[0]["date"] + " " + shows[0]["time"]
            next_show = datetime.strptime(next_show, "%m/%d/%Y %H:%M")
            diff3 = humanize.naturaltime(now - next_show)
        except:
            diff2 = ""
            diff3 = ""
        # print(diff2)

        if numconf == 0:
            stat_text = str(numshows) + " Confirmed"
        if numconf == 1:
            stat_text = str(numconf) + " Show Confirmable.  Click To Confrim"
        if numconf > 1:
            stat_text = str(numconf) + " Shows Confirmable.  Click To Confrim All"
        stat_text2 = "Next show in " + diff3
        stat_text3 = "Last updated " + diff2

        self.root.get_screen("today").ids["stats"].text = stat_text

        self.root.get_screen("today").ids["stats"].secondary_text = stat_text2
        self.root.get_screen("today").ids["stats"].tertiary_text = stat_text3

        paydate, payperiod = self.find_pay_date()

        paylist = self.root.get_screen("today").ids["pay"]
        paylist.text = "Next Payday:  " + paydate
        paylist.secondary_text = "Current Payperiod: " + payperiod
        # paylist.tertiary_text = "third" + payperiod
        if x.get("onboarding") == None:
            b = self.do_onboarding(0)
            x["onboarding"] = True
            import libs.lib_updateuserdata

            libs.lib_updateuserdata.updateuser(x, ad)

    def find_pay_date(self):

        firstdate = datetime.date(2022, 6, 28)
        #:
        now = datetime.datetime.now()
        now = datetime.date.today()
        flag = False
        z = 0
        # while flag == False or z < 50:
        # while z < 50:
        while flag == False:

            nextdate = firstdate + datetime.timedelta(days=14)
            print(nextdate)
            lastdate = nextdate + datetime.timedelta(days=13)
            # print(type(nextdate), type(now), lastdate, flag, z)
            # print(nextdate - now)
            if nextdate >= now:
                flag = True
                print("omg", flag)
            firstdate = nextdate
            z = z + 1
        lastdate = nextdate - datetime.timedelta(days=7)
        lastdate1 = lastdate - datetime.timedelta(days=14)
        l = self.format_date(lastdate, "short")
        l2 = self.format_date(lastdate1, "short")
        a = self.format_date(firstdate, "full")

        return a, l2 + " - " + l

    def check_confirm(self):
        import libs.lib_new

        app = App.get_running_app()
        ad = app.user_data_dir
        # print(x, "BLABLABLA", ad)
        xx9 = libs.lib_new.just_get_json_schedule(x, ad)
        # print("check confirm", xx9)
        print(xx9["num_shows"], "NUMSHOWS")
        if xx9["num_shows"] > 0:
            print(xx9["num_shows"])
            self.new_confirm("all")
            toast("Success")
            self.update()

    def make_toast(self, b):
        print(x, b)

    def update(self):
        print("only updating schedule")
        import libs.lib_new

        libs.lib_new.make_json_schedule(x, ad)
        print("updated schedule")
        self.today()

    def open_panel2(self, xx, i, l, junk, z):

        print("adf", xx, i, l)

        global i9
        global xx9

        xx9 = xx
        i9 = i

    def open_panel(self, xx, i, l, junk, z):
        try:
            global i9
            global xx9
            global s_index

            s_index = z

            xx9 = xx
            i9 = i
            print("asdfasdf", xx9, i, l, z)

            rw = RecipeLine(text=(str("loll")))
            # rw = IngredientDialog(text=("lol"))
            # for x in range(10):
            # self.root.current_screen.ids["rlist"].clear_widgets()
            if junk == False:
                self.root.get_screen("newhome").ids.rlist.children[
                    0
                ].content.clear_widgets()
                self.root.get_screen("newhome").ids.rlist.children[0].content.ids[
                    "pos"
                ].text = xx9["pos"]

                self.root.get_screen("newhome").ids.rlist.children[0].content.ids[
                    "pos"
                ].secondary_text = xx9["pos"] + str(z)

                pp = (
                    self.root.get_screen("newhome")
                    .ids.rlist.children[0]
                    .content.ids["pos"]
                    .text
                )
                try:
                    self.root.current_screen.ids["rlist"].children[
                        (l - i9) - 1
                    ].content.ids["pos"].text = (
                        xx9["pos"] + " " + xx9["type"] + " " + xx9["status"]
                    )
                    self.root.current_screen.ids["rlist"].children[
                        (l - i9) - 1
                    ].content.ids["pos"].secondary_text = (xx9["venue"] + " " + " ")

                    self.root.current_screen.ids["rlist"].children[
                        (l - i9) - 1
                    ].content.ids["pos2"].text = (
                        xx9["client"] + " \n" + xx9["job"] + " \n"
                    )

                    self.root.current_screen.ids["rlist"].children[
                        (l - i9) - 1
                    ].content.ids["pos2"].secondary_text = xx9["notes"]
                    print("old stuff,", l, i9)
                except:
                    print(l, i9, "failed to open")

            if junk == True and x["usecache"] == False:
                self.root.current_screen.ids["rlist"].children[(l)].content.ids[
                    "pos"
                ].text = (str(i) + " " + str(l))
                print("newconfirm you nuts")
                self.new_confirm("all")

            # print(pp)
            # print(x)
            # App.get_running_app().root.current_screen.ids["rlist"].text = "posss"
            # print(App.get_running_app().root.current_screen.ids)
            # zz = dir(self.root.get_screen("newhome").ids.rlist.children[0])
            pass
        except:
            toast("failed to make list")
            self.newstart("", False)

    def close_panel(self, what):
        Pass
        print(what)

    def newstart(self, search, useold):
        import libs.lib_bonus

        self.root.set_current("newhome")
        self.root.current_screen.ids["rlist"].clear_widgets()

        import libs.lib_new

        js = libs.lib_new.get_json_schedule(x, ad)
        if useold == False:
            shows = js["shows"]
        if useold == True:
            shows = js["old_shows"]
        rshows = (len(shows)) - (js["num_shows"])
        if useold == False:
            if js["num_shows"] > 0:
                ttt = str(rshows) + "/" + str(len(shows)) + " shows confirmed"
            else:
                ttt = str(len(shows)) + " shows confirmed"

            panel = MDExpansionPanel(
                # icon="recipe.png",
                content=Content(),
                panel_cls=MDExpansionPanelThreeLine(
                    text=ttt,
                    # content=Content(),
                    # secondary_text=shows[z]["show"],
                    # tertiary_text=shows[z]["venue"],
                    text_color=(1, 0, 1, 0),
                    on_open=lambda x, y=js, q=0,: self.open_panel(y, q),
                    on_close=self.close_panel,
                ),
            )
            panel.bind(
                on_open=lambda x, y=js, q="Click to Confirm All", l=js[
                    "num_shows"
                ], p=True: self.open_panel(y, q, l, p),
                on_close=self.close_panel,
            )

            self.root.get_screen("newhome").ids.rlist.add_widget(panel)
            canned = -1

            for z in range(len(shows)):
                color = ""
                # print(shows[z])
                # if shows[z]["canceled"] == True:
                if 1 == 1:
                    canned = canned + 1
                if shows[z]["status"] != "Confirmed":
                    color = "[color=#00ff00]"
                if shows[z]["canceled"] == True:
                    color = "[color=#ff0000]"
                if shows[z]["old"] == True:
                    color = color + "[size=3sp]"
                    color = "[color=#555555]"
                if shows[z]["old"] == True and shows[z]["canceled"] == True:
                    color = color + "[size=3sp]"
                    color = "[color=#550000]"

                panel = MDExpansionPanel(
                    # icon="recipe.png",
                    content=Content(),
                    panel_cls=MDExpansionPanelThreeLine(
                        text=color + shows[z]["date"] + "\n" + shows[z]["time"],
                        # content=Content(),
                        text_color=(1, 0, 1, 0),
                        secondary_text=color + shows[z]["show"],
                        tertiary_text=color + shows[z]["venue"],
                        on_open=lambda x, y=shows[z], q=canned: self.open_panel(y, q),
                        on_close=self.close_panel,
                    ),
                )
                panel.bind(
                    on_open=lambda x, y=shows[z], q=canned, l=len(
                        shows
                    ), junk=False, bb=z: self.open_panel(y, q, l, junk, z),
                    on_close=self.close_panel,
                )
                # if shows[z]["canceled"] == True:
                if 1 == 1:
                    self.root.get_screen("newhome").ids.rlist.add_widget(panel)
                libs.lib_bonus.create_notification(shows[z], x, True, ad)
        if useold == True:
            canned = -1
            for z in range(len(shows)):
                color = ""
                # print(shows[z])
                # if shows[z]["canceled"] == True:
                if 1 == 1:
                    canned = canned + 1
                if shows[z]["status"] != "Confirmed":
                    color = "[color=#00ff00]"
                if shows[z]["canceled"] == True:
                    color = "[color=#ff0000]"
                if shows[z]["old"] == True:
                    color = color + "[size=3sp]"
                    color = "[color=#555555]"
                if shows[z]["old"] == True and shows[z]["canceled"] == True:
                    color = color + "[size=3sp]"
                    color = "[color=#550000]"

                panel = MDExpansionPanel(
                    # icon="recipe.png",
                    content=Content2(),
                    panel_cls=MDExpansionPanelThreeLine(
                        text=color + shows[z]["date"] + "\n" + shows[z]["time"],
                        # content=Content(),
                        text_color=(1, 0, 1, 0),
                        secondary_text=color + shows[z]["show"],
                        tertiary_text=color + shows[z]["venue"],
                        on_open=lambda x, y=shows[z], q=canned: self.open_panel2(y, q),
                        on_close=self.close_panel,
                    ),
                )
                panel.bind(
                    on_open=lambda x, y=shows[z], q=canned, l=len(
                        shows
                    ), junk=False, z=z: self.open_panel2(y, q, l, junk, z),
                    on_close=self.close_panel,
                )
                # if shows[z]["canceled"] == True:
                if 1 == 1:
                    self.root.get_screen("newhome").ids.rlist.add_widget(panel)
        toast(str(tic - time.perf_counter()))

    def showinfo(self, cat, r, d):

        from kivymd.uix.dialog import MDDialog as md33

        # for ingredient in ingredients:
        #    ingredients_text += ingredient + "\n"
        # self.dialog = IngredientDialog(text=ingredients_text)
        # self.dialog.open()
        print(cat, r, d)
        # r = ""
        if not self.dialog2[d]:
            self.dialog2[d] = md33(
                text=r,
                type="custom",
                #
                # content_cls=Content(),
                buttons=[
                    MDFlatButton(
                        text="Email Times,",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_release=lambda x, y=(cat, r, d): self.email_time(y),
                    ),
                    MDFlatButton(
                        text="Save Time",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        # on_release=self.email_time,
                    ),
                    MDFlatButton(
                        text="Confirm",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_release=lambda x, y=(cat, r, d): self.new_confirm(y),
                    ),
                ],
            )

        self.dialog2[d].open()

    def new_confirm(self, asdf):
        import libs.lib_new

        xx9 = libs.lib_new.get_json_schedule(x, ad)
        # print("save_time", xx9, x)

        try:
            print(asdf, str(xx9["confirmables"]), "OMG ITS CONFIRMING ITSELF")
        except:
            print("one?", asdf)
        if asdf == "all":
            for xxx in range(int(xx9["num_shows"])):
                fail = self.confirm_real(xx9["confirmables"][xxx])
                print((xx9["confirmables"][xxx]), "whattttttttt")
        if asdf != "all":
            if xx9.get("confirable"):
                print(xx9["confirable"], "DO CONFIRM THIS")
                fail = self.confirm_real(asdf)
                print(fail)
                toast("Confirmed")
                self.update()
                self.newstart("", False)
                for u in range(len(self.dialog2)):
                    try:

                        self.dialog2[u].dismiss(force=True)
                    except:
                        print(u)

        else:
            print(
                "one",
                profile,
            )
            # fail = self.confirm_real(asdf)

    def email_time(self, x2):
        print("save_time", xx9, x)

        try:
            endtime = str(x["endtime"])
        except:
            endtime = "??"
            ##TODO make clock thing

        try:
            lunches = str(x["lunches"])
            if lunches > 1:
                es = "es"
        except:
            lunches = "??"
            ##TODO MAKE LUNCHES
            es = ""

        # ee = f"Hi,\nI worked {str(xx9["show"])}  {str(xx9["job"])} at {str(xx9["venue"])} on {str(xx9["date"])} from {str(xx9["venue"])} to {str(xx9["endtime"])}\n Thanks,\n{str(x["name"])}"
        ee = f"Hi,\nI worked {str(xx9['show'])}  ({str(xx9['job'])}) at {str(xx9['venue'])} on {str(xx9['date'])} from {str(xx9['time'])} to {endtime} with {lunches} walkaway lunch{es}\nThanks, {str(x['name'])}"
        # print(ee)
        from kivymd.uix.dialog import MDDialog as md33
        from kivy.core.clipboard import Clipboard

        if not self.dialog3:
            self.dialog3 = md33(
                text=ee,
                type="custom",
                #
                # content_cls=Content(),
                buttons=[
                    MDFlatButton(
                        text="Copy",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_release=lambda x, y=(ee): Clipboard.copy(ee),
                    ),
                ],
            )

        self.dialog3.open()

    def copy_email(self, eee):
        print("email_times", eee)

    def ingredients_list(self, selected_cat, selected_r):
        for category in self.card_file:
            if category["Category"] == selected_cat:
                for recipe in category["Recipes"]:
                    if recipe["title"] == selected_r:
                        return recipe["shopping list"]

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

        xxx, mjds, name = libs.lib_parse.parse(sch, ad, x["usecache"], x)

        print(x, "XXXXXXX")
        x["name"] = name
        import libs.lib_updateuserdata as lib_updateuserdata

        lib_updateuserdata.updateuser(x, ad)

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
        toast("lol" + str(tic - time.perf_counter()))
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

        
        newercolor = newcolor
        xxxx = xxx + "wtf" + str(idex)
        

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
    dialog2 = [None, None, None, None, None, None]
    dialog_name = None
    dialog3 = None

    snackbar = None
    rreverse = True
    menurotate = 10
    menuscale = 0.5, 0.5

    def update_hi_score_keys(self):
        print("updating scores")
        import libs.lib_ach

        win = libs.lib_ach.download_ach(ad)
        toast(win)

    def update_hi_score_data(self, ach):
        print("updating scores")
        import libs.lib_score

        win = libs.lib_score.dl_score(x["name"], ach, ad)
        toast(win)
        self.ach_top(ach)

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

    def get_wall(self, page):
        # self.root.set_current(page)

        print(x, "assert")
        try:
            b = "images/walls/" + x["wall"] + ".jpg"
        except:
            b = "images/walls/" + "rhino" + ".jpg"
        try:
            self.root.get_screen(page).ids["pic"].source = b
            print("success set image")
        except:
            print("fail to set image")
            pass

        return b

        # self.root.current = "settings"

    def menu_callback(self, text_item, v, v2):
        # print(location[text_item])
        # print (text_item,type(text_item))
        # print(v[text_item], "v[text")
        # print(text_item, v2, v, "dumbass")
        if v2 == "name":
            toast(str(v[text_item][v2]))
            App.get_running_app().root.current_screen.ids[
                "last_restore"
            ].secondary_text = str(v[text_item][v2])
        if v2 == "city":
            App.get_running_app().root.current_screen.ids["button4"].text = str(
                v[text_item]
            )
        if v2 == "pcolor":
            App.get_running_app().root.current_screen.ids["button4"].text = str(
                v[text_item]
            )
            self.theme_cls.primary_palette = v[text_item]

        if v2 == "wall":
            App.get_running_app().root.current_screen.ids["button5"].text = str(
                v[text_item]
            )
            self.root.set_current("theme")
            self.root.get_screen("theme").ids["pic"].source = self.get_wall("theme")

        # self.root.get_screen(v2).ids["button4"].text = v[text_item]
        global x
        x[v2] = v[text_item]
        print(x)
        import libs.lib_updateuserdata as lib_updateuserdata

        lib_updateuserdata.updateuser(x, ad)

    def choose_drop(self, v, v2):
        "oll"
        print(v2, v, "THISISTHETHING2")

        if v2 == "city":
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
        if v2 == "name":
            menu_items = [
                {
                    "text": f"{v[i][v2]}",
                    # "scroll_type": ['bars'],
                    # "effect_cls": "ScrollEffect",
                    "viewclass": "OneLineListItem",
                    "on_release": lambda x=i: self.menu_callback(x, v, v2),
                }
                for i in range(len(v) - 1)
            ]
        if v2 == "pcolor":
            menu_items = [
                {
                    "text": "[color=" + webcolors.name_to_hex(v[i]) + "]" + v[i],
                    # "scroll_type": ['bars'],
                    # "effect_cls": "ScrollEffect",
                    "viewclass": "OneLineListItem",
                    "on_release": lambda x=i: self.menu_callback(x, v, v2),
                }
                for i in range(len(v) - 1)
            ]
        if v2 == "wall":
            menu_items = [
                {
                    "text": v[i],
                    # "scroll_type": ['bars'],
                    # "effect_cls": "ScrollEffect",
                    "viewclass": "OneLineListItem",
                    "on_release": lambda x=i: self.menu_callback(x, v, v2),
                }
                for i in range(len(v) - 1)
            ]

            # self.root.

        # print(self.root.get_screen("notification").ids)
        self.menu = MDDropdownMenu(
            # caller=self.root.get_screen("notification").ids["button4"],
            caller=App.get_running_app().root.current_screen.ids["button4"],
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

        import libs.lib_updateuserdata

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

    def about(self):
        self.root.set_current("about")

    def ach_top(self, lol):
        print("achtop", lol)
        from kivy.metrics import dp
        from kivy.uix.anchorlayout import AnchorLayout

        self.root.set_current("achscore")
        self.root.current_screen.ids["graphs3"].clear_widgets()
        import libs.lib_score

        name = x["name"]
        scores, place, q = libs.lib_score.parse_score(
            name, lol, ad, self.theme_cls.primary_color
        )

        print(q, "SCORESSSS", place)
        tables = MDDataTable(
            # size_hint=(0.9, 0.6),
            #
            # background_color_selected_cell=self.theme_cls.primary_light,
            column_data=[
                ("Points", dp(20)),
                ("Name", dp(30)),
                ("Rank", dp(20)),
            ],
            row_data=[
                q
                # The number of elements must match the length
                # of the `column_data` list.
            ],
        )

        self.root.current_screen.ids["graphs3"].add_widget(tables)

    def ach_info(self, data):
        print("info ach", data)
        self.root.set_current("achinfo")
        self.root.current_screen.ids["ach_info_id"].clear_widgets()
        dd = [
            [data["name"], data["disc"]],
            ["Date Achieved:", data["date_achieved"]],
            [data["ach_extra"], (data["ach_progress"])],
            ["Points:", data["ach_level"]],
        ]
        shows = ""
        # print(data["ach_shows"])
        # print(type(data["ach_shows"]))
        # print("LISTNODATA")
        try:
            newd = dict(
                sorted(
                    data["ach_shows"].items(), key=lambda item: item[1], reverse=True
                )
            )
            keys = list((newd).keys())
            values = list((newd).values())
            totshows = 0
            for x in range(len(values)):
                totshows = totshows + values[x]
        except:
            newd = data["ach_shows"]
            keys = data["ach_shows"]
            values = data["ach_shows"]

        # (keys,values) = zip(*tel.items())

        # shows = "[font=Roboto-Regular]" + shows + "[/font]"
        # print(f"{a:10}{b:10}{c:10}"
        # print(shows)

        for z in range(len(dd)):
            # print(str(dd[z][0],str(dd[z][1])
            items = TwoLineAvatarListItem22(
                text=str(dd[z][0]),
                secondary_text=str(dd[z][1]),
                # icon=real_icon,
                # on_release=lambda x, y=data[i]: self.ach_info(y),
            )

            self.root.current_screen.ids["ach_info_id"].add_widget(items)

        # self.root.current_screen.ids["ach_info_id"].add_widget(SmoothLabel(text=self.ids.msg.text, size_hint_x=0.5, size_hint_y=0.1, pos_hint={"x": 0.1, "top": 0.8}, background_color=(0.2, 0.6, 1, 1)))
        # keys.insert(0, "Pos:")
        # values.insert(0, "#:")
        first = 30
        second = 20
        third = 20
        for m in range(len(keys)):
            print(keys)
            if data["name"] == "Hustle and Grind":
                print("jesusccc")

                # keysm = str(m)
                keysm = ""
                valuesm = data["ach_shows"][m][1]
                perc = data["ach_shows"][m][2]

                valuesm, junk, junk = str.split(valuesm, " ")
                first = 4
                third = 30
            if data["name"] == "Celery man!":
                print("jesusccc")

                # keysm = str(m)
                keysm = str(data["ach_shows"][m][0])
                print(data["ach_shows"][m])
                valuesm = data["ach_shows"][m][1]
                perc = data["ach_shows"][m][2]

                perc, junk, junk = str.split(perc, " ")
                first = 6

            if data["name"] == "Wear The Hat":
                try:
                    perc = values[m] / (totshows * 1.0)

                    perc = perc * 100
                    perc = f"{perc:.2f}%"
                    perc = str(perc)
                    keysm = str(keys[m])
                    valuesm = str(values[m])

                except:
                    perc = data["ach_graph_disc"][0]
                    keysm = data["ach_graph_disc"][1]
                    try:
                        valuesm = data["ach_graph_disc"][2]
                    except:
                        valuesm = ""
            try:
                while len(keysm) < first:
                    keysm = keysm + " "
                while len(valuesm) < 20:
                    valuesm = valuesm + " "
                while len(perc) < third:
                    perc = perc + " "

                if len(valuesm) > 15:
                    valuesm = valuesm[0:15]
                if len(perc) > 15:
                    perc = perc[0:15]
                shows = (
                    f"[font=Roboto-Regular]{keysm} {str(valuesm)} {str(perc)}[/font]\n"
                )
            except:
                print(keys)
                shows = str(keys)

            items = SmoothLabel(
                text=(shows),
                size_hint_x=0.5,
                # font_name="Roboto-Regular",
                markup=True,
                # font_size="10dp",
            )
            # if data["name"] == "Wear The Hat":
            self.root.current_screen.ids["ach_info_id"].add_widget(items)
        # if data["name"] == "Hustle and Grind":
        # self.root.current_screen.ids["ach_info_id"].add_widget(items)

    def ach_reset(self):
        print("reset ach")
        import libs.lib_ach

        libs.lib_ach.make_ach(ad)
        App.get_running_app().root.current_screen.ids[
            "ach_points"
        ].text = "Points: " + str(0)

        self.trophys("all")

    def check_ach(self):
        print("checking ach")
        import libs.lib_ach
        import libs.lib_score

        # dicts = self.load_paychecks()
        libs.lib_ach.check_scroll(self, ad, x)
        libs.lib_ach.check_hats(self, ad)

        points = App.get_running_app().root.current_screen.ids["ach_points"].text

        junk, points = str.split(points, " ")
        print(points, "POINTSITES")
        libs.lib_score.submit(x["name"], points, 0, ad)

        self.trophys("all")

    def trophys(self, select):
        # global i
        # import lib_test
        # lib_test.n22()
        from kivymd.icon_definitions import md_icons

        self.root.set_current("ach")
        self.root.current_screen.ids["ach_id"].clear_widgets()
        import libs.lib_ach

        icons = list(md_icons.keys())

        data = libs.lib_ach.list_ach(ad, select)
        points = 0
        for i in range(len(data)):
            # print(data[i])
            tt = data[i]["name"] + "\n" + data[i]["disc"] + "[size=0]" + str(i)
            # self.root.current_screen.ids["ach_id"].add_widget(
            #    ListItemWithCheckbox(
            #        text=tt, icon=icons[i], icon2=icons[i + 10], secondary_text="lalala"
            #    )
            # )
            real_icon = icons[i]
            if data[i]["achieved"] == "False":
                real_icon = "lock"
            if data[i]["achieved"] == "True":
                real_icon = data[i]["ach_icon"]
            items = TwoLineAvatarListItem22(
                text=data[i]["name"],
                secondary_text=data[i]["disc"],
                icon=real_icon,
                on_release=lambda x, y=data[i]: self.ach_info(y),
            )
            if data[i]["ach_level"] > 0:
                points = points + data[i]["ach_level"]

            # items.text_color = (1, 0, 0, 0)
            # items.icon_color = [1, 1, 0, 1]
            # items = items.text_color = self.theme_cls.text_color
            self.root.current_screen.ids["ach_id"].add_widget(items)
            App.get_running_app().root.current_screen.ids[
                "ach_points"
            ].text = "Points: " + str(points)

    def make_stats(self, start, b, e):
        self.root.set_current("stats")
        if start == "ytd":
            App.get_running_app().root.current_screen.ids[
                "scustom"
            ].md_bg_color = self.theme_cls.primary_light
            App.get_running_app().root.current_screen.ids[
                "sytd"
            ].md_bg_color = self.theme_cls.primary_dark
            App.get_running_app().root.current_screen.ids[
                "syear"
            ].md_bg_color = self.theme_cls.primary_light
            App.get_running_app().root.current_screen.ids[
                "sall"
            ].md_bg_color = self.theme_cls.primary_light
        if start == "year":
            App.get_running_app().root.current_screen.ids[
                "scustom"
            ].md_bg_color = self.theme_cls.primary_light
            App.get_running_app().root.current_screen.ids[
                "syear"
            ].md_bg_color = self.theme_cls.primary_dark
            App.get_running_app().root.current_screen.ids[
                "sytd"
            ].md_bg_color = self.theme_cls.primary_light
            App.get_running_app().root.current_screen.ids[
                "sall"
            ].md_bg_color = self.theme_cls.primary_light

        if start == "custom":
            App.get_running_app().root.current_screen.ids[
                "syear"
            ].md_bg_color = self.theme_cls.primary_light
            App.get_running_app().root.current_screen.ids[
                "scustom"
            ].md_bg_color = self.theme_cls.primary_dark
            App.get_running_app().root.current_screen.ids[
                "sytd"
            ].md_bg_color = self.theme_cls.primary_light
            App.get_running_app().root.current_screen.ids[
                "sall"
            ].md_bg_color = self.theme_cls.primary_light

        if start == "all":
            App.get_running_app().root.current_screen.ids[
                "syear"
            ].md_bg_color = self.theme_cls.primary_light
            App.get_running_app().root.current_screen.ids[
                "sall"
            ].md_bg_color = self.theme_cls.primary_dark
            App.get_running_app().root.current_screen.ids[
                "sytd"
            ].md_bg_color = self.theme_cls.primary_light
            App.get_running_app().root.current_screen.ids[
                "scustom"
            ].md_bg_color = self.theme_cls.primary_light

        from kivy.utils import get_color_from_hex

        # self.root.current = "stats"
        # self.root.current("stats")
        # self.root.set_current("stats")
        # self.root.current = "stats"

        self.root.current_screen.ids["graphs"].clear_widgets()
        import libs.lib_makegraphs as lib_makegraphs

        if start == "custom":
            # new_finish = App.get_running_app().root.current_screen.ids["dstart"].text
            # new_start = App.get_running_app().root.current_screen.ids["dend"].text
            # new_finish = pp_date = datetime.datetime.strptime(new_finish, "%Y-%m-%d")
            # new_start = pp_date = datetime.datetime.strptime(new_start, "%Y-%m-%d")
            new_finish = e
            new_start = b
            # print(type(e), "GARBAGE")
        if start == "all":
            new_finish = datetime.datetime.now() - datetime.timedelta(days=10365)
            new_start = datetime.datetime.now()
            App.get_running_app().root.current_screen.ids["dstart"].text = str("ALL")
            App.get_running_app().root.current_screen.ids["dend"].text = str("ALL")
        if start == "ytd":
            doy = datetime.datetime.now().timetuple().tm_yday
            new_finish = datetime.datetime.now() - datetime.timedelta(days=doy)
            new_start = datetime.datetime.now()
            App.get_running_app().root.current_screen.ids["dstart"].text = str(
                new_finish.date()
            )
            App.get_running_app().root.current_screen.ids["dend"].text = str(
                new_start.date()
            )
        if start == "year":
            now = datetime.datetime.now()
            three_yrs_ago = datetime.datetime.now() - datetime.timedelta(days=365)
            new_start = now
            new_finish = three_yrs_ago
            App.get_running_app().root.current_screen.ids["dstart"].text = str(
                new_finish.date()
            )
            App.get_running_app().root.current_screen.ids["dend"].text = str(
                new_start.date()
            )
        # print(new_finish - new_start)
        (
            dd,
            dd2,
            maxd,
            maxm,
            max_dy,
            max_my,
            ins,
            outs,
            shows,
            max_t,
        ) = lib_makegraphs.parsepp(self, ad, "check", new_start, new_finish)

        lib_makegraphs.make_stats_pp(self, "Checks", dd, maxm, max_dy)

        lib_makegraphs.make_stats_pp(self, "$/Day", dd2, maxd, max_dy)
        dumb = str(f"In ~ Show ~ Out\n" + str(ins) + " " + str(shows) + " " + str(outs))
        dumb = str(f"In ~ Show ~ Out\n" + str(ins) + " " + str(shows) + " " + str(outs))
        dumb = f"In  ~  Out  ~  Show\n{ins:<4}{outs:>8}{shows:>14}"

        lib_makegraphs.make_stats_pp(
            self,
            dumb,
            [[0, ins], [1, shows], [2, outs]],
            max_t,
            3,
        )

        self.root.current_screen.ids["graphs"].add_widget(
            SwipeToDeleteItem2(text="wow+0")
        )

        self.root.set_current("stats")

    def maketransp(self):

        x = self.theme_cls.primary_color
        x[3] = 0.3
        return x

    def menuu(self):
        self.do_login("", useold)

    def test_not(self):
        print(x)
        toast("Success")

        sh = {
            "date": "10/07/2022",
            "time": "07:00",
            "show": "(TMA) MY CHEMICAL ROMANCE - PLACEHOLDER",
        }
        import libs.lib_bonus

        print(x, "dothis)")
        libs.lib_bonus.create_notification(sh, x, False, ad)

    def mainmenuf(self):
        self.root.set_current("mainmenu")
        # self.root.current_screen.ids["payperiod_list"].clear_widgets()

    def dlpp(self):
        import libs.lib_ppdownloader as lib_ppdownloader

        if x["name"] == "Test McDemo":
            toast(str("No Paychecks found for ") + x["name"])
        else:
            paystubs, new = lib_ppdownloader.thinkpp(x, ad)
            self.snackbar = Snackbar(
                text="Downloaded " + str(new) + " Paystubs out of " + str(paystubs),
                bg_color=self.theme_cls.primary_color,
            )
            self.snackbar.open()

    def ccc(self):
        print(mjds)
        confable = []
        for i in range(len(mjds)):

            if 1 == 1:
                # if mjds[i].has_key(["confirmable"]):
                if "confirmable" in mjds[i]:
                    z = mjds[i]["confirmable"]
                    print(z)
                    confable.append(mjds[i]["confirmable"])
            # except:
            #    pass
        for i in range(len(confable)):
            print(confable[i], len(confable))
        print(len(confable), "confable")
        self.snackbar = Snackbar(
            text="Success!" + str(len(confable)), bg_color=self.theme_cls.primary_color
        )
        self.snackbar.open()

    def dialog_close(self, *args):
        for z in range(len(self.dialog2)):
            try:
                self.dialog2[z].dismiss(force=True)
            except:
                print(z)

    def animate_money_new(self, y):
        self.dialog_close()
        from kivy.clock import Clock

        self.root.set_current("animate")
        print(y, xx9)

        pos = xx9["pos"]

        App.get_running_app().root.current_screen.ids["top"].text = str("call start")
        App.get_running_app().root.current_screen.ids["moneyinfo"].secondary_text = str(
            pos + " rate"
        )
        # zzz = self.root.get_screen("info").ids["lunches"].text
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

        Clock.schedule_interval(self.update_label_new, 0.1)

    def animate_money(self):
        from kivy.clock import Clock

        self.root.set_current("animate")
        pos = mjds[idex]["pos"]
        App.get_running_app().root.current_screen.ids["top"].text = str("call start")
        App.get_running_app().root.current_screen.ids["moneyinfo"].secondary_text = str(
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

    def update_label_new(self, dt):
        from datetime import datetime
        import libs.lib_extractjson as lib_extractjson

        start_time = xx9["date"] + "." + xx9["time"]
        start_time = datetime.strptime(start_time, "%m/%d/%Y.%H:%M")
        pos = xx9["pos"]
        rate = lib_extractjson.extract_pos(App, ad, pos)
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
        # zzz = self.root.get_screen("info").ids["lunches"].text
        # ot_after = float(self.root.get_screen("info").ids["ot_spin"].text)
        ot_after = 8
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

    def update_label66(self, dt):
        from datetime import datetime
        import libs.lib_extractjson as lib_extractjson

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
        import libs.lib_readuserdata

        x = libs.lib_readuserdata.readuserdata(App, ad, ios)
        print(x)
        if x["login"] == "False":
            fail = "fail"

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
        import ssl

        ssl.verify = False
        ssl._create_default_https_context = ssl._create_unverified_context
        # print (what)
        # print(len(xxx[idex]))
        try:
            # print(xxx[idex][13])
            pass
        except:
            print("nonconfirm")
            return "fail"
        dg = what
        confirmable = False
        try:
            if "dg" in dg:
                confirmable = True
                # print("trying to confirm " + str(xx9["date"]))
        except:
            print("nonconfirmable you nerd")

        # print(type(browser), "OMGWHATISTHISSTUFF", dg)
        if 1 == 1:
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
                # print(browser, "browser 2")
                control_t.readonly = False
                control_a.readonly = False

                # control_t.value = str(xxx[idex][13])
                control_t.value = str(dg)
                control_a.value = "Confirm"
                # print(browser, 'browser 3')

                response = browser.submit()
                # print(browser, 'browser 4')
                aa = response.get_data()
                # print(browser, "browser 5")

                aaa = open(ad + "/realdata.html", "wb")
                aaa.write((aa))
                aaa.close()
        # except:
        #    """"""

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

    def handle_selection(self, selection):
        """
        Callback function for handling the selection response from Activity.
        """
        # self.selection = selection
        print(selection)

    def on_selection(self, *a, **k):
        """
        Update TextInput.text after FileChoose.selection is changed
        via FileChoose.handle_selection.
        """
        App.get_running_app().root.ids.result.text = str(self.selection)

    def backup_new(self):
        results = "blablabla"
        self.results = "asdfasdfasdf"
        print("backup_omg")
        # filechooser.open_file(on_selection=self.handle_selection)

        out_file = ad + "/result.json"
        with open(out_file, "w") as ofile:
            import json

            json.dump(self.results, ofile, indent=4)

        if platform == "ios":
            self.do_share_ios(out_file, "Some title")
        if platform != "ios":
            filechooser.open_file(on_selection=self.handle_selection)

    def do_share_ios(self, data, title):
        URL = NSURL.fileURLWithPath_(data)
        UIActivityViewController = autoclass("UIActivityViewController")
        UIcontroller = sharedApplication.keyWindow.rootViewController()
        UIActivityViewController_instance = UIActivityViewController.alloc().init()
        # print(dir(UIActivityViewController_instance))
        activityViewController = UIActivityViewController_instance.initWithActivityItems_applicationActivities_(
            [URL], None
        )
        UIcontroller.presentViewController_animated_completion_(
            activityViewController, True, None
        )

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
            size_hint=(0.5, 0.5),
            size=(400 * scale, 600 * scale),
            separator_height=1,
            title_size=1,
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
        if 1 == 1:
            import libs.lib_extractjson as lib_extractjson

            # print(xxx[idex], "get_rate")
            pos = xxx[idex][8]
            rate = lib_extractjson.extract_pos(App, config_file, pos)
            print("rate mofo", rate)
            # App.get_running_app().root.current_screen.ids["rate"].text = str(rate)

            # App.get_running_app().root.current_screen.ids["venue"].text = str(rate)
            # except:
            print("failed to get rate")

            # print(xxx, "get_rate2error3")
            # pass

    def set_rate(self):
        x = xxx[idex][8]
        # rate=str(28.5)
        rate = App.get_running_app().root.current_screen.ids["rate"].text
        import libs.lib_makeuserdata as lib_makeuserdata

        lib_makeuserdata.makeposfile(App, x, config_file, ios, rate)
        print("set rate")

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
        from datetime import datetime

        print(self.root.current, "CURRENT SCREEEEEEN")
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
        print(self.root.current, "CURRENT SCREEN===:")
        if self.root.current == "stats":
            # self.make_stats("custom", "custom")
            self.make_stats("custom", date_range[-1], date_range[0])
        if self.root.current == "history":
            self.do_history()
        if self.root.current == "newstats":

            d0 = datetime.combine(date_range[-1], datetime.min.time())
            d1 = datetime.combine(date_range[0], datetime.min.time())

            self.do_new_stats(d1, d0, "Custom")
        if self.root.current == "pay":
            self.lday = datetime.combine(date_range[-1], datetime.min.time())
            self.fday = datetime.combine(date_range[0], datetime.min.time())
            self.do_payperiod()

    def updatetext(self, box):
        app = App.get_running_app()
        ad = app.user_data_dir
        debugbox = App.get_running_app().root.current_screen.ids[box].active
        x[box] = debugbox
        print(x[box], box, " SETTINGS TOGGLE")
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

    def removeAll(self):
        self.root.current_screen.ids["users_lst"].clear_widgets()

    from typing import Union

    def do_theme(self):

        specific_text_color = ""
        self.root.set_current("theme")
        self.root.get_screen("theme").ids["pic"].source = self.get_wall("theme")
        self.save_theme_picker()

    theme_settings = ""

    def do_old_theme2(self):
        self.root.set_current("theme_picker")
        self.save_theme_picker()

    def show_theme_picker(self, t):
        global theme_setting
        theme_setting = t

        # theme_dialog = MDThemePicker()
        color_picker = MDColorPicker(size_hint=(0.45, 0.45))
        color_picker.open()
        color_picker.bind(
            on_select_color=self.on_select_color,
            # on_select_color=self.on_select_color,
            on_release=self.get_selected_color,
        )

    # on_release=(lambda a: self.grabText(ttt)),
    def update_color(self, color: list) -> None:
        # self.root.ids.toolbar.md_bg_color = color
        print(color)

    def get_selected_color(
        self,
        instance_color_picker: MDColorPicker,
        type_color: str,
        selected_color: Union[list, str],
    ):
        """Return selected color."""

        print(f"Selected color is {selected_color}")
        print(theme_setting)
        self.update_color(selected_color[:-1] + [1])

        if theme_setting == "p":
            self.theme_cls.primary_palette = selected_color

        if theme_setting == "s":
            self.theme_cls.accent_palette = selected_color

        if theme_setting == "d":
            self.theme_cls.theme_style = selected_color
        # s = self.theme_cls.theme_style
        # p = self.theme_cls.primary_palette
        # a = self.theme_cls.accent_palette

        self.save_theme_picker()

    def on_select_color(self, instance_gradient_tab, color: list) -> None:
        """Called when a gradient image is clicked."""

    def save_theme_picker(self):
        s = self.theme_cls.theme_style
        p = self.theme_cls.primary_palette
        a = self.theme_cls.accent_palette
        import libs.lib_readuserdata as lib_readuserdata

        x = lib_readuserdata.readuserdata(App, ad, ios)
        # print(s, p, a, x)
        x["pcolor"] = p
        x["scolor"] = a

        try:
            if x["theme2"] == True:
                x["theme"] = "Dark"
            else:
                x["theme"] = "Light"
        except:
            x["theme"] = "Dark"
        self.theme_cls.theme_style = x["theme"]

        # print(s, p, a, x)
        import libs.lib_updateuserdata as lib_updateuserdata

        lib_updateuserdata.updateuser(x, ad)
        print(x)

    def change_screen(self, screen, direction):
        self.root.transition.direction = direction
        # self.root.current = screen
        self.root.set_current(screen)

    def load_paychecks(self):
        import glob, os
        from datetime import datetime

        try:
            os.chdir(ad + "/pp")
        except:
            os.mkdir(ad + "/pp")
            os.chdir(ad + "/pp")
        x = 0
        listofdicks = []
        # now = datetime.now()
        # print(self.fday, "now", self.lday)
        from kivy.clock import Clock

        for file in glob.glob("*.html"):
            # print (file)
            import libs.lib_parse as lib_parse

            f1 = datetime.strptime(file, "%m-%d-%Y.html")
            dd, junk, junk, junk, junk, junk = lib_parse.parsepayperiod(
                ad + "/pp/" + file
            )
            if self.fday <= f1 and f1 <= self.lday:
                listofdicks.append(dd)
                x = x + 1
            # print(x)
            # toast("loaded:" + str(x))
            # Clock.schedule_once(self.dumb(x))

        return listofdicks

    def dumb(self, z):
        print(z)

    def check_var(self, x):
        print(x)
        if x == True:
            return "^^"
        else:
            return "vv"

    def spinner_toggle(self):
        print("Spinner Toggle")
        app = self.get_running_app()

        sp = self.root.current_screen.ids["spinner"]
        if sp == False:
            sp = True
        else:
            sp = False

    def do_payperiod_trim(self, sort):
        if self.sort_pp == sort:
            # print("omg its equal")
            self.rreverse = not self.rreverse
            # print(self.rreverse)
        self.sort_pp = sort
        # Clock.schedule_once()
        self.do_payperiod("x")
        ## Clock.schedule_once(self.do_payperiod())

    def do_payperiod_f(self, date_rng):

        ssort = self.sort_pp
        fdate, ldate = self.get_dates(date_rng)
        # print(fdate, ldate, self.rreverse, ssort)
        self.lday = ldate
        self.fday = fdate
        self.date_range_pp = date_rng

        self.do_payperiod("None")

    def do_payperiod(self, zz):
        self.root.set_current("pay")
        self.root.get_screen("today").ids["pic"].source = self.get_wall("theme")
        from kivymd.uix.list import ThreeLineListItem
        from kivy.uix.progressbar import ProgressBar

        ssort = self.sort_pp
        rreverse = self.rreverse
        print(rreverse, "REVERSE")

        self.root.current_screen.ids["payperiod_list"].clear_widgets()
        listofdicks = self.load_paychecks()
        listofdicks = sorted(listofdicks, key=lambda i: i[ssort], reverse=rreverse)

        bu = ["YTD", "Year", "All", "Custom"]
        bu2 = ["paydate", "moneytotal", "totalhours"]
        for i in range(len(bu)):
            if self.date_range_pp == bu[i]:
                App.get_running_app().root.current_screen.ids[
                    bu[i]
                ].md_bg_color = self.theme_cls.primary_dark
            else:
                App.get_running_app().root.current_screen.ids[
                    bu[i]
                ].md_bg_color = self.theme_cls.primary_light

        for i in range(len(bu2)):
            if ssort == bu2[i]:
                App.get_running_app().root.current_screen.ids[
                    bu2[i]
                ].md_bg_color = self.theme_cls.primary_dark
            else:
                App.get_running_app().root.current_screen.ids[
                    bu2[i]
                ].md_bg_color = self.theme_cls.primary_light
        if rreverse == False:
            App.get_running_app().root.current_screen.ids[
                "sall"
            ].icon = "sort-descending"
        else:
            App.get_running_app().root.current_screen.ids[
                "sall"
            ].icon = "sort-ascending"

        App.get_running_app().root.current_screen.ids["dstart"].text = (
            self.format_date(self.fday, "full") + "     to"
        )

        App.get_running_app().root.current_screen.ids["dend"].text = self.format_date(
            self.lday, "full"
        )
        for z in range(len(listofdicks)):
            # print(listofdicks[z])

            panel = ThreeLineListItem(
                text="Paydate: "
                + str(self.format_date(listofdicks[z]["paydate"], "full")),
                secondary_text="Shows: "
                + str(listofdicks[z]["shows"])
                + " Hours: "
                + str(listofdicks[z]["totalhours"])
                + " Overtime: "
                + str(listofdicks[z]["othours"]),
                tertiary_text="$" + str(listofdicks[z]["moneytotal"]),
                bg_color=self.theme_cls.bg_dark,
                radius=[self.c_radius, self.c_radius, self.c_radius, self.c_radius],
                on_release=self.do_pay_ind,
            )

            self.root.get_screen("pay").ids.payperiod_list.add_widget(panel, z)

    def do_pay_ind(self, b):
        import libs.lib_parse2

        # from kivymd.uix.list import ThreeLineListItem

        # print(dir(FourLineListItem), "testtest")

        print(
            "ind",
            b.text,
        )

        i = str.split(b.text, " ")
        d, m, y = str.split(i[1], "/")
        z = libs.lib_parse2.parsepayperiod(
            d + "-" + m + "-" + y + ".html",
        )
        # print(z, "gigigig")
        # for line in o.readlines():
        #    print(line)
        import os

        print(os.getcwd(), "CWDDDDD")
        os.chdir(cwd)
        print(os.getcwd(), "CWDDDDD")
        self.root.set_current("pay_breakdown")

        panel = ThreeLineListItem(
            text="Paydate: " + str(z["paydate"]),
            secondary_text="Shows: "
            + str(z["days"])
            + " RegHours: "
            + str(z["reghours"])
            + " Overtime: "
            + str(z["othours"]),
            tertiary_text="$" + str(z["grandtotal"]),
            # fourth_text="test",
            bg_color=self.theme_cls.bg_darkest,
            radius=[self.c_radius, self.c_radius, self.c_radius, self.c_radius],
            # on_release=self.do_pay_ind,
        )

        self.root.get_screen("pay_breakdown").ids.pay_gigs.add_widget(panel)

        for i in range(len(z["gigs"])):
            d = z["gigs"][i]
            din, tin = str.split(d["timeIn"], " ")
            junk, monthi, datei = str.split(din, "-")
            h_i, min_i, junk = str.split(tin, ":")

            dout, tout = str.split(d["timeOut"], " ")
            h_o, min_o, junk = str.split(tout, ":")
            junk, montho, dateo = str.split(din, "-")
            time = (
                monthi
                + "-"
                + datei
                + " "
                + h_i
                + ":"
                + min_i
                + " -- "
                + h_o
                + ":"
                + min_o
            )
            hours_nice = "Hours:" + str(d["tot_hours"])
            if float((d["otH"])) > 0:
                hours_nice = hours_nice + " Overtime: " + str(d["otH"])
            panel = ThreeLineListItem(
                secondary_text=time,
                text=d["show"],
                tertiary_text=hours_nice,
                bg_color=self.theme_cls.bg_dark,
                radius=[self.c_radius, self.c_radius, self.c_radius, self.c_radius],
                # on_release=self.do_pay_ind,
            )

            self.root.get_screen("pay_breakdown").ids.pay_gigs.add_widget(panel)

    def do_payperiod2(self, ssort, rreverse):
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
        i = 0
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
        if i > 0:
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
        if i == 0:
            toast("No Paystubs Found")
        # print(moneys, "moneys")

    def do_history(self):

        self.root.set_current("history")
        self.root.current_screen.ids["history_list"].clear_widgets()
        # self.root.current_screen.ids["history_list"].add_widget(HistoryItem(text='bla'))
        import glob, os

        try:
            os.chdir(ad + "/shows")
        except:
            os.mkdir(ad + "/shows")
            os.chdir(ad + "/shows")
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
                    App, file, ad
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

        print("poppy", v)
        if v == "about":
            ttt = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
            if not self.dialog:
                self.dialog = MDDialog(
                    text=ttt,
                    type="custom",
                    # content_cls=Content(),
                    buttons=[],
                )
        if v == "notes":
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
        import libs.lib_enc

        self.root.current = "login"
        x["username"] = App.get_running_app().root.current_screen.ids["temail"].text
        x["usecache"] = False
        x["password"] = str(
            libs.lib_enc.make_password(
                App.get_running_app().root.current_screen.ids["tpassword"].text
            )
        )
        x["city"] = App.get_running_app().root.current_screen.ids["button4"].text
        import libs.lib_updateuserdata as lib_updateuserdata

        lib_updateuserdata.updateuser(x, ad)

    # btnState2 = StringProperty("false")


Demo3App().run()


# Your appId:	d6073280-f7af-4082-8b33-0356d7068f51
# Your appSecret:	073276b2-4940-40f0-87cc-7e4805382cd0
# https://www.highscores.ovh/

##Photo by <a href="https://unsplash.com/@sebastiaanstam?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">sebastiaan stam</a> on <a href="https://unsplash.com/s/photos/concert?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
##Photo by <a href="https://unsplash.com/@fkaregan?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Samuel Regan-Asante</a> on <a href="https://unsplash.com/s/photos/concert?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
##Photo by <a href="https://unsplash.com/@nickleejeffries?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Nicholas Jeffries</a> on <a href="https://unsplash.com/s/photos/concert?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
