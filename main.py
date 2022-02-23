ios=True
notch=True
debug=True
scale=2
useold=False
import platform
pf= (platform.platform())
if pf[0]=='W':
    scale=1
    notch=False



from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen,ScreenManager
from kivymd.uix.list import MDList, ThreeLineIconListItem,TwoLineIconListItem,IconLeftWidget
from kivy.properties import StringProperty
from kivy.properties import ObjectProperty
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.list import IRightBodyTouch
from kivymd.uix.boxlayout import MDBoxLayout
#from kivymd.uix.Floatlayout import MDFloatLayout
from kivymd.uix.snackbar import Snackbar

import pyperclip


from kivymd.uix.button import MDFlatButton
from kivymd.uix.button import MDRectangleFlatIconButton
from datetime import datetime
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.core.clipboard import ClipboardBase

#from kivycupertino.uix.slider import CupertinoSlider



from kivy.uix.textinput import TextInput

import json
from appdirs import *
import ssl
import logging

ssl.verify = False




from kivy.uix.spinner import Spinner, SpinnerOption
from kivy.uix.dropdown import DropDown
import webcolors

from kivy.utils import platform
from kivy.app import App


from kivy.config import Config
from kivy.core.window import Window
from kivymd.uix.picker import MDThemePicker
from kivymd.uix.picker import MDTimePicker
from kivymd.uix.picker import MDDatePicker
from kivymd.uix.dialog import MDDialog
from math import sin
from kivy_garden.graph import Graph, MeshLinePlot,LinePlot
from kivy.properties import NumericProperty
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.button import MDFlatButton
from kivymd.uix.behaviors.toggle_behavior import MDToggleButton




import os
#if platform=='ios':
if 1==1:
    w=1125/3
    h=2436/3
    Config.set('graphics', 'width', str(w))
    Config.set('graphics', 'height', str(h))
    Window.size = (w,h)
    HOME = os.environ.get("HOME", "/")
    BUNDLE = os.environ.get("KIVY_BUNDLE_ID", "/")
    os.environ["PYTHON_EGG_CACHE"] = f"{HOME}/Library/Caches/{BUNDLE}"
config_file=(f"{HOME}/Library/Caches/{BUNDLE}")
print (config_file,'THIS IS THE CONFIG FILE',platform)

#if platform=='win':
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







class SpinnerOptions(SpinnerOption):

    def __init__(self, **kwargs):
        super(SpinnerOptions, self).__init__(**kwargs)
        self.background_normal = ''
        self.background_color = [0, 0, 1, 1]    # blue colour

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

class InfoScreen(Screen):



    pass
class NotificationScreen(Screen):
    pass
class PayScreen(Screen):
    pass
class SettingsScreen(Screen):
    global x
    #app = App.get_running_app()
    #ad=app.user_data_dir
    #x=lib_readuserdata.readuserdata(App)
    
    btnState2 = StringProperty("false")
    #btnState = 'down'
    #btnState2 = 'true'



class YourContainer(IRightBodyTouch, MDBoxLayout):
    adaptive_width = True
class YourContainer2(IRightBodyTouch, MDBoxLayout):
    adaptive_width = False
    size_hint=(.9,.9)
class HistoryItem(Screen):
    text = StringProperty()
class PayItem(Screen):
    text = StringProperty()

class NewSlider(Screen):
    text= StringProperty()










class SwipeToDeleteItem(Screen):
    #def on_touch_down(self, touch):
        #pass
#class SwipeToDeleteItem(MDCardSwipe):

    text = StringProperty()
    

    def click(self,*args):
        global idex

        idex= (self.ids.idmdlabel.text)

        
        try:
            junk,idex=str.split(idex,'***')
            idex=int(idex)
            newxxx= (xxx[idex])
        except:
            ''
            newxxx=[]
        try:
            rate=lib_extractjson.extract_pos(App,config_file,xxx[idex][8])
            App.get_running_app().root.current_screen.ids['rate'].text=rate
        except:
            App.get_running_app().root.current_screen.ids['rate'].text="?"
        now = datetime.datetime.now()
        today,fdate=lib_tinyfs.format_text(idex,mjds,now,'info')
        try:
            App.get_running_app().root.current_screen.ids['date'].text=fdate
            #App.get_running_app().root.current_screen.ids['d0'].text=str(newxxx[0])
            #App.get_running_app().root.current_screen.ids['d1'].text=str(newxxx[1])
            App.get_running_app().root.current_screen.ids['jobid'].text=str(newxxx[2])
            App.get_running_app().root.current_screen.ids['show'].text=str(newxxx[3])
            App.get_running_app().root.current_screen.ids['venue'].text=str(newxxx[4])
            App.get_running_app().root.current_screen.ids['location'].text=str(newxxx[5])
            App.get_running_app().root.current_screen.ids['client'].text=str(newxxx[6])
            App.get_running_app().root.current_screen.ids['type'].text=str(newxxx[7])
            App.get_running_app().root.current_screen.ids['wrench'].text=str(newxxx[8])
            App.get_running_app().root.current_screen.ids['status'].text=str(newxxx[10])
            App.get_running_app().root.current_screen.ids['notes'].text=str(newxxx[11])
            App.get_running_app().root.current_screen.ids['d12'].text=str(newxxx[12])
            App.get_running_app().root.current_screen.ids['d13'].text=str(newxxx[9])
            App.get_running_app().root.current_screen.ids['d10'].text=str(newxxx[13])

        except:
            (newxxx)
        if newxxx[8]=='ME':
            App.get_running_app().root.current_screen.ids['pos'].icon='power-socket-us'
class ContentNavigationDrawer(Screen):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()
class P(FloatLayout):
    

    pass
class Prestore(FloatLayout):
    

    pass
from kivymd.uix.button import MDRaisedButton

class MyToggleButton(MDRaisedButton, MDToggleButton):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_down = self.theme_cls.primary_light


newcolor=(.2,.2,.2)
x=''
ad=''
xxx=''
idex=1
browser=''
class Demo3App(MDApp):
    #def __init__(self, **kwargs):
    #    self.snackbar = None
    global idex
    iii=idex
    bud2='65'
    global x
    x=x
    





    
    locations=['denver', 'dc', 'florida' ,'georgia' , 'indiana' ,'kentucky' , 'lasvegas' ,'losangeles' , 'louisiana' , 'michigan' , 'minnesota' , 'missouri' , 'mississippi' , 'montana' ,'newmexico' , 'northerncalifornia'  ,'northwest' ,'ohio' , 'reno' , 'california' , 'southcarolina' ,'tempe' , 'memphis' , 'texas' , 'tucson' ,'wisconsin'  ]
    newercolor=newcolor
    xxxx=xxx+'wtf'+str(idex)
    lunch=['0','1','2']
    if notch==True:
        mheight=120
    else:
        mheight=45
    cpadding=20
    cspacing=10
    mtype='top'
    bradius=20
    radius=25
    mfontel='fonts/SourceSansPro-ExtraLight.ttf'
    mfontb='fonts/SourceSansPro-Bold.ttf'
    mfont='fonts/SourceSansPro-Regular.ttf'
    dialog = None
    snackbar = None
    rreverse=True
    menurotate=10
    menuscale=.5,.5
    notheight=400
    pf= (platform.platform())
        if pf[0]=='W':
            notheight=400
    #zoom = NumericProperty(1)
    def format_minutes(self,t,v,d):
        #v=5
        if d==True:
            return(t+' Notification will be sent '+ str(v) +' minutes before call')
        if d==False:
            return(t+' Notification disabled')


    def enable_nots(self):
        global x
        self.root.current = "settings"
        tog1=(App.get_running_app().root.current_screen.ids['switchnotify'].active)
        print (tog1,x)
        x['not']=tog1
        lib_updateuserdata.updateuser(x,ad)
        

    
    def do_settings(self):
        global x
        print (x)
        self.root.current = "settings"
        try:
            self.root.get_screen("notification").ids['slider2'].value=x['not2time']
            self.root.get_screen("notification").ids['slider1'].value=x['not1time']
            
            self.root.get_screen("notification").ids['disable1'].active=x['not1']
            self.root.get_screen("notification").ids['disable2'].active=x['not2']
        
            if x['not']==True:
                App.get_running_app().root.current_screen.ids['switchnotify'].active=True

        
            tog1=(App.get_running_app().root.current_screen.ids['switchnotify'].active)
        except:
            x['not2time']=0
            x['not1time']=0
            x['not1']=False
            x['not2']=False
            x['not']=False
        #print (tog1)
        
        
        
        
        
        lib_updateuserdata.updateuser(x,ad)


    def loadnots(self,sslider):
        global x

        self.root.current = "notification"

        if x['not1']==True:
            App.get_running_app().root.current_screen.ids['disable1'].active=True

        if x['not2']==True:
            App.get_running_app().root.current_screen.ids['disable2'].active=True
        App.get_running_app().root.current_screen.ids['slider2'].value=x['not2time']
        try:
            App.get_running_app().root.current_screen.ids['slider2'].value=x['not2time']
            App.get_running_app().root.current_screen.ids['slider1'].value=x['not1time']
        except:
            print ('rip')
        lib_updateuserdata.updateuser(x,ad)
            
    def makenots(self,sslider):
        global x
        self.root.current = "notification"

        first=str(App.get_running_app().root.current_screen.ids['slider'+sslider].value)
        #App.get_running_app().root.current_screen.ids['text'+sslider].text=first


        text1=str(App.get_running_app().root.current_screen.ids['slider1'].value)
        text2=str(App.get_running_app().root.current_screen.ids['slider2'].value)
        tog1=(App.get_running_app().root.current_screen.ids['disable1'].active)
        tog2=(App.get_running_app().root.current_screen.ids['disable2'].active)

        
        x['not1']=tog1
        x['not1time']=text1

        x['not2']=tog2
        x['not2time']=text2
        print (text1,text2,tog1,tog2,x)
        lib_updateuserdata.updateuser(x,ad)

        
    def trophys(self):
        import lib_test
        lib_test.n22()
    def make_stats(self):
        self.root.current = "stats"
        self.root.current_screen.ids["graphs"].clear_widgets()
        dd,dd2,maxd,maxm,max_dy,max_my=lib_makegraphs.parsepp(self,ad,'check')
        print (dd[1])
        lib_makegraphs.make_stats_pp(self,'Checks',dd,maxm,max_dy)

        print (dd[1])

        lib_makegraphs.make_stats_pp(self,'$/Day',dd2,maxd,max_dy)



    
    def maketransp(self):

        x=(self.theme_cls.primary_color)
        x[3]=.3
        return x

    def menuu(self):
        self.do_login('',False)
        
    def mainmenuf(self):
        self.root.current = "mainmenu"
        #self.root.current_screen.ids["payperiod_list"].clear_widgets()
        
    def dlpp(self):
        lib_ppdownloader.thinkpp(x,ad)
    def ccc(self):
        print (xxx)
        confable=[]
        for i in range(len(xxx)):

            try:
                z=xxx[i][13]
                z.append(confable)
            except:
                pass
        for i in range(len(confable)):
            print (confable[i])
        self.snackbar = Snackbar(text='Success!',bg_color=self.theme_cls.primary_color)
        self.snackbar.open()

    
    def confirm(self,what):
        fail=self.confirm_real(what)
        old=False
        if fail !='fail':
            nf2=ad+'/realdata.html'
            try:
                with open(nf2,mode='r') as f:
                    for line in f.readlines():
                        #print (line)
                        
                        if "javascript'>alert" in line:
                            old=True
                            l,x=str.split(line,'(')
                            x,l=str.split(x,')')
                            print (x)
            except:
                self.snackbar = Snackbar(text='Not Logged In',bg_color=self.theme_cls.primary_color)
                self.snackbar.open()
                        #if not self.snackbar: 
        if old==True:
            self.snackbar = Snackbar(text=x,bg_color=self.theme_cls.primary_color)
            self.snackbar.open()
        if fail =='fail':
            self.snackbar = Snackbar(text='Already confirmed you dum dum',bg_color=self.theme_cls.primary_color)
            self.snackbar.open()
        if old==False and fail !='fail':
            self.snackbar = Snackbar(text='Success!',bg_color=self.theme_cls.primary_color)
            self.snackbar.open()


    def confirm_real(self,what):
        global browser
        #print (what)
        print (len(xxx[idex]))
        try:
            print (xxx[idex][13])
        except:
            print ('nonconfirm')
            return ('fail')
        
        
        print (type(browser))
        try:
            if 1==1:
                try:
                    browser.select_form(name="ctl00")
                    print ("USED OLD BROWSER")
                except:
                    browser=lib_think.openbrowser(ad,x,ios,App)
                    browser.select_form(name="ctl00")
                    print ("USED NEW BROWSER")

                #print(browser, 'browser 1')
                control_t = browser.form.find_control("__EVENTTARGET")
                control_a = browser.form.find_control("__EVENTARGUMENT")
                #print(browser, 'browser 2')
                control_t.readonly = False
                control_a.readonly = False

                control_t.value = str(xxx[idex][13])
                control_a.value = 'Confirm'
                #print(browser, 'browser 3')

                response = browser.submit()
                #print(browser, 'browser 4')
                aa = response.get_data()
                #print(browser, 'browser 5')

                aaa = open(ad+'/realdata.html', 'wb')
                aaa.write((aa))
                aaa.close()
        except:
            ''
        
                
    def closeDialog(self, inst):
        self.dialog.dismiss()
    def delete_shows(self,what):
        #print (what)
        from os import walk

        filenames = next(walk(ad+'/shows'), (None, None, []))[2]  # [] if no file
        print (filenames)
        for i in range(len(filenames)):
            os.remove(ad+'/shows/'+filenames[i])

    def show_delete_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                text="Discard draft?",
                buttons=[
                    MDFlatButton(
                        text="CANCEL",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_press=self.closeDialog
                        
                    ),
                    MDFlatButton(
                        text="DELETE",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_press=self.delete_shows
                    ),
                ],
            )
        self.dialog.open()

    def backup(self):
        nf=(os.path.join(ad,'shows2.zip'))
        #nf='C:/Users/kw/AppData/Roaming/demo3/shows2.zip'
        try:
            shutil.make_archive(ad+'/show2', 'zip', ad+'/shows')

            nfc=ad
            nf2=(os.path.join(nfc,'show2.zip'))
            with open(nf2,mode='rb') as f:
                f=f.read()
                print (type(f),'typef')
                f=str(f)
            #print (f)
            return f
        except:
            self.snackbar = Snackbar(text='Make some show files first',bg_color=self.theme_cls.primary_color)
            self.snackbar.open()
            return ''

    def restorebin(self,x):
        try:
            print (x)
            nf2=(os.path.join(ad,'show3.zip'))
            #j,x,j=str.split(x,'"')
            #print (x)
            #x=x.encode()
            #print (bytes(x,'utf-8'))
            x=eval(x)
     
            
            with open(nf2,mode='wb') as f:
                f.write(x)
            shutil.unpack_archive(nf2, ad+'/shows')
        except:
            self.snackbar = Snackbar(text='Not Valid Backup Data',bg_color=self.theme_cls.primary_color)
            self.snackbar.open()

    def search_menu(self):
        #scale=2
        show = P() # Create a new instance of the P class 

        popupWindow = Popup(title="", content=show, size_hint=(None,None),size=(400*scale,600*scale),separator_height=0,title_size=0,background_color=(self.theme_cls.primary_dark))
    # Create the popup window

        popupWindow.open() # show the popup
    def search(self,x):
        #term=App.get_running_app().root.current_screen.ids['search'].text
        print (x.text)
        self.do_login(x.text,True)
        #root.dismiss()
    def set_caption(self, popup):
        self.button.text = popup.content.text
    
    def get_rate(self):
        try:
            print (xxx[idex],'get_rate')
            pos= (xxx[idex][8])
            rate=extract_pos(App,config_file,pos)
            App.get_running_app().root.current_screen.ids['rate'].text=str(rate)
        except:
            print (xxx,'get_rate23')
    
    def set_rate(self):
        x= (xxx[idex][8])
        #rate=str(28.5)
        rate=App.get_running_app().root.current_screen.ids['rate'].text
        lib_makeuserdata.makeposfile(App,x,config_file,ios,rate)

        
    def get_date(self, date):
        '''
        :type date: <class 'datetime.date'>
        '''
        #return date
        pass
    def set_pp(self,current):
        App.get_running_app().root.current_screen.ids['scustom'].md_bg_color= self.theme_cls.primary_light
        if current=='current':
            App.get_running_app().root.current_screen.ids['scustom'].md_bg_color= self.theme_cls.primary_light
            App.get_running_app().root.current_screen.ids['scurrent'].md_bg_color= self.theme_cls.primary_dark
            App.get_running_app().root.current_screen.ids['slast'].md_bg_color= self.theme_cls.primary_light
            App.get_running_app().root.current_screen.ids['sall'].md_bg_color= self.theme_cls.primary_light

        if current=='last':
            App.get_running_app().root.current_screen.ids['scustom'].md_bg_color= self.theme_cls.primary_light
            App.get_running_app().root.current_screen.ids['scurrent'].md_bg_color= self.theme_cls.primary_light
            App.get_running_app().root.current_screen.ids['slast'].md_bg_color= self.theme_cls.primary_dark
            App.get_running_app().root.current_screen.ids['sall'].md_bg_color= self.theme_cls.primary_light
        if current=='custom':
            App.get_running_app().root.current_screen.ids['scustom'].md_bg_color= self.theme_cls.primary_dark
            App.get_running_app().root.current_screen.ids['scurrent'].md_bg_color= self.theme_cls.primary_light
            App.get_running_app().root.current_screen.ids['slast'].md_bg_color= self.theme_cls.primary_light
            App.get_running_app().root.current_screen.ids['sall'].md_bg_color= self.theme_cls.primary_light
        if current=='all':
            App.get_running_app().root.current_screen.ids['scustom'].md_bg_color= self.theme_cls.primary_light
            App.get_running_app().root.current_screen.ids['scurrent'].md_bg_color= self.theme_cls.primary_light
            App.get_running_app().root.current_screen.ids['slast'].md_bg_color= self.theme_cls.primary_light
            App.get_running_app().root.current_screen.ids['sall'].md_bg_color= self.theme_cls.primary_dark
            App.get_running_app().root.current_screen.ids['dend'].text=str('All')
            App.get_running_app().root.current_screen.ids['dstart'].text=str('All')
        flag=False
        firstdate=datetime.date(2021, 10, 13)
        #:
        now = datetime.datetime.now()
        now=datetime.date.today()
        while flag==False:
            
            nextdate=firstdate+datetime.timedelta(days=14)
            lastdate=nextdate+datetime.timedelta(days=13)
            if nextdate <= now <= lastdate:
                flag=True
                if current=='current':
                    App.get_running_app().root.current_screen.ids['dstart'].text=str(nextdate)
                    App.get_running_app().root.current_screen.ids['dend'].text=str(lastdate)
                if current=='last':
                    App.get_running_app().root.current_screen.ids['dstart'].text=str(nextdate-datetime.timedelta(days=14))
                    App.get_running_app().root.current_screen.ids['dend'].text=str(lastdate-datetime.timedelta(days=14))
            firstdate=nextdate
        if current !='custom':
            self.do_history()
            
    def show_date_picker(self): 
        date_dialog = MDDatePicker(mode="range")
        date_dialog.bind(on_save=self.on_save, on_cancel=self.on_cancel)
        date_dialog.open()
        #App.get_running_app().root.current_screen.ids['send'].md_bg_color= self.theme_cls.primary_light
        #App.get_running_app().root.current_screen.ids['sstart'].md_bg_color= self.theme_cls.primary_light
        #App.get_running_app().root.current_screen.ids['scustom'].md_bg_color= self.theme_cls.primary_dark
    def on_cancel(self, instance, value):
		#self.root.ids.date_label.text = "You Clicked Cancel"
        pass
    def on_save(self, instance, value, date_range):
		#self.root.ids.date_label.text = str(value)
		#self.root.ids.date_label.text = f'{str(date_range[0])} - {str(date_range[-1])}'
        try:
            App.get_running_app().root.current_screen.ids['dstart'].text=str(date_range[0])
            App.get_running_app().root.current_screen.ids['dend'].text=str(date_range[-1])
        except:
            App.get_running_app().root.current_screen.ids['dstart'].text=str('')
            App.get_running_app().root.current_screen.ids['dend'].text=str('')
        self.do_history()

    def check_att(self,b):


        #app = App.get_running_app()
        #ad=app.user_data_dir
        #config_file=ad

        if ios==True:
        
            x=lib_readuserdata.readuserdata(App,ad,ios)
        return x[b]
    def updatetext(self):
        app = App.get_running_app()
        ad=app.user_data_dir
        print (ad)
        if ios==False:
            config_file=ad
        debugbox=App.get_running_app().root.current_screen.ids['usecachebox'].active
        x['usecache']=debugbox
        lib_updateuserdata.updateuser(x,ad)

    def maps(self,):
        bbb=App.get_running_app().root.current_screen.ids['venue'].text
        webbrowser.open("https://www.google.com/maps/search/"+bbb)
    def save(show):
        pass
    def format_textt(self,name):
        name=str.replace(name,'/','')
        name=str.replace(name,':','')
        return name
    def show_time_picker2(self):
        lib_makeuserdata.makeshowfile(App,xxx[idex],config_file,ios)
        



    def show_time_picker1(self):
        #if App.get_running_app().root.current_screen.ids['newhours'].text=='Set Worked Hours':
        if 1==1:
            y=time_dialog1 = MDTimePicker()
            x=time_dialog1.bind(time=self.get_time)
            z=time_dialog1.open()
        


    def get_time(self, instance, time):

        App.get_running_app().root.current_screen.ids['newhours'].text=str(time)
        return time
    def make_info(self,thing):

        return thing

    def on_checkbox_active(self, checkbox, value):
        global x
        if value:
            print('The checkbox', checkbox, 'is active', 'and', checkbox.state, 'state')
            x['usecache']='True'
        else:
            print('The checkbox', checkbox, 'is inactive', 'and', checkbox.state, 'state')
            x['usecache']='False'
        btnState2 = StringProperty("false")
        lib_updateuserdata.updateuser(x,ad)





    def on_start(self):
        global x
        global ad
        app = App.get_running_app()
        ad=app.user_data_dir
        if ios==True:
            config_file=ad

        try:
            x=lib_readuserdata.readuserdata(App,config_file,ios)
        except:
            print ('failed to read user data, making shit up now')
            lib_makeuserdata.makeuserdata(App,config_file,ios)
            x=lib_readuserdata.readuserdata(App,config_file,ios)
            print (x,'readuserdata after creating it',type(x),x["username"])
        self.do_login('',False)
        #self.search_menu = SearchPopupMenu()
        #self.root.ids.usecache.state='down'
        
    def lol(self):
        #x=lib_readuserdata.readuserdata(App,config_file)
        #xx=(x['usecache'])
        #if xx=="True":
        #    xx='Using Cache'
        #if xx=="False":
        #    xx='Using Real Data'
        
        #return str(xx)
        pass

    def removeAll(self):
        self.root.current_screen.ids["users_lst"].clear_widgets()
    def show_theme_picker(self):
        theme_dialog = MDThemePicker()
        theme_dialog.open()
    def save_theme_picker(self):
        s=self.theme_cls.theme_style
        p=self.theme_cls.primary_palette
        a=self.theme_cls.accent_palette 
        x=lib_readuserdata.readuserdata(App,config_file,ios)
        print (s,p,a,x)
        x['pcolor']=p
        x['scolor']=a
        x['theme']=s
        print (s,p,a,x)
        lib_updateuserdata.updateuser(x,ad)
        

    def change_screen(self, screen, direction):
        self.root.transition.direction = direction
        self.root.current = screen
    def build(self):



        self.button = Button(text="Click",
                             on_release=self.search_menu)

        global newcolor
        try:
            x=lib_readuserdata.readuserdata(App,config_file,ios)
        except:
            lib_makeuserdata.makeuserdata(App,config_file,ios)
            x=lib_readuserdata.readuserdata(App,config_file,ios)
        try:
            self.theme_cls.theme_style=x['theme']
            self.theme_cls.primary_palette = x['pcolor']
            self.theme_cls.accent_palette = x['scolor']
        except:
            ''
        
        self.sm=ScreenManager()
        self.sm.add_widget(InfoScreen(name="info"))
        self.sm.add_widget(SettingsScreen(name="settings"))
        self.sm.add_widget(HomeScreen(name="home"))
        self.sm.add_widget(LoginScreen(name="login"))
        self.sm.add_widget(HistoryScreen(name="history"))
        self.sm.add_widget(PayScreen(name="Pay"))
        self.sm.add_widget(MainMenuScreen(name="mainmenu"))
        self.sm.add_widget(AboutScreen(name="about"))
        self.sm.add_widget(TrophyScreen(name="trophy"))
        self.sm.add_widget(StatsScreen(name="stats"))
        self.sm.add_widget(NotificationScreen(name="notification"))
        
        #newcolor=webcolors.name_to_rgb(self.theme_cls.accent_palette)
        
        

        screen=Builder.load_file("demo.kv")
        #site = server.Site(Simple())

        #reactor.listenTCP(8080, site)

      
        
        return screen
    def do_payperiod(self,ssort,rreverse):
        self.root.current = "Pay"
        self.root.current_screen.ids["payperiod_list"].clear_widgets()
        #self.root.current_screen.ids["payperiod_list"].add_widget(HistoryItem(text='bla1'))
        import glob, os
        try:
            os.chdir(config_file+'/pp')
        except:
            os.mkdir(config_file+'/pp')
            os.chdir(config_file+'/pp')
        x=0
        listofdicks=[]
        for file in glob.glob("*.html"):
            #print (file)
            dd,junk=lib_parse.parsepayperiod(config_file+'/pp/'+file)
            listofdicks.append(dd)
            x=x+1
            #self.root.current_screen.ids["payperiod_list"].add_widget(HistoryItem(text=str(dd)+'[size='+str(x)))
            #if x<5:
            #    self.root.current_screen.ids["payperiod_list"].add_widget(HistoryItem(text=str(dd['dtext'])+'[size=0]'+str(x)))
        #listofdicks.sort()
        #listofdicks= (sorted(listofdicks, key = lambda i: i['paydate'],reverse=True))
        #listofdicks= (sorted(listofdicks, key = lambda i: i['shows'],reverse=True))
        #listofdicks= (sorted(listofdicks, key = lambda i: i['moneytotal'],reverse=rrverse))
        listofdicks= (sorted(listofdicks, key = lambda i: i[ssort],reverse=rreverse))

        for i in range(len(listofdicks)):
            
            #print (listofdicks[i])
            self.root.current_screen.ids["payperiod_list"].add_widget(HistoryItem(text=str(listofdicks[i]['dtext'])+'[size=0]'+str(i)))
        
            

        xy='Found '+str(x)+' PayStubs '
        try:
            self.root.current_screen.ids["payperiod_list"].add_widget(HistoryItem(text=xy+'[size=0]'+str(i+1)))
        except:
            self.root.current_screen.ids["payperiod_list"].add_widget(HistoryItem(text='No Pay Stubs found!'+'[size=0]'+str(1)))
            
        
    def do_history(self):
        
        
        self.root.current = "history"
        self.root.current_screen.ids["history_list"].clear_widgets()
        #self.root.current_screen.ids["history_list"].add_widget(HistoryItem(text='bla'))
        import glob, os
        try:
            os.chdir(config_file+'/shows')
        except:
            os.mkdir(config_file+'/shows')
            os.chdir(config_file+'/shows')
        x=0

        for file in glob.glob("*.json"):
            x=x+1
        x='Found '+str(x)+' Shows '
        #self.root.current_screen.ids["history_list"].add_widget(HistoryItem(text=str(x))+'0')
        allshows=[]
        #allshows.sort()
        hours=0
        ot=0
        pay=0
        tot=0
        now = datetime.datetime.now()
        for file in glob.glob("*.json"):
            data,pay2,ot2,hours2,tot2,date=lib_extractjson.extract_show(App,file,config_file)
            
            show_date = datetime.datetime.strptime(date,"%m/%d/%Y")
            dstart=App.get_running_app().root.current_screen.ids['dstart'].text
            dend=App.get_running_app().root.current_screen.ids['dend'].text
            print (show_date.date(),dstart,dend)
            print (type(show_date.date()),type(dstart),type(dend))
            force=False
            if dstart=='All':

                dstart = datetime.datetime.strptime('1900',"%Y")
                dend = datetime.datetime.strptime('2200',"%Y")
                force=True
            else:
            #dstart != 'All':
                print (dstart,dend,'WF')
                dstart = datetime.datetime.strptime(dstart,"%Y-%m-%d")
                dend = datetime.datetime.strptime(dend,"%Y-%m-%d")
                print (type(show_date.date()),type(dstart.date()),type(dend.date()))
            if dstart.date()<=show_date.date()<=dend.date() :


                allshows.append(data)
                pay=pay+pay2
                ot=ot+ot2
                hours=hours+hours2
                tot=tot+tot2
        self.root.current_screen.ids["history_list"].add_widget(HistoryItem(text='pay='+str(pay)+'\nhours='+str(hours)+'\not='+str(ot)+'\nTotal Hours='+str(tot)+'\nTotal Shows='+str(len(allshows))+'[size=1 sp]***1'))
        s=allshows
        s=allshows.sort(reverse=True)

        for i in range(len(allshows)):
            t=allshows[i]+'[size=1 sp]***'+str(i)
            self.root.current_screen.ids["history_list"].add_widget(HistoryItem(text=t))
    def check_pull_refresh(self, view,user_list):
        max_pixel = 200
        
        to_relative = max_pixel / ( view.height)
        if view.scroll_y < 1.0 + to_relative or self.refreshing:
            return

        self.refresh_data()
    def refresh_data(self): 
        print ('lol')
    #def check_login(self):
        #good_login=self.do_login('',False)
        #if good_login==True:
            #self.save_login()
            #self.root.current = "home"
            
    def save_login(self):
        self.root.current = "login"
        x['username']=App.get_running_app().root.current_screen.ids['temail'].text
        x['password']=App.get_running_app().root.current_screen.ids['tpassword'].text
        x['city']=App.get_running_app().root.current_screen.ids['tloc'].text
        lib_updateuserdata.updateuser(x,ad)
    def do_login(self,search,useold):
        print ('do_login')

        #if pf[0]!='W':
        #if 1==1:
            #from lib_test import n22
            #n22()
        
        


        global xxx
        global mjds
        global config_file
        good_login=False
        now = datetime.datetime.now()
        app = App.get_running_app()
        config_file=app.user_data_dir

    

        self.root.current = "home"
        self.root.current_screen.ids["users_lst"].clear_widgets()

        
        if x['usecache']=="True" or x['usecache']==True :
            print('Using Cache2')
            lib_createcache.createcache(ad,20)
        sch=(ad+'/conf.html')
        
        if x['usecache']=="False" or x['usecache']==False:
            print ("Using Live Data")
            if useold==False:
                good_login=lib_think.login(ad,x,ios,App)
                good_login=True
                pass
                if good_login==True:
                    sch=(ad+'/realdata.html')
        
        
        xxx,mjds=lib_parse.parse(sch,ad,x['usecache'],x)
        
        
        
        
        
        cf,week,tot=lib_tinyfs.stats(xxx,now,search)
        founddates=''
        if len(search)>0:
            founddates=str(tot)+'/'+str(len(xxx)-1)+'dates matching: '+str(search)+'\n'

        texta='[size=18 sp]'+founddates+str(cf)+'/'+str(tot)+' confirmed dates\n'+str(week)+' gigs this week[size=1 sp]***0'
        


        self.root.current_screen.ids["users_lst"].add_widget(SwipeToDeleteItem(text=texta))
        if cf<tot:
            texta='Click To Confirm'+str(tot-cf)+' gigs [size=1 sp]***1'
            self.root.current_screen.ids["users_lst"].add_widget(SwipeToDeleteItem(text=texta))
        #App.get_running_app().root.current_screen.ids['istoday'].text='wow'
        
        
        for i in range(len(mjds)):
            #lib_bonus.create_notification(mjds[i],x)
            texta=lib_tinyfs.format_text(i,mjds,now,'index')
            if search.lower() in str(xxx[i]).lower() or len(search)==0:
                self.root.current_screen.ids["users_lst"].add_widget(SwipeToDeleteItem(text=texta))
        return good_login
                
        
    #btnState2 = StringProperty("false")
Demo3App().run()


