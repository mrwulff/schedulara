from tkinter import Menu
from kivy.lang import Builder
from kivy.properties import StringProperty

from kivymd.app import MDApp
from kivymd.uix.card import MDCardSwipe
from kivymd.uix.card import MDCard
from kivymd.uix.behaviors import RoundedRectangularElevationBehavior
from kivy.config import Config
from kivy.core.window import Window
from kivymd.uix.picker import MDThemePicker
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivymd.uix.button import MDRectangleFlatIconButton




w=1125/2
h=2436/2
Config.set('graphics', 'width', str(w))
Config.set('graphics', 'height', str(h))
Window.size = (w,h)






import datetime
import humanize
import create_cache
import libparse
import time


create_cache.createcache('',10)
xxx=libparse.parse('','','')



sm=''






class SwipeToDeleteItem(Screen):
#class SwipeToDeleteItem(MDCardSwipe):

    text = StringProperty()

    
class MainScreen(Screen):
    pass
class SettingsScreen(Screen):
    pass

class TestCard(MDApp):

    


    def click(self,root):


        pass
    def set_screen(self, screen_name):
        #self.root.current = MenuScreen
        print(screen_name)
        MDApp.get_running_app().root.current = "SettingsScreen"
    def show_theme_picker(self):
        theme_dialog = MDThemePicker()
        theme_dialog.open()
    def addAllBack(self):
        #self.screen.ids.llogin.clear_widgets()
        self.make_list()
    def removeAll(self):
        #print (dir(self.screen.ids.md_list))
        self.screen.ids.md_list.clear_widgets()
        
        #addAllBack(self)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title = "My Material Application"
        self.theme_cls.primary_palette = "Green"
        #self.screen = Builder.load_string(KV)

    def build(self):
        screen = Builder.load_file("f.kv")
        #self.screen_manager = screen.ids.screen_manager
        
        
        return screen
        #return self.sm
    def make_list(self):
        odd=0
        now = datetime.datetime.now()
        for i in range(len(xxx)-1):
            past=False
            odd=odd+1
            try:
                dobj = datetime.datetime.strptime(xxx[i][0]+'/'+xxx[i][1], '%m/%d/%Y/%H:%M')
            except:
                print('errrrror:',xxx[i])
            diff=now-dobj
            if now.date()>dobj.date():
                past=True
            diff2=humanize.naturaltime(now - dobj)
            diff2=str(diff2)
            diff=str(diff)
                #if 'irmed' not in mj3[i][10]:
                #    mj3[i][10]='[color=ff0000ff]'+mj3[i][10]+'[/color]'
            fdate=(dobj.strftime("%A"))+', '+(dobj.strftime("%m"))+'/'+(dobj.strftime("%d"))+ ' ' +(dobj.strftime("%I"))+':'+(dobj.strftime("%M"))+'[sup]'+(dobj.strftime("%p"))+'[/sup]'
            #print (fl)
            if now.date()==dobj.date():
                today='[color=#00007fff][b]TODAY[/b][/color]\n'
            else:
                today=''

            texta=today+''+fdate+' \n'+xxx[i][3]+' '+'\n[b]'+xxx[i][4]+'\n[/b][size=16 sp]'+xxx[i][5]+'\n'+xxx[i][8]+' '+xxx[i][7]+' '+xxx[i][10]+'\n'+diff2
            if past==True:
                texta='[size=16 sp]'+fdate+'\n'+xxx[i][3]+'\n'+xxx[i][4]



            
            self.screen.ids.md_list.add_widget(
            SwipeToDeleteItem(text=texta))
            
            




    def update_list(self, instance):
        self.removeAll()

        global xxx
        create_cache.createcache('')
        xxx=libparse.parse('','','')
        self.addAllBack()
        print ('lol')

    def on_swipe_complete(self, instance):
        xx=self.screen.ids.md_list.children.index(instance)
        i= (len(xxx)-xx)-2
        print (i,xxx[i])
        self.screen.ids.md_list.clear_widgets()
        #self.screen.ids.llogin2.clear_widgets()


        #self.root.ids.llogin2.add_widget(MDBoxLayout2())
        
        self.root.ids.llogin2.add_widget(MDCard())
            


    def on_start(self):
        #global sm
        #self.sm = ScreenManager()
        #self.sm.add_widget(Screen1(name = "Screen1"))

        self.make_list()
        print(dir(self.root.ids.llogin),'shit')
        #self.root.ids.llogin.disabled=True
        self.screen.ids.llogin2.clear_widgets()






TestCard().run()