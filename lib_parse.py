def parsepayperiod(file):
    import re
    #print (file)
    from bs4 import BeautifulSoup
    aaa=open(file,'r',encoding="utf8")
    soup = BeautifulSoup(aaa, 'html.parser')
    grandtotal = soup.find("span", id="lblGrandTotal")
    paydate = soup.find("span", id="lblPayDate")
    reghours = soup.find("span", id="lblRegHoursTotal")
    othours = soup.find("span", id="lblOTHoursTotal")
    payperiod = soup.find("span", id="lblPayPeriod")
    days=0
    day = soup.findAll("span", id=re.compile('_ct'))
    #day=soup.findAll('span', id=re.compile('^post_'))
    days= (len(day))
    #print (days,'daysss')
    temp= (paydate.text)
    temp=str.split(temp,' ')
    temp=temp[3]
    #print (temp)
    
    import datetime
    past=False
    dobj = datetime.datetime.strptime(temp, '%m/%d/%Y')
    #print (dobj.day)
    dobj2 = datetime.datetime.strftime(dobj, '%d %b %Y')



    


    #lblRegHoursTotal
    #lblOTHoursTotal
    #lblPayPeriod
    #print (grandtotal.text)
    #print (paydate.text)
    #print (grandtotal.text)
    #print (reghours)
    #print (othours)
    #print (paydate.text)
    #ddict=dobjgrandtotal.text
    totalhours=float(reghours.text)+float(othours.text)
    text='Paydate: '+str(dobj2)+' '+grandtotal.text+'\nRegHours: '+reghours.text+' '+'Othours: '+othours.text+' Shows: '+str(days)
    grandtotal=str.replace(grandtotal.text,',','')
    grandtotal=str.replace(grandtotal,'$','')
    grandtotal=float(grandtotal)

    ddict = {
            'paydate': dobj,
            'moneytotal': grandtotal,
            'reghours': reghours.text,
            'othours:': othours.text,
            'totalhours': totalhours,
            'shows':days,
            'dtext':text
    }

    
    #print (text)
    return ddict
def parse(sch,ad,usecache):
    debug=False
    ios=True

    from logging import NOTSET
    import os
    #
    appname = ""
    appauthor = "Acme"
    #a= (	(appname, appauthor))
    #a2=open(a,'w')
    #a2.write('test')
    #from os import *

    #ad=config_file
    import lib_createcache
    from bs4 import BeautifulSoup
    global mj
    global mj2
    global mj3
    global l
    global firstName
    global lastName

    l=[]
    
    d=[]
    ti=[]
    j=[]
    s=[]
    v=[]
    l=[]
    l2=[]
    c=[]
    ty=[]
    p=[]
    st=[]
    n=[]
    tk=[]
    pl=[]
    p2=[]
    dd={}
    mj=[]
    mj2=[]
    mj3=[]
    joob3=[]
    l2=[]

    aaa=open(sch,'r',encoding="utf8")
    encoding="utf8"

    #ab=aaa.read()
    soup = BeautifulSoup(aaa, 'html.parser')

    nn=(soup.find_all('span'))
    for i in range(len(nn)):
        try:
            realName= (nn[i].get_text())
            lastName,firstName=str.split(realName,', ')
        except:
            ''

    ab=(soup.find_all('tr'))
    



    fullnj=[]
    for i in range(len(ab)):
        nj=[]
        ax=(ab[i].find_all('td'))



        date= (ax[0].get_text())
        time=(ax[1].get_text())
        jobid=(ax[2].get_text())
        show=(ax[3].get_text())
        venue=(ax[4].get_text())
        locationclient=(ax[5].get_text())
        typeposition=(ax[6].get_text())
        details=(ax[7].get_text())
        
        status=(ax[8].get_text())
        notes=(ax[9].get_text())
        tk=(ax[10].get_text())
        conf=(ax[11].get_text())


        nj.append (ax[0].get_text())
        nj.append(ax[1].get_text())
        nj.append(ax[2].get_text())
        nj.append(ax[3].get_text())
        nj.append(ax[4].get_text())
        nj.append(ax[5].get_text())
        nj.append(ax[6].get_text())
        nj.append(ax[7].get_text())
        
        nj.append(ax[8].get_text())
        nj.append(ax[9].get_text())
        nj.append(ax[10].get_text())
        nj.append(ax[11].get_text())
        nj.append(ax[12].get_text())
        if 'dgR' in str(ax[13]):
            xx=str(ax[13])
            f=str.split(xx,'"')
            nj.append(f[3])



        if i>0:
            mj3.append(nj)

        

    
    #for i in range(15,len(ab)-15):
    #print (len(ab))

    for i in range(len(ab)):
        asds= str(ab[i].contents)
        
        if 'input2 name' not in asds:


            l.append( (ab[i].get_text()))
        if 'input4 name' in asds:
            l.append(str(ab[i]))
    #for z in range(len(mj3)):
        #print (mj3[z])
    return mj3



x=parsepayperiod('y.html')
print (x)