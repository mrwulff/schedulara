from kivy.lang import Builder
from kivy.properties import ObjectProperty

from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout

import datetime
import humanize

import create_cache
import libparse

create_cache.createcache('')
xxx=libparse.parse('','','')


KV = '''
<ContentNavigationDrawer>

    ScrollView:

        MDList:

            OneLineListItem:
                text: "Screen 1"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "scr 1"

            OneLineListItem:
                text: "Screen 2"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "scr 2"


MDScreen:

    MDToolbar:
        id: toolbar
        pos_hint: {"top": 1}
        elevation: 10
        title: "MDNavigationDrawer"
        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]

    MDNavigationLayout:
        x: toolbar.height

        ScreenManager:
            id: screen_manager

            MDScreen:
                name: "scr 1"

                MDLabel:
                    text: "Screen 1"
                    halign: "center"

            MDScreen:
                name: "scr 2"

                MDLabel:
                    text: "Screen 2"
                    halign: "center"

        MDNavigationDrawer:
            id: nav_drawer

            ContentNavigationDrawer:
                screen_manager: screen_manager
                nav_drawer: nav_drawer
'''


class ContentNavigationDrawer(MDBoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class TestNavigationDrawer(MDApp):
    def __init__(self, **kwargs):
        #super().__init__(**kwargs)
        self.screen = Builder.load_string(KV)
    
    #def build(self):
    #    return Builder.load_string(KV)
    def on_start(self):
        print('start')
        self.make_list()


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




TestNavigationDrawer().run()