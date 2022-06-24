from pyobjus import *
from pyobjus.dylib_manager import *
from objc_util import *

"""
def al2():

    from pyobjus import autoclass


    Bridge = autoclass('bridge')
    br = Bridge.alloc().init()
    br.motionManager.setAccelerometerUpdateInterval_(0.1)
    br.startAccelerometer()

    for i in range(10000):
        print ('x: {0} y: {1} z: {2}'.format(br.ac_x, br.ac_y, br.ac_z))

def n23():
    from kivy.app import App
    from kivy.clock import Clock
    from kivy.utils import platform

    if platform == 'ios':
        from pyobjus import autoclass, objc_dict



        onesignal_object = autoclass("OneSignal")
        mock_launch_options = objc_dict({})
        onesignal_object.initWithLaunchOptions_(mock_launch_options, "f440b374-4f65-4709-8b32-52f51e859191")
        onesignal_object.setAppId_("f440b374-4f65-4709-8b32-52f51e859191")
        onesignal_object.promptForPushNotificationsWithUserResponse_("f440b374-4f65-4709-8b32-52f51e859191")
        
        print (dir(onesignal_object),'onesignal...')
        



        #initWithLaunchOptions

def n2_old():
    #get notification popup!
    from plyer.facades import Notification
    from pyobjus import autoclass
    from pyobjus.dylib_manager import load_framework, INCLUDE
    
    load_framework(INCLUDE.Foundation)
    # load_framework('/System/Library/Frameworks/Foundation.framework')
    
    UILocalNotification = autoclass('UILocalNotification')
    UIUserNotificationSettings = autoclass('UIUserNotificationSettings')
    UIApplication = autoclass('UIApplication')
    NSDate = autoclass('NSDate')
    
    NSTimeZone = autoclass('NSTimeZone')
    UIDevice = autoclass('UIDevice')
    UIAlertView = autoclass('UIAlertView')
    
    NSString = autoclass('NSString')
    UIAlertController = autoclass('UIAlertController')
    UIAlertAction = autoclass('UIAlertAction')



    local_noti = UILocalNotification.alloc().init()

    local_noti.fireDate = NSDate.date().dateByAddingTimeInterval_(5)
    local_noti.alertBody = 'message'
    local_noti.alertTitle = 'title'
    #local_noti.alertAction = ns("Slide to unlock")
    # local_noti.timeZone = "GMT+5"
    local_noti.applicationIconBadgeNumber = 10

    settings = UIUserNotificationSettings.settingsForUserNotificationTypes_userNotificationActionSettings_(0 | 1 << 0 | 1 << 1 | 1 << 2,None)
    UIApplication.sharedApplication().registerUserNotificationSettings_(settings)
    UIApplication.sharedApplication().registerForRemoteNotifications(settings)
    UIApplication.sharedApplication().presentLocalNotificationNow_(local_noti)
    #return UIApplication.sharedApplication().scheduleLocalNotification_(local_noti)
def n2shit():
    from plyer import notification
    notification.notify(title='Title',message='Message')
    pass
"""


def n22junk():
    # from plyer.facades import Notification

    # from plyer import uniqueid

    # import random, string
    from pyobjus import autoclass

    load_framework(INCLUDE.Foundation)
    load_framework("/System/Library/Frameworks/UserNotifications.framework")

    UNMutableNotificationContent = autoclass("UNMutableNotificationContent")
    UNNotificationRequest = autoclass("UNNotificationRequest")
    UNTimeIntervalNotificationTrigger = autoclass("UNTimeIntervalNotificationTrigger")
    UNUserNotificationCenter = autoclass("UNUserNotificationCenter")
    NSString = autoclass("NSString")

    # oad_dylib('UniBlocks.dylib')
    # load_dylib('./Blocks_ios.dylib')


def openlinks():
    import ios

    url = "comgooglecalendar://"
    url = "http://www.google.com/calendar/event?action=TEMPLATE&dates=20220201T010000Z%2F20220202T010000Z&text=asdf&location=&details="

    url = "comgooglecalendar://www.google.com/calendar/event?action=TEMPLATE&dates=20220201T010000Z%2F20220202T010000Z&text=asdf&location=&details="
    ios.open_url(url)


def n22():

    import notification_old

    notification_old.schedule(
        "NOW",
        delay=15,
        title="this is a titls",
    )
    x = notification_old.get_scheduled()
    print(x, "omggggg")


def testnot2():
    import notification_old as notification2

    # import notification
    # xx=notification2.authorize()
    # rint (xx,'wow')
    notification2.schedule("!wow!", delay=10, subtitle="wow")
    # notification.schedule('!wow!',delay=10,title= "title",subtitle='subtitle')

    x = notification2.get_scheduled()
    print(x)


def testnot():

    # import notification_old
    # notification_old.schedule('!wow55!',delay=10,subtitle='wow')

    import libs.notification as notification

    notification.schedule(
        "!wo2w!",
        delay=5,
        subtitle="subtitle",
        title="title",
        attachments=["images/black-rhino.png"],
    )
