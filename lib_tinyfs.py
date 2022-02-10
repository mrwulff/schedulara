def stats(xxx,now,search):
    import datetime
    cf=0
    week=0
    tot=0
    for i in range(len(xxx)-1):
        v= (xxx[i][10])
        if search.lower() in str(xxx[i]).lower() or len(search)==0:
            tot=tot+1
            if v=='Confirmed':
                cf=cf+1
            dobj = datetime.datetime.strptime(xxx[i][0]+'/'+xxx[i][1], '%m/%d/%Y/%H:%M')
            daysaway= (dobj.date()-now.date())
            a = int(daysaway.days)
            if a<7 and a>=0:
                week=week+1
    return cf,week,tot

def format_text(i,xxx,now,page):
    import datetime
    import humanize
    past=False
    dobj = datetime.datetime.strptime(xxx[i][0]+'/'+xxx[i][1], '%m/%d/%Y/%H:%M')
    try:
        dobj = datetime.datetime.strptime(xxx[i][0]+'/'+xxx[i][1], '%m/%d/%Y/%H:%M')
    except:
        ('errrrror:',xxx[i])
    diff=now-dobj
    if now.date()>dobj.date():
        past=True
    diff2=humanize.naturaltime(now - dobj)
    diff2=str(diff2)
    diff=str(diff)
    if 'irmed' not in xxx[i][10]:
        xxx[i][10]='[color=ff0000ff]'+xxx[i][10]+'[/color]'
    if 'irmed'  in xxx[i][10]:
        xxx[i][10]='[color=00ff00ff]'+xxx[i][10]+'[/color]'
    fdate=(dobj.strftime("%A"))+', '+(dobj.strftime("%m"))+'/'+(dobj.strftime("%d"))+ ' ' +(dobj.strftime("%I"))+':'+(dobj.strftime("%M"))+'[sup]'+(dobj.strftime("%p"))+'[/sup]'
    if now.date()==dobj.date():
        #today='[color=#00007fff][b]TODAY[/b][/color]\n'
        today='[size=0 sp][b][/b][/size]'
    else:
        today=''
    rindex=(len(xxx)-1)-i
    rindex=i
    texta=today+''+fdate+' \n'+xxx[i][3]+' '+'\n[b]'+xxx[i][4]+'\n[/b][size=13 sp]'+xxx[i][5]+'\n'+xxx[i][8]+' '+xxx[i][7]+' '+xxx[i][10]+'\n'+diff2+'[size=1 sp]***'+str(rindex)
    if past==True:
        texta='[size=12 sp]'+fdate+'\n'+xxx[i][3]+'\n'+xxx[i][4]+'[size=1 sp]***'+str(rindex)
    
    if page=='index':    
        return texta
    if page=='info':
        return today,fdate
