def create_notification(x,y,debug):
    print (x,'XDXXX','y',y)
    import logging
    import datetime
    now = datetime.datetime.now()
    from kivy.utils import platform
    print (platform,'KIVY PLATFORM')
    if platform == 'linux':
        print ('omgitslinux')
    d1=float(y['not1time'])
    d2=float(y['not2time'])

    d1=d1*60
    d2=d2*60

    #print (d1,d2,'omgwtfitsday1')
    

    showdatetime=x['date']+' '+x['time']

    showdatetime = datetime.datetime.strptime(showdatetime, '%m/%d/%Y %H:%M')
    dif= (showdatetime-now)

    delay2= (dif.total_seconds())
    #print (delay2,'delay2',d2)
    #print (type(delay2),type(d2))
    delay2=delay2-d2
    #print (delay2,'delay2-d2',d2)

    delay1= (dif.total_seconds())
    #print (delay1,'delay1')

    delay1=delay1-d1
    #print (delay1,'delay2-d1')

    #if debug==56:
    #    delay1=5
    #    delay2=10
    #logging.info(pf,delay2)
    print (delay1,delay2,'DELAY!@')
    #pf='W'
    #try:
    #    y['not2time'],junk=str.split(y['not2time'],'.')
    #    y['not1time'],junk=str.split(y['not1time'],'.')
    #except:
    #    ''
    if platform =='win':
        logging.info('windows notifications not supported')
    if platform !='win':
        if platform !='win':
            print('IOS BITCHES',x['show'],delay2,d2,now,showdatetime)
            

            import notification
            if y['not']==True and y['not2']==True:
                #print (x,'xxxxxx')
                #print (x['show'])
                notification.schedule(x['show'],delay=delay2,title= y['not2time']+' Minutes From Now: '+x['time'],subtitle=x['venue'],attachments=['images/black-rhino.png'],sound_name='images/beep.wav')
                print ('added not 2 ',delay2)

            if y['not']==True and y['not1']==True:
                notification.schedule(x['show'],delay=delay1,title= y['not1time']+' Minutes From Now:  '+x['time'],subtitle=x['venue'],attachments=['images/black-rhino.png'],sound_name='images/beep.wav')
                print ('added not 1 ',delay1)

            #import notification_old
            #x6=notification.get_scheduled()
            #print (len(x6),'omggggg')
            #print(type(datetime_object))
            #print(datetime_object)


    logging.debug (x)

def cancel_notification():
    import platform
    import logging
        
    from kivy.utils import platform
    print (platform,'KIVY PLATFORM')
    if platform == 'ios':
        import notification_old as notification
        logging.debug('IOS BITCHES')
        notification.cancel_all()
    









if __name__ == "__main__":
    create_notification({'date': '04/01/2022', 'time': '18:30', 'job': '25321', 'show': '(TMA) BILLIE EILISH', 'venue': 'T-MOBILE ARENA', 'location': 'LOADING DOCK', 'client': 'MGM RESORTS', 'type': 'SHOW', 'pos': 'ME', 'details': '\xa0', 'status': 'Confirmed', 'notes': 'ALL VAX CREW; MASK (no gaiters or bandanas), HARD HAT, SAFETY VEST, GLOVES, & PROTECTIVE TOE BOOTS; BRING PARKING STUB TO VALIDATE// Covid Testing', 'timekeep': '\xa0', 'plus': '\xa0', 'canceled': False, 'confirmid': '', 'lunches': '', 'endtime': '', 'is_new': False})