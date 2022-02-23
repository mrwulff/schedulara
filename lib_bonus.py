def create_notification(x,y):
    import logging
    import datetime
    now = datetime.datetime.now()
    import platform
    d1=float(y['not1time']*60)
    d2=float(y['not2time']*60)

    

    datetime_str = '09/19/18 13:55:26'
    showdatetime=x['date']+' '+x['time']

    showdatetime = datetime.datetime.strptime(showdatetime, '%m/%d/%Y %H:%M')
    dif= (showdatetime-now)
    delay2= (dif.total_seconds(),type(dif))
    deyay2=delay2-d2

    delay1= (dif.total_seconds(),type(dif))
    deyay1=delay2-d1


    pf= platform.platform()
    logging.info(pf,delay2)
    print (pf)
    pf='W'
    if pf[0]=='W':
        logging.info('windows notifications not supported')
    if pf[0]!='W':
        logging.debug('IOS BITCHES',pf)
        

        import notification
        if y['not']==True and y['not2']=True:
            notification.schedule(x['show'],delay=delay2,title=x['venue'])

        if y['not']==True and y['not1']=True:
            notification.schedule(x['show'],delay=delay1,title=x['venue'])


        x=notification.get_scheduled()
        print (x,'omggggg')
        #print(type(datetime_object))
        #print(datetime_object)


    logging.debug (x)

def cancel_notification():
    import platform

    pf= platform.platform()
    if pf[0]!='W':
        logging.debug('IOS BITCHES',pf)
        notification.cancel_all()
    









if __name__ == "__main__":
    create_notification({'date': '04/01/2022', 'time': '18:30', 'job': '25321', 'show': '(TMA) BILLIE EILISH', 'venue': 'T-MOBILE ARENA', 'location': 'LOADING DOCK', 'client': 'MGM RESORTS', 'type': 'SHOW', 'pos': 'ME', 'details': '\xa0', 'status': 'Confirmed', 'notes': 'ALL VAX CREW; MASK (no gaiters or bandanas), HARD HAT, SAFETY VEST, GLOVES, & PROTECTIVE TOE BOOTS; BRING PARKING STUB TO VALIDATE// Covid Testing', 'timekeep': '\xa0', 'plus': '\xa0', 'canceled': False, 'confirmid': '', 'lunches': '', 'endtime': '', 'is_new': False})